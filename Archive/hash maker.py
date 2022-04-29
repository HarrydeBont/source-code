# import OS module
import os

# Get the list of all files and directories
path = "C://Users//HWdeB//Documents//Python//source facerecogn//source code//images"
dir_list = os.listdir(path)

print("The integer hash value is : " + str(hash(str(dir_list))))
print("Files and directories in '", path, "' :")
# prints all files
print(str(dir_list))
