#DAY 1 03/07/2024

'''str_var = 'Hi i am Harmehar'
print(str_var)
print(type(str_var))

print(str_var[0])
print(str_var[-5])

String1 = "GeeksForGeeks"
print("Last character of String is: ", String1[-3])

my_name = 'Harmehar Singh'
my_age = 20
status = 'Student'

a = f"Hello my name is {my_name}."
b = f"My age is {my_age}."

print(a)
print(b)

types_of_cars = 100

x = f"There are {types_of_cars} types of cars in this world."
y = f"There aren't {types_of_cars} types of cars in this world."

print(f"Someone said that: {x}")
print(f"Someone else said that: {y}")

joke_evaluation="The car joke is so funny isn't it? {}"
funny=False
print(joke_evaluation.format(funny))
 
formatter="{} {} {} {}"
print(formatter.format(10,20,30,40))
print(formatter.format(True, False,True,True))

print("""Hello
      what is up?
      this is a multi line print
""")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
op = input("Enter the operator(+,-,/,*,%): ")

if op=="+":
    print("Sum of given numbers: ", x+y)

elif op=="-":
    print("Difference of given numbers: ", x-y)

elif op=="/":
    print("Division of given numbers: ", x/y)

elif op=="*":
    print("Product of given numbers: ", x*y)

elif op=="%":
    print("Modulus of given numbers: ", x%y)

x = list(map(int, input("Enter the table of five: ").split()))
print(x)

from sys import argv
script, first, second, third = argv

print("This script is called: ", script)
print("First variable: ", first)
print("Second variable: ", second)
print("Third variable: ", third)'''

#run in terminal with command line arguments
from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""Ok {user_name} 
      you said you {likes} like me.
      Remember that i am {script}
      I see that you have a {computer}
      Good to know that you live in {lives}.""")