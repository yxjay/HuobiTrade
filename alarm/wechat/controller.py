import requests
import json
from common import conf
from common import log

corpid = conf.get("alarm", "wechat_corpid")
corpsecret = conf.get("alarm", "wechat_corpsecret")

def get_token():
  
  url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
  values = {'corpid' : corpid ,
            'corpsecret': corpsecret,
           }
  req = requests.post(url, params=values) 
  data = json.loads(req.text)
  return data["access_token"]
  
def sendwechat(msg):
  url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+get_token()
  values = """{"touser" : "1" ,
      "toparty":"1",
      "msgtype":"text",
      "agentid":"1",
      "text":{
        "content": "%s"
      },
      "safe":"0"
      }""" %(msg)
   
  data = json.loads(values)
  req = requests.post(url, values) 
  
