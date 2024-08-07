#JULY 15 2.30pm

#calculator program
'''def user_input():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = str(input("Chose the operation you want to perform(add,subtract,multiply,divide): ")).lower()

    return num1, num2, operator
def calculator(l1):
    if l1[2]=='add':
        print(f"The result is {l1[0]+l1[1]}")
    elif l1[2]=='subtract':
        print(f"The result is {l1[0]-l1[1]}")
    elif l1[2]=='multiply':
        print(f"The result is {l1[0]*l1[1]}")
    elif l1[2]=='divide':
        print(f"The result is {l1[0]/l1[1]}")
l1 = user_input()
calculator(l1)'''

#occurence of each object in list
'''input = ['b', 'a', 'a','b','a','b','c','b']
input.sort()

d1 = dict()
d1 = {x:input.count(x) for x in input}

for key,value in d1.items():
    print(key," = ",value)'''

#decorator prog
'''def f(func):
    def wrapper(*args):
        print("Start of decorator")
        val = []
        val = func(args) + list(args)
        print("End of decorator")
        return val
    return wrapper
@f
def starting_list(ele):
    l1 = [1,2,3]
    return l1
a = starting_list(8)
print(a)'''

#Rectangle class program
'''class Rectangle:
    def __init__(self,lenght,breadth):
        self.length = lenght
        self.breadth = breadth

    def area(self):
        print(f"Area: {self.length*self.breadth}")
    
    def perimeter(self):
        print(f"Perimeter: {2*(self.length + self.breadth)}")

r = Rectangle(6,4)
r.area()
r.perimeter()'''