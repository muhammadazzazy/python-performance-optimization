import time

start_time = time.time()

# code here
# cube_numbers = [n**3 for n in range(1,10) if n%2 == 0]
cube_numbers = [n**3 for n in range(1,1000) if n%2 == 0]

end_time = time.time()
print(end_time-start_time)