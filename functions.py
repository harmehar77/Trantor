'''def printer(*argv):
    argv1, argv2 = argv
    print(f"\nArgument 1 is: {argv1}.\nArgument 2 is: {argv2}.")

printer("harmehar", "coder")

def cars(type_of_car, model, colour):
    print(f"You have a {type_of_car} car.")
    print(f"Your car model is {model}.")
    print(f"Colour of your car is {colour}.")

type_input = input("Enter the type of car you have: ")
model_input = input("Enter the model of your car: ")
colour_input = input("Enter the colour of your car: ")

cars(type_input,model_input,colour_input)'''

'''foods = ["banana", "apple", "roti", "sabzi","cake","idli","rice"]

def printer(list):
    for item in list:
        print(item,end=" ")

printer(foods)'''

def factorial(num):
    factorial = 1
    for i in range(1,num+1):
            factorial *= i
            print(factorial)
    
factorial(4)