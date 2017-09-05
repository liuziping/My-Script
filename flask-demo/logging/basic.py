import logging

logging.basicConfig(level=logging.DEBUG,
			format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(lineno)s %(message)s',
			datefmt='%d %b %Y %H:%M:%S',
			filename='myapp.log',
			filemde='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter= logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")

