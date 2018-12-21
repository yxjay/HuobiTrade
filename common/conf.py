import configparser
conf = configparser.ConfigParser()
conf.read("config/trade.conf")

def getconf():
     return conf
