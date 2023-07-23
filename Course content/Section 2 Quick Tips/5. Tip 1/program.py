import time

def f():
	total = 0
	for i in range(1,5000):
		for j in range(1,5000):
			total += i
			total += j

start_time = time.time()
f()
end_time = time.time()
print(end_time-start_time)