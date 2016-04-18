#coding:utf-8
import logging

def InitLogger(filename,level,name):
	'''
		init  logging 
		由于logging运行的机制是，一旦实例化一个logging实例，该实例下如果有多个handler，
		任何一个handler执行一次，其他handler符合条件level的也会跟着执行一次。如果两个handler
		输出定义的日志文件不一样，level级别低的日志文件就会收到其他所有高level的handler的日志

		在输出多个日志文件的场景下，可以设置多个logging实例，取不同的名字，handler处理时
		互不影响
	'''
	# create a logging object 
	logger = logging.getLogger(name)
	logger.setLevel(level)

    # format log     
	formatter = logging.Formatter('%(asctime)s  %(name)s - %(levelname)s - %(filename)s -[line:%(lineno)s] - %(message)s')

    # create the logging file handler and format the log file  
	fh = logging.FileHandler(filename,mode = 'a+')
	fh.setFormatter(formatter)

    # logger object load the handler
	logger.addHandler(fh) 

	return logger

if __name__ == '__main__':
	logger = InitLogger('/tmp/test.log',logging.INFO,'test')
	logger.info("just a info")
	logger.debug("just a debug")

    #这种写法和上面一样，适用于参数比较少的场景
    InitLogger('/tmp/test.log',logging.INFO,'test').info('just a info')

'''
其他模块调用方法
cat  test.py 
	import logging,loggerdemo
 
	logger = loggerdemo.InitLogger('/tmp/test.log',logging.DEBUG,'test')
	logger.info("just a info")
	logger.debug("just a debug")

    logger1 = loggerdemo.InitLogger('/tmp/test1.log',logging.INFO,'test1')
	logger1.info("just a info")
	logger1.debug("just a debug")

    等价于：
    loggerdemo.InitLogger('/tmp/test1.log',logging.INFO,'test1').info("just a info")

'''
