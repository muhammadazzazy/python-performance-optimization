# Introduction
You can call functions written in C from Python. If you have never
programmed with the C programming language before, this can
be a bit confusing.

Unlike Python, C is converted directly into machine code. It
doesn't use an interpreter. That's why executing C code directly
can be faster.

The way this works is by converting C code into a system library
and then loading the library in Python and calling the function.