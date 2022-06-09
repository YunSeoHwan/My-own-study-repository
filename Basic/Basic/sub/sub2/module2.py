import sys
import inspect
# from ..sub1 import module1

# module2.py
def mod2_test1():
	print ("Module2 -> Test1")
	print("Path : ", inspect.getfile(inspect.currentframe()))

def mod2_test2():
	print ("Module2 -> Test2")
	print("Path : ", inspect.getfile(inspect.currentframe()))