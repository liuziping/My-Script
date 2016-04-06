# -*- encoding: utf-8 -*-
import logging
import MySQLdb as mysql

class Cursor():
    def __init__(self, config):
        self.config = dict([(k[6:], config[k]) for k in config if k.startswith('mysql_')])
        if 'port' in self.config:
            self.config['port'] = int(self.config['port'])
        if self.config:
            self.connect_db()

    def connect_db(self):
        self.db = mysql.connect(**self.config)
        self.db.autocommit(True)
        self.cur = self.db.cursor()

    def close_db(self):
        self.cur.close()
        self.db.close()

    def execute(self, sql):
        try:
            return self.cur.execute(sql)
        except:
            self.close_db()
            self.connect_db()
            return self.cur.execute(sql)
    
    def fetchone(self):
        return self.cur.fetchone()

    def fetchall(self):
        return self.cur.fetchall()

    def insert_sql(self, table_name, data):
        fields, values = [], []
        for k, v in data.items():
            fields.append(k)
            values.append("'%s'" % v)
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (table_name, ','.join(fields), ','.join(values))
        logging.getLogger().info("Insert sql: %s" % sql)
        return sql

    def execute_insert_sql(self, table_name, data):
        sql = self.insert_sql(table_name, data)
        return self.execute(sql)

    def select_sql(self, table_name, fields, where=None, order=None, asc_order=True, limit=None):
        if isinstance(where, dict) and where:
            conditions = []
            for k, v in where.items():
                if isinstance(v, list):
                    conditions.append("%s IN (%s)" % (k, ','.join(v)))
                elif isinstance(v, str) or isinstance(v, unicode):
                    conditions.append("%s='%s'" % (k, v))
                elif isinstance(v, int):
                    conditions.append("%s=%s" % (k, v))
 
            sql = "SELECT %s FROM %s WHERE %s" % (','.join(fields), table_name, ' AND '.join(conditions))
        elif not where:
            sql = "SELECT %s FROM %s" % (','.join(fields), table_name)
        else:
            sql = ""
        if order and (isinstance(order, str) or isinstance(order, unicode)):
            sql = "%s ORDER BY %s %s" % (sql, order, 'ASC' if asc_order else 'DESC')
        if limit and isinstance(limit, tuple) and len(limit) == 2:
            sql = "%s LIMIT %s,%s" % (sql, limit[0], limit[1])
        logging.getLogger().info("Select sql: %s" % sql)
        return sql

    def get_one_result(self, table_name, fields, where=None, order=None, asc_order=True, limit=None):
        sql = self.select_sql(table_name, fields, where, order, asc_order, limit)
        if not sql:
            return None
        self.execute(sql)
        result_set = self.fetchone()
        if result_set:
            return dict([(k, '' if result_set[i] is None else result_set[i]) for i,k in enumerate(fields)])
        else:
            return {}

    def get_results(self, table_name, fields, where=None, order=None, asc_order=True, limit=None):
        sql = self.select_sql(table_name, fields, where, order, asc_order, limit)
        self.execute(sql)
        result_sets = self.fetchall()
        return [dict([(k, '' if row[i] is None else row[i]) for i,k in enumerate(fields)]) for row in result_sets]

    def update_sql(self, table_name, data, where, fields=None):
        if not (where and isinstance(where, dict)):
            return ""
        where_cond = ["%s='%s'" % (k, v) for k,v in where.items()]
        if fields:
            conditions = ["%s='%s'" % (k, data[k]) for k in fields]
        else:
            conditions = ["%s='%s'" % (k, data[k]) for k in data]
        sql = "UPDATE %s SET %s WHERE %s" % (table_name, ','.join(conditions), ' AND '.join(where_cond))
        logging.getLogger().info("Update sql: %s" % sql)
        return sql

    def execute_update_sql(self, table_name, data, where, fields=None):
        sql = self.update_sql(table_name, data, where, fields)
        if sql:
            return self.execute(sql)
        else:
            return ""

    def delete_sql(self, table_name, where):
        if not (where and isinstance(where, dict)):
            return ""
        where_cond = ["%s='%s'" % (k, v) for k,v in where.items()]
        sql = "DELETE FROM %s WHERE %s" % (table_name, ' AND '.join(where_cond))
        logging.getLogger().info("Delete sql: %s" % sql)
        return sql

    def execute_delete_sql(self, table_name, where):
        sql = self.delete_sql(table_name, where)
        if sql:
            return self.execute(sql)
        else:
            return ""

    def if_userid_exist(self, user_id):
        result = self.get_one_result('user', ['id'], {'id': user_id})
        if result:
            return True
        else:
            logging.getLogger().error("user '%s' is not exist" % user_id)
            return False

    def if_groupid_exist(self, group_id):
        result = self.get_one_result('group', ['id'], {'id': group_id})
        if result:
            return True
        else:
            logging.getLogger().error("group '%s' is not exist" % group_id)
            return False

    def getinfo(self, table_name, fields):
        '''
        查询单个数据表内容，fields首字段为key
        fields为两个字段，返回{v1: v2, ...}，格式为 ['field1','field2'], 例如['id','name'],['name','r_id']
        返回结果一，两列都是字符串如：用户id2name {'1':'tom','2','jerry'}; 组信息id2name {'1':'sa','2':'ask'}
        返回结果二，第二列是个列表如：用户权限信息：{u'songpeng': [u'1', u'2'], u'admin': [u'1', u'2', u'4', u'3']}

        fields为多于两个字段，返回{v1: {k2: v2, k3: v3, ...}, ...}，格式为 ['field1', 'field2', 'field3', ...]
        返回结果，从第二列的内容保存在字典中，如：项目权限表：{'1': {'group_all_perm': [u'3', u'4'], 'user_all_perm': [u'2', u'4', u'5']}, '3': {'group_all_perm': [u'1'], 'user_all_perm': [u'2', u'5']}}
        '''
        def val(k, v):
            special_fields = ('r_id','p_id','group_all_perm','group_rw_perm','user_all_perm','user_rw_perm')
            return v.split(',') if k in special_fields else v

        if len(fields) < 2:
            return None
        result = self.get_results(table_name,fields)
        if len(fields) == 2:
            return dict([(str(x[fields[0]]), val(fields[1], x[fields[1]])) for x in result])
        else:
            return dict([(str(x[fields[0]]), dict([(k, val(k, x[k])) for k in fields[1:]])) for x in result])

    @property
    def users(self):
        return self.getinfo('user', ['id', 'username'])

    @property
    def groups(self):
        return self.getinfo('user_group', ['id', 'name'])

    @property
    def user_groups(self):
        return self.getinfo('user', ['id', 'r_id'])

    @property
    def projects(self):
        return self.getinfo('project', ['id', 'name'])

    @property
    def project_perms(self):
        return self.getinfo('project_perm', ['id', 'group_all_perm', 'group_rw_perm', 'user_all_perm', 'user_rw_perm'])

