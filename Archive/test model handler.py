from objectR_handler import objecter

# initiate the objects filename
testthis = objecter('directory model', 'save_my_object')

# Create a test object
a_var = [5]
i = 0
while(i < 3):
    a_var.append(i)
    i += 1
a_var.append("Mary had a little lamb.")

# write the test object onto the physical harddrive
testthis.write_model(a_var)

# read the model form physical harddrive
print(testthis.read_model())
