import GroupMeClasses
import sys
#import BotInfo
BotInfo = __import__('TestBotInfo')
import time
from random import randint
def main():
    messages = ['Test Message one','Test Message 2']
    bot = GroupMeClasses.generalBot(BotInfo.botID,messages)
    groupme = GroupMeClasses.GroupMe(BotInfo.token,BotInfo.groupID)
    groupme.sendMessage('I Started the bot')
    if len(sys.argv) >1 :
        previous =groupme.getLastMessageID()
    else:
        previous =''
    count =0
    while True:
        if count %6==0 : print (count/6)
        terms =['Spoiler Alert','Spoilers']
        hits = bot.searchMessages(terms,groupme.getMessages()['response']['messages'])
        if hits:
            print('yes')
            user=[]
            for hit in hits:
                user.append(hit)
            bot.defaultAction()
            groupme.sendMessage('Stop Spoiling',user)
        previous= groupme.getLastMessageID()
        count+=1
        time.sleep(1)
if __name__=="__main__":
    main() 