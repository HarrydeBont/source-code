import cv2
    
    
def list_ports():
    """
    Test the ports and returns a tuple with the available ports and the ones that are working.
    """
    non_working_ports = []
    dev_port = 0
    working_ports = []
    available_ports = []
    while len(non_working_ports) < 6: # if there are more than 5 non working ports stop the testing. 
        cam = cv2.VideoCapture(dev_port, cv2.CAP_DSHOW)

        if not cam.isOpened():
            non_working_ports.append(dev_port)
            #print("Port %s is not working." %dev_port)
        else:
            is_reading, img = cam.read()
            # camstr = 'Camera port:' + str(dev_port)
            # cv2.imshow(camstr, img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            w = cam.get(3)
            h = cam.get(4)
            if is_reading:
                #print("Port %s is working and reads images (%s x %s)" %(dev_port,h,w))
                working_ports.append(dev_port)
            else:
                #print("Port %s for camera ( %s x %s) is present but does not reads." %(dev_port,h,w))
                available_ports.append(dev_port)
        dev_port +=1
    # return available_ports,working_ports,non_working_ports
    return working_ports

#print(list_ports())