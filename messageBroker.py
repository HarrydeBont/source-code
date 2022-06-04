# Attempt to create a message broker
# todo include destination in get
import queue
from cv2 import boxPoints
from objectR_handler import objecter
import datetime

# Author: H.W. de Bont May 2022

class mess_broker:
    def __init__(self):
        self.mess_queue = objecter('mess_queue', 'message' )
        # In case the mess_queue file already exist
        # if self.mess_queue.verify_file():
        #     message_pipeline = self.mess_queue.read_model()

        #     # self.mess_data = self.mess_queue.read_model()
        #     # self.mess_dest = self.mess_queue[].tolist() # list of destinations
        #     # self.timestamps = self.registration[5].tolist() # 2D array :: Rows are names / columns are timestamps
        # else:
        #     self.mess_data = [] # 1D array of names recognized (row index for timestamps )
        #     self.mess_dest = [] # 1D array of times when something has occured (column index for timestamps)
        #     self.timestamps = [] # 2D array :: Rows are names / columns are timestamps


    
    def msgput(self, msg:str, dest: list):
        Mqueue = []
        Mqueue = self.mess_queue.read_model()
        #print(Mqueue)
        stampTime = str(datetime.datetime.now())
        dest.insert(0,msg)
        dest.insert(1,stampTime) 
        Mqueue.append(dest) 
        self.slot = dest
        #print(Mqueue)
        self.mess_queue.write_model(Mqueue)
        #print(self.slot)

    def getmsg(self, dest):
        """
        Inquires whether there are messages(msg) in the message queue (Mqueue) for the defines destination (dest)
        Outputs the oldest message first (FiFo)
        """
        Mqueue = self.mess_queue.read_model()

        for item in range(len(Mqueue)):
            if (dest in Mqueue[item]):
                msg = Mqueue[item][0]
                Mqueue.pop(item)
            else:
                msg = None
            self.mess_queue.write_model(Mqueue)
            break
        else:
            msg = None
        return(msg)
    
    def ql(self, dest):
        """
        Retreives the length (QL) of the message queue (Mqueue) for the defines destination (dest)

        """
        Mqueue = self.mess_queue.read_model()
        QL = 0
        for item in range(len(Mqueue)):
            if (dest in Mqueue[item]):
                QL += 1
        return(QL)

"""
--- Usage of Put and Get

a = mess_broker()
#send a message to the queue:
for i in range(100):
    msg = str(i)+ ' harry.'
    a.put(msg,['db','ui'])

#Get a message from the queue
b=a.getmsg('ui')
if b == None:
    print('End of Queue')
else:
    print(b)
"""
#Get a message from the queue
a = mess_broker()
msg = 'start'
while msg != None:
    b=a.getmsg('ui')
    if b == None:
        print('End of Queue')
        break
    else:
        print(b)

# #Get a length of the 'ui' queue
# a = mess_broker()

# print(a.ql('ui'))