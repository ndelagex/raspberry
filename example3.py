import sys

def str_operation(str, num):
	a = num * str
	print(a)

str_operation(sys.argv[1], int(sys.argv[2]))
