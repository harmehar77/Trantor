#prog for prime number with random number
'''def prime(num):
    #num = int(input("Enter the number to check for prime: "))
    divisors = []
    for i in range(2,num+1):
        if num%i==0:
            divisors.append(i)
        
    if len(divisors)>1:
        print(f"{num} is not prime")
    else:
        print(f"{num} is prime")
def generate_random():
    import random
    #num = []
    x = int(input("Range to generate random number (starting from 1): "))
    n = random.randint(1,x)
    print(f"Random number generated is {n}")
    return n
a = generate_random()
prime(a)'''

#WAP to return the element of list which does not have a duplicate
'''l1 = [1,1,2,3,3,2,2,4,4,2,4,3,3,5]
l1.sort()

d1 = dict()
d1 = {x :l1.count(x) for x in l1}
print(d1)

for key, value in d1.items():
    if value==1:
        print("the element without any duplicates is: ",key)'''

#fibonacci sequence
'''t1,t2 = 0,1
n = int(input("Enter till which term to generate the fibonacci series: "))
print(t1,t2,end=" ")
for i in range(0,n):
    t3 = t1+t2
    t1 = t2
    t2 = t3
    print(t3,end=" ")'''

#staring and ending elements of a list
'''import random
n = int(input("enter no. of elements of a list: "))
l1 = []
for i in range(0,n):
    element = random.randint(1,100)
    l1.append(element)
print(l1)
l2 = []
l2.append(l1[0])
l2.append(l1[-1])
print(l2)'''

#prog to reverse a string
'''string = str(input("Enter a string: "))
splitted = string.split()
reverse_string = " ".join(splitted[::-1])
print(reverse_string)'''

#prog to check whether or the given number is inside a random list
'''import random
n = int(input("Enter the size of list: "))
l1 = []
for i in range(0,n):
    element = random.randint(1,10)
    l1.append(element)
num = int(input("Enter the number you want to check in list: "))
flag = 0
if num in l1:
    flag +=1
if flag ==1:
    print(True)
else:
    print(False)
print(l1)'''

#OBJECT ORIENTED PROGRAMMING
'''class Book:
    def __init__(self,title,author,year,price):
        self.title = title
        self.author = author
        self.year = year 
        self.price = price

    def __str__(self):
        return f"{self.title},{self.author}"

b1 = Book('Python','Harmehar',1,1)
print(b1)

b2 = Book('Maths','Pythagoras',2,2)
print(b2)'''

'''class car():
    def __init__(self,model,maker,bhp,year):
        self.maker = maker
        self.model = model
        self.bhp = bhp
        self.year = year

    def output(self):
        print(f"{self.model} is made by {self.maker}, in the year {self.year}.It has {self.bhp} horsepower.")
        
class BMW(car):
    def __init__(self, model, maker, bhp, year,cost):
        super().__init__(model, maker, bhp, year)
        self.cost = cost
    
    def output(self):
        return super().output()
    
    def buy(self):
        print(f"{self.model} costs {self.cost}")

m6 = BMW('BMW M8','BMW',500,2024,140000)
m6.output()
m6.buy()
obj1 = car('Baleno','Maruti Suzuki',100,2024)
obj1.output()'''

#print("\033[1m" + "THIS IS BOLD" + "\033[0m")

'''class Student:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display(self):
        print(f"Student Name:\t\t{self.name}\nSubject 1 Marks:\t{self.m1}\nSubject 2 Marks:\t{self.m2}\nSubject 3 Marks:\t{self.m3}")

s1 = Student('Harmehar',89,89,91)
s1.display()'''

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

from sys import argv 
script, file1, file2 = argv
with open (file1,'r') as in_text:
    text = in_text.read()
main_list = text.split()

def marks_sum(p):
    marks =  main_list[p].split(",")
    name = marks[0]
    sum_marks = int(marks[1])+int(marks[2])+int(marks[3])
    average_marks = sum_marks//2
    return name, sum_marks, average_marks

p1=list(marks_sum(0))
p2=list(marks_sum(1))
p3=list(marks_sum(2))

with open(file2,'w') as out_text:
    out_text.write(p1[0]+" Sum:"+str(p1[1])+" Average:"+str(p1[2])+
                   "\n"+p2[0]+" Sum:"+str(p2[1])+" Average:"+str(p2[2])+
                   "\n"+p3[0]+" Sum:"+str(p3[1])+" Average:"+str(p3[2]))