import time

start_time = time.time() 

# code here
def f():
    total = 0
    for i in range(0,5000):
        for j in range(0,5000):
            z = (i*j)
            total += z
    print(total)

f()
end_time = time.time()
print(end_time-start_time)

