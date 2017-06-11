import Trump
import time
from random import randint
def main():
    if len(sys.argv) >1 :
        previous =Trump.getLastMessageID()
    else:
        previous =''
    count =0
    while True:
        time.sleep(10)
        if count %6==0 : print (count/6)
        
        hits = Trump.searchForTrump(previous)
        if hits:
            user=[]
            for hit in hits:
                user.append(hit['sender_id'])
            Trump.sendStockMessage(randint(0,3),user)
            Trump.thankSupporter(hits)
        previous=Trump.getLastMessageID()
        count+=1
if __name__=="__main__":
    main() 