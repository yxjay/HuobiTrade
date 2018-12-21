# -*- coding: utf-8 -*-
from websocket import create_connection
import gzip
import time
import json
import os
from multiprocessing import Process
import _thread as thread
from common import log
from common import conf
from analizer import controller
from alarm import sendemail

conf = conf.getconf()
LOG = log.getlogger()

sendemail("hello")
timeHistory = conf.getint("default", "saveCount")
LOG.info(timeHistory)

def nows():
    return int(time.time())

def nowts():
   return int(round(time.time()*1000))

buyList = {"elf": 1.2686}
coinList = ["btc","bch","eth","etc","ltc","eos","xrp","omg","dash","zec","iota",
            "ada","steem","soc","ctxc","act","btm","bts","ont","iost","ht",
            "trx","dta","neo","qtum","smt","ela","ven","theta","snt","xem",
            "ruff","hsr","let","mds","storg","elf","itc","cvc","gnt"]

tradetype = "usdt"

infoType = ["kline", "depth", "trade","detail"]

klineTradeStr = """{"sub": "market.%susdt.kline.1min","id": "id10"}""" % coinList[1]     # from ,to 
depthTradeStr = """{"sub": "market.%susdt.depth.step0", "id": "id11"}""" % coinList[1]
tradeTradeStr =  """{"sub": "market.%susdt.trade.detail", "id": "id15"}""" % coinList[1]


ws = None

def subscribe(ws, tradeStr):
    ws.send(tradeStr)
    while(1):
        #with open("/tmp/huobi.log","a+") as f:
        #    f.write((str(nows()) + " tradeStr=" + tradeStr + " ws.status=" + str(ws.status))+"\n")
        if ws.status != 101:
            ws = create_connection("wss://api.huobi.br.com/ws")
            LOG.error(str(nows()) + " tradeStr=" + tradeStr + "  ws.status=" + str(ws.status))

        compressData=ws.recv()
        result=gzip.decompress(compressData).decode('utf-8')
        if result[:7] == '{"ping"':
            ts=result[8:21]
            pong='{"pong":'+ts+'}'
            ws.send(pong)
            ws.send(tradeStr)
        else:
            result = json.loads(result)
            if "tick" in result:
                _tick = result.get("tick")
                if "trade.detail" in tradeStr or "data" in _tick:
                    print([result.get("ch"), _tick.get("data")])
                else:
                    print([result.get("ch"), _tick])

if __name__ == '__main__':
    while(1):
        try:
            ws = create_connection("wss://api.huobi.br.com/ws")
            break
        except:
            print('connect ws error,retry...')
            time.sleep(5)
    thread.start_new_thread(subscribe, (ws, tradeTradeStr))
    thread.start_new_thread(subscribe, (ws, klineTradeStr))

    while(1):
        pass
