#coding:utf-8
import logging

def LoggingDemo():
	""" 
		just demo basic usage of logging module
	"""
	InitLogging("/tmp/test.log")
	logging.debug("this is debug message")
	logging.info("this is info message")
	logging.warning("this is warning message")
	logging.error("this is error message")

def InitLogging(logfilename):
	logging.basicConfig(level = logging.DEBUG,
			format   = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
			datefmt  = '%d-%b-%Y %H:%M:%S',
			filename = logfilename,
			filemde  = 'w');
if __name__=="__main__":
	LoggingDemo()

'''
其他模块调用logging
cat  test.py
	import logging,util

	basicdemo.InitLogging("/tmp/config.log")
	logging.debug('this is DEBUG')
'''
