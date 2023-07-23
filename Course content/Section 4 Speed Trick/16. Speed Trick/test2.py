import time

start_time = time.time()

# code here
import ctypes
fun = ctypes.CDLL("./libtest.so")
fun.f()

end_time = time.time()
print(end_time-start_time)