import requests
import json
import sys
from random import randint


class generalBot(object):
    '''A class that represents a bot
        needs a botID and has a messagelist optional'''
    baseUrl = 'https://api.groupme.com/v3'
    botUrl= baseUrl +'/bots'
    botId = ''
    interval = 5
    messageList =['Bot Triggered']


    def __init__(self,botId,messageList):
        self.botId =botId
        self.messageList = messageList


    def sendMessage(self,msg,user=[]):
        if user:
            loc = []
            name = []
            count =0
            for u in hit:
                user.append(u['sender_id'])
                loc.append([count,len(u['name'])])
                name.append(u['name'])
                count+=len(u['name'])+2
            for n in list(set(name)):
                msg = '@'+n+' '+msg
        jsonData =json.dumps({'bot_id':self.botId,'text':msg})
        requests.post(self.botUrl+'/post',jsonData)


    def searchMessages(self,terms,messages):
        hitList =[]
        for msg in messages:
            for term in terms:
                if term.lower() in msg['text'].lower():
                    hitList.append(msg)
                    print(msg['text'])
        return  hitList   


    def defaultAction(self):
        self.sendMessage(self.messageList[randint(0,len(self.messageList)-1)])


    def customAction(self,file):
        '''Unsafe; run a custom code'''
        exec(file)

        
class GroupMe(object):
    token =''
    baseURL = 'https://api.groupme.com/v3'
    groupID = ''
    baseGuid = 'GROUPMEBOTSOURCED'


    def __init__(self,token,groupID):
        self.token = token
        self.groupID =groupID


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


    def likeMessage(self,msgID):
        jsonData =json.dumps({'bot_id':Bot.botID})
        requests.post(self.baseURL+'/messages/'+self.groupID+'/'+msgID+'/like?token='+self.token,jsonData)


    def getLastMessageID(self):
        msg= self.getMessages('limit',1)['response']['messages']
        return msg[0]['id']
    

    def sendMessage(self,msg,user=[]):
        loc = []
        name = []
        attachments =[]
        userID=[]
        if user: 
            count =0
            for u in user:
                if type(u) is not dict:
                    continue
                userID.append(u['sender_id'])
                loc.append([count,len(u['name'])])
                name.append(u['name'])
                count+=len(u['name'])+2
            for n in list(set(name)):
                msg = '@'+n+' '+msg
            attachments.append({'type':'mentions','user_ids':userID,'loci':loc})
        jsonData =json.dumps({'message':{'source_guid':self.baseGuid+str(randint(10,10100)),'text':msg,'attachments':attachments}})
        print(jsonData)
        headers = {'Content-type': 'application/json'}
        r=requests.post(self.baseURL+'/groups/'+self.groupID+'/messages?token='+self.token,data= jsonData, headers=headers)  
        print(r.raise_for_status())
