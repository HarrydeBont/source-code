from directory_structure import dir_struc

import cv2
import os
import shutil
# Handle actions for unknown faces:
# 0) Store unknown faces with double digits in filename V Done 13-0602022 (unknown_faces.py)
# 1) show next unknown face - set index V Done 13-06-2022
# 2) show prev unknown face - set index V Done 13-06-2022
# 3) Remove unknown face - set index V Done 13-06-2022
# 4) Rename unknown face - re-index list of unknown faces set pointer to renamed file V Done 13-06-2022
# 5) Move unknown face - re-index and move renamed file to images directory for training (check validity filename) V Done 13-06-2022
# 6) Check edge case empty diorectory of unknown faces V Done 15-06-2022 (exception Indexerror)

# 0) Leading zero's in the unknown faces filename is useful for the sorting/indexing (unknown_faces.py)
# msg2 = str(number).zfill(2)
# print(msg2)
#1) show next unknown face - set index
# list the files in the unknown_faces directory

# initialise
ds = dir_struc()

global uindex,  Unknown_faces, amount_ufaces
uindex = 0
Unknown_path = ds.unknown_img_path()
print(Unknown_path)
image_path = ds.img_path()

Unknown_faces = ds.list_ufaces()
# train_images = ds.
amount_ufaces = len(Unknown_faces)


def show():
    global uindex
    try:
        current_file = Unknown_faces[uindex]
        imgpathfile = Unknown_path + "//" + current_file
        window_name = 'Showing: ' + imgpathfile
        img = cv2.imread(imgpathfile)
        cv2.imshow(window_name,img)
        cv2.waitKey(0)
        # cv2.destroyAllWindows()
    except IndexError:
        print('Unknown faces directory empty')

def next():
    global uindex
    uindex = min(amount_ufaces - 1, uindex + 1)
    try:
        current_file = Unknown_faces[uindex]
        imgpathfile = Unknown_path + "//" + current_file
        window_name = 'Showing: ' + imgpathfile
        img = cv2.imread(imgpathfile)
        cv2.imshow(window_name,img)
        cv2.waitKey(0)
        # cv2.destroyAllWindows()
    except IndexError:
        print('Unknown faces directory empty')


def prev():
    global uindex
    uindex = max(0, uindex - 1)
    try:
        current_file = Unknown_faces[uindex]
        imgpathfile = Unknown_path + "//" + current_file
        window_name = 'Showing: ' + imgpathfile
        img = cv2.imread(imgpathfile)
        cv2.imshow(window_name,img)
        cv2.waitKey(0)
        # cv2.destroyAllWindows()
    except IndexError: 
        print('Unknown faces directory empty')

def rem():
    global uindex, Unknown_faces
    uindex = min(uindex, len(Unknown_faces)-1)
    try:
        current_file = Unknown_faces[uindex]
        imgpathfile = Unknown_path + "//" + current_file
        window_name = "Delete? :" + imgpathfile + ' [Y] to delete'
        img = cv2.imread(imgpathfile)
        cv2.imshow(window_name,img)
        key = cv2.waitKey(0) & 0xFF
        # key is 'y' or 'Y'
        if (key == 121) or (key == 89):
            try: 
                os.remove(imgpathfile)
                Unknown_faces = ds.list_ufaces()
            except: pass
        else:
            print('Image not deleted..')
    except:
        print('Image not found..')

def rename(name):
    global uindex, Unknown_faces
    uindex = min(uindex, len(Unknown_faces)-1)
    try:
        current_file = Unknown_faces[uindex]
        old_imgpathfile = Unknown_path + "//" + current_file
        new_imgpathfile = Unknown_path + "//" + name + ".jpg"
        window_name = "Rename? :" + old_imgpathfile + ' [Y] to rename'
        img = cv2.imread(old_imgpathfile)
        cv2.imshow(window_name,img)
        key = cv2.waitKey(0) & 0xFF
        # key is 'y' or 'Y'
        if (key == 121) or (key == 89):
            try: 
                os.rename(old_imgpathfile, new_imgpathfile )
                find(name) # re-index so still point to the renamed image
            except: 
                print('Something went wrong..')
        else:
            print('Image not renamed..')
    except:
        print('Image not found..')

def copy():
    global uindex, Unknown_faces
    uindex = min(uindex, len(Unknown_faces)-1)
    try:
        current_file = Unknown_faces[uindex]
        imgpathfile = Unknown_path + "//" + current_file
        dest_imgpathfile = Unknown_path + current_file
        window_name = "Copy ? :" + imgpathfile + ' [Y] to copy'
        img = cv2.imread(imgpathfile)
        cv2.imshow(window_name,img)
        key = cv2.waitKey(0) & 0xFF
        # key is 'y' or 'Y'
        if (key == 121) or (key == 89):
            try: 
                shutil.copy(imgpathfile, image_path)
                #Unknown_faces = ds.list_ufaces()
            except: 
                print('Something went wrong..')
        else:
            print('Image not copied..')
    except:
        print('Image not found..')

def find(name):
    global uindex, Unknown_faces
    find_img = name + ".jpg"
    Unknown_faces = ds.list_ufaces()
    uindex = Unknown_faces.index(find_img)
    return(uindex)

# show()
# # next()
# # next()
# # next()

# rename('Harry de Bont_007')
# copy()
cv2.destroyAllWindows()



