import GroupMeClasses
#import BotInfo
BotInfo = __import__('TestBotInfo')
import time
from random import randint
def main():
    messages = ['Test Message one','Test Message 2']
    bot = GroupMeClasses.generalBot(BotInfo.botID,messages)
    groupme = GroupMeClasses.GroupMe(BotInfo.token,BotInfo.groupID)
    if len(sys.argv) >1 :
        previous =groupme.getLastMessageID()
    else:
        previous =''
    count =0
    while True:
        time.sleep(10)
        if count %6==0 : print (count/6)
        
        hits = bot.searchMessages(['Spoiler Alert','Spoilers'],groupme.getMessages())
        if hits:
            user=[]
            for hit in hits:
                user.append(hit['sender_id'])
            bot.defaultAction()
            groupme.sendMessage('Stop Spoiling',user)
        previous= bot.getLastMessageID()
        count+=1
        
if __name__=="__main__":
    main() 