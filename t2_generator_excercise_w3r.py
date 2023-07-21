#Task source: https://www.w3resource.com/python-exercises/generators-yield/index.php

c=0
def new_print():
    global c
    c +=1
    print("\n}" + 30 * "-"+ "[" + str(c) + "]" + 30 * "-" + "{\n")


new_print() #1. Write a Python program that creates a generator function that yields cubes of numbers from 1 to n. Accept n from the user.

def cube_gen(n):
    for i in range(n):
        yield i*i

print([elem for elem in cube_gen(5)])


new_print() #2. Write a Python program to implement a generator that generates random numbers within a given range.

from random import randint

def random_gen(n):
    yield randint(0,n)

print(next(random_gen(9)))


new_print() #3. Write a Python program that creates a generator function that generates all prime numbers between two given numbers.

def prime_range_gen(n,m):
    for i in range(n, m):
        c = 0
        for divider in range(1,i//2):
            if i % divider == 0 : c += 1

        if c == 1: yield i

print([elem for elem in prime_range_gen(12,78)])


new_print() #4. Write a Python program to implement a generator function that generates the Fibonacci sequence.

def fib_gen(n):
    x, y =0, 1
    for _ in range(0,n):
        yield x
        x, y = y, x+y

print([i for i in fib_gen(10)])


new_print() #5. Write a Python program to implement a generator function that generates all permutations of a given list of elements.

def permutations_gen(iter_arg):
    permutations = set()
    for elem in iter_arg:
        permutations.add(elem)
    return permutations

print(permutations_gen([1,2,3]))
#print([i for i in permutations_gen([1,2,3])])