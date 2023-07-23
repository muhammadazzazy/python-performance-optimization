import time

start_time = time.time()

# code here
from nltk.corpus import words
word_list = words.words()

mystr = ",".join(word_list)
print(mystr)

end_time = time.time()
print(end_time-start_time)