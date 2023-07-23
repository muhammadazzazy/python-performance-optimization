import time

def long_time():
	x = 0
	for j in range(0,1000000):
		for i in range(0,1000000):
			# x = x + 1
			x = x + i
			x = x + j


start = time.time()
# print("hello world")
# x = 0
# for i in range(0,1000000):
# 	x = x + 1
long_time()
end = time.time()
print(end-start)