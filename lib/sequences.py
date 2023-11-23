#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    if length == 0:
        print(fib)
    elif length == 1:
        fib.append(0)
        print(fib)
    elif length == 2:
        fib.append(0)
        fib.append(1)
        print(fib)
    else:
        fib.append(0)
        fib.append(1)
        for i in range(3, length+1):
            fib.append(fib[i-3] + fib[i-2])

        print(fib)


