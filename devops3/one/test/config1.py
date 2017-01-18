#coding:utf-8
import ConfigParser

def getconfig(filename,section=''):
    cf = ConfigParser.ConfigParser()
    cf.read(filename)
    cf_items = dict(cf.items(section)) if cf.has_section(section) else {} # 判断section是否存在，存在则把数据存入字典

    return cf_items

#if __name__ == '__main__':
#        conf = getconfig('test.conf','web')
#        print conf
#        print conf['port'] # 以字典的方式读取数据
#        print conf.get('path') # config模块的方式读取数据
