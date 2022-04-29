from objectR_handler import objecter


directory_hash = objecter('directory hash','hash')
my_hash = directory_hash.read_model()
print(my_hash)