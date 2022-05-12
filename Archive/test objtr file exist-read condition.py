from objectR_handler import objecter
import directory_structure

registry = objecter('FaceR_registry', 'registry')
registry.read_model(True)

print(registry.verify_registry())

dir_test = directory_structure.dir_struc()
dir_test.count_faces()

