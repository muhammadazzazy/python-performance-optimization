import time

start_time = time.time()

total = 0

for i in range(1, 10000):
	for j in range(1, 10000):
		total += i
		total += j

end_time = time.time()

print(end_time - start_time)