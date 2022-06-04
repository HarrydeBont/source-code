# This routine registers the date and time of faces recognized by the main program.
# By Harry de Bont, April, May 2022

# import os
import datetime
import numpy as np
from objectR_handler import objecter
from termess import terMess

My_msg = terMess()


class register_faceR():
    """
    This class takes care of registration.
    Two functions: registryWrite (save registration to file) and register(save registration to memory)
    """
    def __init__(self):
        self.registry = objecter('FaceR_registry', 'registry' )
        # In case the registry already exist
        if self.registry.verify_file():
            self.registration = self.registry.read_model()
            self.reg_names = self.registration[1].tolist() # 1D array of names recognized (row index for timestamps )
            self.reg_times = self.registration[3].tolist() # 1D array of times when something has occured (column index for timestamps)
            self.timestamps = self.registration[5].tolist() # 2D array :: Rows are names / columns are timestamps
        else:
            self.reg_names = [] # 1D array of names recognized (row index for timestamps )
            self.reg_times = [] # 1D array of times when something has occured (column index for timestamps)
            self.timestamps = [] # 2D array :: Rows are names / columns are timestamps
            self.registration = []
        # convert a numpy array to Python list
        # a = np.array([1, 2]) 
        # a.tolist()


    def registryWrite(self, terminal_message = False):
        """
        This routine stores the face-regsitration in memory and eventually saves the memory to file
        args: True for terminal message
        """
        # convert Python list/arrays to numpy array
        self.reg_names = np.asarray(self.reg_names)
        self.reg_times = np.asarray(self.reg_times)
        self.timestamps = np.asarray(self.timestamps)
        self.registration = ['List of names. ', self.reg_names, 'Timeslots. ', self.reg_times, 'Timestamps. ', self.timestamps]
        self.registry.write_model(self.registration, True)
        if terminal_message:
            msg = 'Registry finshed at: ' +  str(datetime.datetime.now())
            My_msg.tprint(msg)
            msg = 'Number of Timeslots registered: '+ str(len(self.reg_times))
            My_msg.tprint(msg)
            msg = 'Number of faces seen: ' +str(len(self.reg_names))
            My_msg.tprint(msg)
            msg = 'Dimension of the registry: ' + str(self.timestamps.shape)
            My_msg.tprint(msg)
            msg = str(self.registry.read_model())
            My_msg.tprint(msg)



    def register(self, name: str, terminal_message = False):
        """
        This routine registers the face-registration to memory.
        When appending in a loop, it is faster to append to a list than to a Numpy array,
        subsequently convert to a numpy array at the end.
        """
        self.person = name
        self.reg_times.append(str(datetime.datetime.now())) # create a time-index
        if not(self.person in self.reg_names):

            self.reg_names.append(self.person)
            self.timestamps.append([]) # create new person row for timestamps
            
            for i in range(len(self.reg_times)-1):
                self.timestamps[-1].append(False) # new face not recognized @ previous timestamps
        row_index = self.reg_names.index(self.person)
        for i in range(len(self.reg_names)): 
                if (i == row_index): self.timestamps[i].append(True) # this face is recognized @ this timestamp
                if (i != row_index): self.timestamps[i].append(False) # this face is not recognized @ this timestamp
