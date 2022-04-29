# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import time

def sleep_time(num):
    """
    function sleep timer
    """
    print("sleep: {} seconds".format(num))
    time.sleep(num)
 

def print_square(num):
	"""
	function to print square of given num
	"""
	print("Square: {}".format(num * num))

if __name__ == "__main__":
	# creating thread
	t1 = threading.Thread(target=print_square, args=(10,))
	t2 = threading.Thread(target=sleep_time, args=(2,))

	# starting thread 1
	t1.start()
	# starting thread 2
	t2.start()

	# wait until thread 1 is completely executed
	t1.join()
	# wait until thread 2 is completely executed
	t2.join()

	# both threads completely executed
	print("Done!")
