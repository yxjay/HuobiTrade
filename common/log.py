import logging,os
import configparser
conf = configparser.ConfigParser()
conf.read("config/trade.conf")

BASE_DIR = conf.get("default","logdir")
if not BASE_DIR:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = BASE_DIR + '/trade.log'


#logfmt = conf.get("default", "logfmt")
logfmt = "%(asctime)s %(levelname)s %(module)s %(filename)s %(pathname)s %(funcName)s %(message)s"

class getLogger:
    #def get_logger():
    def __init__():
        fh = logging.FileHandler(log_dir, encoding='utf-8') 
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        fm = logging.Formatter(logfmt) 
        logger.addHandler(fh) 
        fh.setFormatter(fm) 
        
def get_logger():
    fh = logging.FileHandler(log_dir, encoding='utf-8') 
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fm = logging.Formatter(logfmt) 
    logger.addHandler(fh) 
    fh.setFormatter(fm) 
    return logger
