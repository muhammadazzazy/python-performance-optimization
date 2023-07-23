import time

start_time = time.time()

# code here
from nltk.corpus import words
word_list = words.words()

mystr = ""
for s in word_list:
	mystr += s
	mystr += ","

print(mystr)

end_time = time.time()
print(end_time-start_time)