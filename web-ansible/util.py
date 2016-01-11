#coding:utf-8
import logging

def InitLogger(filename,level,name):
	'''
		init  logging 
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
