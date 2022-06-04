# Display terminal messages in therequired output form
# Either no mmessages / in the terminal window / using the UI (to be build as of writing this coding)
# Author: Harry de Bont
# May 2022
from objectR_handler import objecter
from messageBroker import mess_broker

class terMess:
    """
    mode == 1 ::  print(msg) # Use plain terminal message without UI
    mode == 2 ::  print(".") # Show activity, no messages
    """
    def __init__(self):
        # Read show_m from config file
        self.faceR_config = objecter('config','FaceR_config')
        config_test = self.faceR_config.read_model()
        self.show_m = config_test[1]
        self.MessQueue = mess_broker()

    def tprint(self, msg):
        self.msg = msg
        config_test = self.faceR_config.read_model()
        self.show_m = config_test[1]
        if self.show_m == 1: 
            print(self.msg) # Switch terminal messages ON
            self.MessQueue.msgput(msg, ['ui'])
        elif self.show_m == 2: print(".") # Show activity, no messages
        else: return  
        