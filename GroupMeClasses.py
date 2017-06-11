import requests
from random import randint
import json

class generalBot(object):
    '''A clas that represents a bot
        needs a botID and has a messagelist optional'''
    baseUrl = 'https://api.groupme.com/v3'
    botUrl= baseUrl +'/bots'
    botId = ''
    interval = 5
    messageList =['Bot Triggered']
    
    def __init__(self,botId,messageList)
        self.botId =botId
    
    def sendMessage(self,msg,user=[]):
        if user:
            loc = [], name = [],count =0
            for u in hit:
                user.append(u['sender_id'])
                loc.append([count,len(u['name'])])
                name.append(u['name'])
                count+=len(u['name'])+2
            for n in list(set(name)):
                msg = '@'+n+' '+msg
        jsonData =json.dumps({'bot_id':self.botID,'text':msg})
        requests.post(self.botUrl+'/post',jsonData)

    def searchMesaages(terms,messages):
        hitList =[]   
        for msg in messages:
            if terms in msg['text'].lower():
                hitList.append(msg)
                print(msg['text'])
        return  hitList   
    
    def defaultAction():
        sendMessage(messageList[randint(0,len(messageList)-1)])
    
    def customAction(file):
        '''Unsafe; run a custom code'''
        exec(file)

        
class GroupMe(object):
    token =''
    baseUrl = 'https://api.groupme.com/v3'
    groupID = ''
    baseGuid = 'GroupMEBOTSOURCED'
    
    def __init__(self,token,groupID)
        self.token = token
    
    def getMessages(self,extraKey='',extraVal=''):
        if extraKey:
            params = {'token':str(self.token),extraKey:extraVal}
        else:
            params = 'token='+str(self.token)
        r = requests.get(self.baseURL+'/groups/'+self.groupID+'/messages',params)
        if r.status_code == 304:
            return False
        else:
            return  r.json()
    
    def likeMessage(msgID):
        jsonData =json.dumps({'bot_id':Bot.botID})
        requests.post(self.baseURL+'/messages/'+self.groupID+'/'+msgID+'/like?token='+self.token,jsonData)
    
    def getLastMessageID():
        msg= getMessages('limit',1)['response']['messages']
        return msg[0]['id']
    
    def sendMessage(self,msg,user=[]):
        if user:
            loc = [], name = [],count =0
            for u in hit:
                user.append(u['sender_id'])
                loc.append([count,len(u['name'])])
                name.append(u['name'])
                count+=len(u['name'])+2
            for n in list(set(name)):
                msg = '@'+n+' '+msg
        jsonData =json.dumps({'source_guid':self.baseGuid+randint(10,10100),'text':msg})
        requests.post(self.baseUrl+'/groups/'+self.groupID+'/messages?token='+self.token,jsonData)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    