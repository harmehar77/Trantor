#decorators
'''def f1(fxn):
    def wrapper():
        print("STARTED")
        fxn()
        print("ENDED")

    return wrapper

@f1
def printer():
    print("HELLO")

f1(printer())'''

'''def decorator_fxn(func):
    def wrapper(*args,**kwargs):
        print("Starting execution.")
        func(*args,**kwargs)
        print("Ending execution.")
    return wrapper

@decorator_fxn
def student_details():
    name = str(input("Enter your name: "))
    marks = []
    for i in range(0,4):
        element = input(f"Enter your marks of subject {i+1}: ")
        marks.append(element)

    print(name,marks)

hello_print = decorator_fxn(student_details())
print(hello_print)'''

'''import time
def timer(func):
    def wrapper(*args,**kwargs):
        print("Start")
        before = time.time()
        func()
        print(f"Finish\nTime taken for execution is {time.time()-before} seconds")
    return wrapper
@timer
def hello():
    print("Hello")

a=timer(hello())
print(a)'''

'''import time
def logger(func):
    def wrapper(*args,**kwargs):
        print("Start")
        with open('log.txt','a') as out:
            out.write(f"\nFunction executed with arguments {args} on {time.asctime()}.")
        val = func(*args,**kwargs)
        print("Finished Execution.")
        print("*"*10)
    return wrapper

@logger
def addition(a,b,c):
    print(a+b+c)

hmm = logger(addition(1,2,3))
print(hmm)'''

#generator
'''def generator(n):
    for i in range(n):
        yield i

for j in generator(100):
    print(j,end=" ")'''

'''import sys
import time

def generator(nums):
    for i in nums:
        yield i*i

nums = [n for n in range(0,1000000)]
t1 = time.time()
for i in range(0,10):
    print((generator(nums)))
t2 = time.time()

#print(square)
#print(sys.getsizeof(square))
print(t2-t1)'''

#single line generator (tuple with iterator inside of it)
#x = (i for i in range(0,10))

#fibonacci series using generators
'''def generator(n):
    t1,t2 = 0,1
    for i in range(0,n):
        t1=t2
        t2 = t1+t2
        yield t2''' 

'''def generator(n):
    t1 = 0 
    t2 = 1
    for i in range(0,n):
        yield t1
        t1,t2 = t2, t1+t2

num = int(input("Enter the term of fibonacci series: "))

#generator(num)
print(list(generator(num)))'''

'''def square(list):
    for i in list:
        yield i*i

l1 = [x for x in range(1,11)]

a = square(l1)
print(a)
for i in a:
    print(i)'''

'''def collatz(n):
    while True:
        if n%2==0:
            n=n//2
        else:
            n = n*3+1
        yield n
        if n ==1:
            break

num =int(input("Enter the number you want the collatz sequence of: "))
a = collatz(num)
print(type(a))
for i in a:
    print(i,end=" ")'''

'''def square(num):
    for n in range(0,num):
        yield n*n
a =[]
a = square(10)
for i in a: 
    print((i))'''

'''def gen(n):
    i = 0
    while i<n:
        i += 1
        yield i

a = gen(100)
for x in a:
    print(x)'''