import time

start_time = time.time()

# code here
x = "hello world this is an example text."
i = 0
while x[i] != '.':
	i = i + 1
print(i)

end_time = time.time()
print(end_time-start_time)