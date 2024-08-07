'''#maximum of two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

def maximum(num1,num2): 
    if (num1>num2):
        print(f"Greater number is {num1}")
    else:
        print(f"Greater number is {num2}")

def minimum(num1,num2):
    if (num1<num2):
        print(f"Smaller number is {num1}")
    else:
        print(f"Smaller number is {num2}")

maximum(num1,num2)
minimum(num1,num2)


#methods to find length of list
list1 = [1,23,3,5,2,27]

print(f"Length of list is {len(list1)}")

#naive method of finding length of string using counter
print(f"The test list is: {list1}")
counter = 0
for i in list1:
    counter += 1
print("The length of test list is: ",counter)

#prog to swap two elements of a list
def swap(list,pos1,pos2):
    temp = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = temp
    print(list)

list1 = list()
n = int(input("Enter the length of the list: "))
for i in range(0,n):
    element = int(input(f"Enter the {i} element of list: "))
    list1.append(element)

pos1 = int(input("Enter the position of element 1 to be swapped: "))
pos2 = int(input("Enter the position of element 2 to be swapped: "))

swap(list1,pos1,pos2)

#Palindrome word program
str1 = input("Enter the word to check for Palindrome: ")
mid = len(str1)-1

start=0
last=len(str1)-1
flag=0

while(start<=last):
    if(str1[start]==str1[last]):
        start += 1
        last -=1

    else:
        flag = 1
        break

if(flag==1):
    print("Given word is not a palindrome.")

else:
    print("Given word is a palindrome.")

str1 = input("Enter the word to check for palindrome: ")
str2 = str1[::-1]

print(f"{str1} \t {str2}")
if(str1==str2):
    print("is a palindrome")
else:
    print("isn't a palindrome")

str = input("Enter the string you want to be reversed: ")
s = str.split()[::-1]
l =[]
for i in s:
    l.append(i)

print(" ".join(l))


str = input("Enter a string: ")
count = 0
for i in str:
    count += 1

print(count)
print(len(str))'''

str = input("Enter a string: ")

a = str.split(" ")

for i in a:
    if len(i)%2==0:
        print(i)
