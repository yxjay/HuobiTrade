import logging,os
from common import conf
conf = conf.getconf()

BASE_DIR = conf.get("log","logdir")
LOGNAME = conf.get("log", "logname")
loglevel = conf.get("log", "loglevel")

if loglevel == "DEBUG":
    loglevel = logging.DEBUG

if not BASE_DIR:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = BASE_DIR + LOGNAME


#logfmt = conf.get("default", "logfmt")
logfmt = "%(asctime)s %(levelname)s  %(pathname)s %(lineno)d %(message)s"

fh = logging.FileHandler(log_dir, encoding='utf-8') 
logger = logging.getLogger()
logger.setLevel(loglevel)
fm = logging.Formatter(logfmt) 
logger.addHandler(fh) 
fh.setFormatter(fm) 

def getlogger():
    return logger
