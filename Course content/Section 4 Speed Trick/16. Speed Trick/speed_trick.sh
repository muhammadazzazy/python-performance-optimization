#!/bin/bash
cat test.py
python3 test.py
vim test.c
clear
cat test.c
gcc -fPIC -shared -o libtest.so test.c
vim test2.py
python3 test2.py
vim test2.py
vim test.c
gcc -fPIC -shared -o libtest.so test.c
vim test.py
python3 test.py
gcc -fPIC -shared -o libtest.so test.c
python3 test2.py
vim test2.py
clear
pypy3 test.py
python3 test.py
pypy3 test2.py

python3 test.py
python3 test2.py
