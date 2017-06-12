import GroupMeClasses
import sys
#import BotInfo
BotInfo = __import__('TestBotInfo')
import BotMessages
import time
from random import randint
def main():
    messages = BotMessages.messages
    bot = GroupMeClasses.generalBot(BotInfo.botID,BotInfo.botName,messages)
    #groupme = GroupMeClasses.GroupMe(BotInfo.token,BotInfo.groupID)
    #groupme.sendMessage('I Started the bot')
    if len(sys.argv) >1 :
        previous =groupme.getLastMessageID()
    else:
        previous =''
    count =0
    while True:
        if count %60==0 : print (count/60)
        terms =BotMessages.terms
        #print(terms)
        newMessages = groupme.getMessages('since_id',previous)
        if newMessages:
            hits = bot.searchMessages(terms,newMessages['response']['messages'])
            if hits:
                print('yes')
                user=[]
                for hit in hits:
                    user.append(hit)
                bot.customAction(user)
                print('out')
                #groupme.sendMessage(BotMessages.fromCreator,user)
            previous= groupme.getLastMessageID()
        count+=1
        time.sleep(1)
def runWeb(response):
    messages = BotMessages.messages
    bot = GroupMeClasses.generalBot(BotInfo.botID,BotInfo.botName,messages)
    #groupme = GroupMeClasses.GroupMe(BotInfo.token,BotInfo.groupID)
    terms =BotMessages.terms
    hits = bot.searchMessages(terms,[response])
    if hits:
        print('yes')
        user=[]
        for hit in hits:
            if 'bot' in hit['sender_type']:
                continue
            user.append(hit)
            #bot.sendMessage(hit['text'])
        bot.customAction(user)

        print('out')

if __name__=="__main__":
    main()