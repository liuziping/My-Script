#!/usr/bin/env python 
#coding: utf-8
import csv
import MySQLdb

mydb = MySQLdb.connect(host='192.168.1.251',
    user='liuziping',
    passwd='liuziping_123456',
    db='IT',charset='utf8')
cursor = mydb.cursor()

csv_data = csv.reader(file('lz.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO employee(num,branch,title,name,sex,shenfen_num,shengri,tel,start,zhuanzheng,work,shebao,QQ,weixin,bank_num,kaihu,info,computer,status) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s","%s","%s","%s")' %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18]))
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"
