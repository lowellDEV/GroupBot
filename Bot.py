#Bot= __import__('BotInfo') #user and bot info
Bot= __import__('TestBotInfo') #for testing
import requests
from random import randint
import json
import cgi
gmURL = 'https://api.groupme.com/v3'
URLB = gmURL+'/bots'

def sendMessage(msg):
    jsonData =json.dumps({'bot_id':Bot.botID,'text':msg})
    r= requests.post(URLB+'/post',jsonData)

def getMessages(extraKey='',extraVal=''):
    if extraKey:
        params = {'token':str(Bot.token),extraKey:extraVal}
    else:
        params = 'token='+str(Bot.token)
    r = requests.get(gmURL+'/groups/'+Bot.groupID+'/messages',params)
    if r.status_code == 304:
        return False
    else:
        return  r.json()

def getNewMessages(previous):
    return getMessages('since_id',previous)
    # r= requests.get(gmURL+'/groups/'+Bot.groupID+'/messages',params).json()
    
    # if r.status_code == 304:
        # return []
    # else:
        # return r.json()    
        
def getMessagesRequest(extraKey='',extraVal=''):
    if extraKey:
        params = {'token':str(Bot.token),extraKey:extraVal}
    else:
        params = 'token='+str(Bot.token)
    return  requests.get(gmURL+'/groups/'+Bot.groupID+'/messages',params)
    
def getMessagesHuman():
     msg= json.loads(getMessages())
     print(msg['name']+':'+msg['text'])

def searchForTerms(previous="",term ='text'):
    termList =[]
    if previous is not "":
        #print(previous)
        preCheck= getNewMessages(previous)
        messages = ''
        #print(preCheck)
        if preCheck is not False:
            messages =preCheck['response']['messages']
    
    else:
        messages =getMessages()['response']['messages']
    
    #if not messages: return False
    
    for msg in messages:
        if term in  msg['text'].lower():
            termList.append(msg)
            #getStockMessage(randint(0,3))
            likeMessage(msg['id'])
            print(msg['text'])
    
    return  termList   


    
    
def sendStockMessage(num,*args):
    if num is 0:
       sendMessage("Stock Message 1")
    elif num is 1:
        sendMessage("Stock Message 2")
    elif num is 2:
        sendMessage("Stock Message 3")
    else:
        sendMessage("Stock Message 4")

def likeMessage(msgID):
    jsonData =json.dumps({'bot_id':Bot.botID})
    r= requests.post(gmURL+'/messages/'+Bot.groupID+'/'+msgID+'/like?token='+Bot.token,jsonData)
    #print(r.request.path_url)
    print(msgID)

def getLastMessageID():
    msg= getMessages('limit=1')['response']['messages']
    return msg[0]['id']
 

def thankSupporter(hit):
    #print('_____________________________________')
    #print(hit)
    #raw_input('____________________________________')
    msg ="I have the best people. THANK YOU for supporting me."
    user =[]
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
    
    jsonData =json.dumps({'bot_id':Bot.botID,'text':msg,
        'attachments':[{'type':'mentions','user_ids':user,'loci':loc}]})
    
    r= requests.post(URLB+'/post',jsonData)
    #print(jsonData)