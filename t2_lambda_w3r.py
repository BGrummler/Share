#lambda tasks from https://www.w3resource.com/python-exercises/lambda/index.php
from functools import reduce
from random import randint
c=0
def new_print():
    global c
    c +=1
    print("\n}" + 30 * "-"+ "[" + str(c) + "]" + 30 * "-" + "{\n")


new_print() #1
print((lambda x : x +15)(10))
print((lambda x,y : x + y)(40,8))
new_print() #2
print((lambda x: x + randint(0,100))(15))
print("\n#3\n")
l_o_t = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(sorted(l_o_t, key=lambda x: x[1]))
new_print() #3
l_o_d = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(sorted(l_o_d, key=lambda x : x["color"]))
new_print() #4
print(list(filter((lambda x : x % 2 == 0),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
print(list(filter((lambda x : x % 2 == 1),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
new_print() #5
print(list(map(lambda x:x*x,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
print(list(map(lambda x:x*x*x,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
new_print() #6
print((lambda x,y: x[0] == y)("Banane","B"))
new_print() #7
print("".join(map((lambda x:x if x not in " -" else "\n"),"2020-01-15 09:03:32.744178")))
new_print() #8
print((lambda x: type(x) == int)(1))
print((lambda x: type(x) == int)("A"))
print((lambda x: type(x) == int)(False))
print((lambda x: type(x) == int)(100))
print((lambda x: type(x) == int)(None))
print((lambda x: type(x) == int)(1.1))
new_print() #9
print((lambda c: reduce(lambda x, _: x+[x[-1]+x[-2]],range(c-2), [0, 1]))(10)) #TODO 
def gen(c):
    x, y =0, 1
    for _ in range(0,c):
        yield x
        x, y = y, x+y
print([i for i in gen(10)])
new_print() #10
print((lambda x,y : [x[i] for i in range(len(x)) if x[i] in y])([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]))