import time

start_time = time.time()

# code here
movies = ["Superman","Spiderman","Hulk","Xmen","Batman"]
m = []
for i in range(0,len(movies)):
	m.append( movies[i].upper())
print(m)

end_time = time.time()
print(end_time-start_time)