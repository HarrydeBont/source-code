# test usage of Python array for storage of names and timestamps when faces are recognized
# 1) Todo test numpy array Done
# https://stackoverflow.com/questions/22392497/how-to-add-a-new-row-to-an-empty-numpy-array

import numpy as np
import datetime
import random

# Numpy array
reg_names = [] # 1D array of names recognized (row index for timestamps )
reg_times = [] # 1D array of times when something has occured (column index for timestamps)
timestamps = [] # 2D array :: Rows are names / columns are timestamps

from time import sleep

for i in range(50): # simulate face recognized 5x times
    sleep(0.01)
    reg_times.append(str(datetime.datetime.now())) # create a time-index
    persons = ['Harry de Bont', 'Katelijn', 'Wim'] # name is person?
    for j in range(len(persons)):
        #print(persons[j])
        if not(persons[j] in reg_names):
            reg_names.append(persons[j])
            timestamps.append([]) # create new row for timestamps
        # Store time stamps as boolean
        timestamps[j].append(random.choice([True,False])) # simulate face recognized

print('Python lists/arrays: ')
print(reg_names)
print(reg_times)
print(timestamps)

reg_names = np.asarray(reg_names)
reg_times = np.asarray(reg_times)
timestamps = np.asarray(timestamps)

# when appending in a loop, it would be much faster to append to a list,
# then convert to a numpy array at the end, since we would really not be using numpy functionality as intended during the loop

print('Numpy arrays: ')
print(reg_names)
print(reg_times)
print(timestamps)


# # Show content of timestamps (Numpy_array)
for j in range(len(reg_names)):
    for i in range(len(reg_times)):
        print(reg_names[j], reg_times[i],timestamps[j][i])