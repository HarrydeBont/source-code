import datetime

right_now = datetime.datetime.now()
person = "Harry de Bont"
print(right_now)
reg_str = person + " : " + str(right_now) + "\n"
with open ("face registration.txt", 'a') as file:
    file.write(reg_str)
    file.close()
    pass