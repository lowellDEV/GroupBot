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

def searchForTrump(previous=""):
    trumpList =[]
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
        if 'trump' in  msg['text'].lower():
            trumpList.append(msg)
            #getStockMessage(randint(0,3))
            likeMessage(msg['id'])
            print(msg['text'])
    
    return  trumpList   
def searchForTrumpWeb(previous=""):
    trumpList =[]
    if previous is not "":
        #print(previous)
        preCheck= cgi.FieldStorage()
        messages = []
        #print(preCheck)
        if preCheck is not False:
            print(preCheck)
            messages.append(preCheck)
    
    else:
        
        messages =getMessages()['response']['messages']
    
    #if not messages: return False
    
    for msg in messages:
        if 'trump' in  msg['text'].lower():
            trumpList.append(msg)
            #getStockMessage(randint(0,3))
            likeMessage(msg['id'])
            print(msg['text'])
    
    return  trumpList     

    
    
def sendStockMessage(num,*args):
    if num is 0:
       sendMessage("MEXICO does not have the best people. I have the best people. Believe it folks.")
    elif num is 1:
        sendMessage("We can no longer allow CHYNA to attack Russia.")
    elif num is 2:
        sendMessage("You will not lose your covfefe.")
    else:
        sendMessage("bigly")

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