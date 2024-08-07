'''avg = lambda x,y,z: (x+y+z)/3

additon = lambda x,y,z: x+y+z
print(additon(1,2,3)) 

print(avg(12,14,26))'''

'''def fibonacci(num):
    if num <= 0:
        print("Incorrect input!")
    elif num ==1:
        return 0
    elif num ==2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

num = input("Enter the number of terms of fibonacci : ")    
print(fibonacci(13))'''
'''
#fibonacci sequence
t1, t2 = 0,1
num = int(input("Enter the number of terms of fibonacci : "))
print(t1,t1, end=" ")
for i in range(2,num):
    t3 = t1+t2
    t1 = t2
    t2= t3
    print(t3, end=" ")'''

#TWO SUM PROBLEM
'''target = int(input("Enter the target value: "))

num = int(input("Enter the number of elements of num list: "))
l1 = []
print("Enter the list of numbers: ")
for i in range(0,num):
    ele = int(input(f"Enter the {i+1} element of list: "))
    l1.append(ele)

for i in range(0,num):
    for j in range(i+1,num):
        if (i!= j and l1[i] + l1[j]==target):
            print("Indices of elements with sum equal to target value: ",i,j)
            print(f"Element {l1[i]} and {l1[j]} of list have sum equal to {target}.")'''

#list elements less than 10
'''l1=[]
num = int(input("enter number of elements of list: "))
for i in range(num):
    element = int(input(f"Enter {i+1} element of list: "))
    l1.append(element)
l2 = []
for i in range(0,num):
    if l1[i]<10:
        l2.append(l1[i])
print(l2)'''

#prog to print divisors of a number
'''num = int(input("Enter the number you want to find divisors of: "))
div = []
for i in range(1,num+1):
    if num%i==0:
        div.append(i)
print(f"The divisors of {num} are: {div}")'''

#prog for list overlap
'''def list_input():
    list = []
    num = int(input("enter number of elements of list: "))
    for i in range(0,num):
        element = int(input(f"Enter {i+1} element of list: "))
        list.append(element)
    print(list)'''

'''def remove_duplicates(l1):
    l =[]
    for i in range(0,len(l1)):
        if l1[i] not in l:
            l.append(l1[i])
    l.sort()
    l1 = l
    return l1'''
'''
l1 = [1,1,4,6,3,7,8,3,6,9,10]
l1.sort()
l1 = set(l1)
l1 = list(l1)

l2 = [1,8,4,11,24,5,9,31,10]
l2.sort()
l2 = set(l2)
l2 = list(l2)'''

'''l3 = []
if len(l1)>len(l2):
    for i in range(0,len(l1)):
        if l1[i] in l2:
            l3.append(l1[i])
else:
    for i in range(0,len(l2)):
        if l2[i] in l1:
            l3.append(l2[i])
print(l3)'''

'''import random
def generate_list():
    l1 = []
    r = int(input("Enter range of list: "))
    for i in range(0,r):
        element = random.randint(1,20)
        l1.append(element)
    return l1

def common_element(l1,l2):
    l3 = []
    for i in l1:
        if i in l2:
            if i in l3:
                continue
            l3.append(i)
    return l3

a = generate_list()
b = generate_list()
print(a,b)
print(common_element(a,b))'''

'''string = str(input("Enter the string you want to check: "))

if string==string[::-1]:
    print("Given string is a Palindrome")
else:
    print("Given string is NOT a Palindrome")'''

'''a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = [i for i in a if i%2==0]
print(even)'''

#ROCK PAPER SCISSOR GAME
#Rock beats scissors
#Scissors beats paper
#Paper beats rock
'''import random
check = True
options = ["rock","paper","scissor"]
while check:
    choice1 = str(input("Player 1 enter your choice(Rock/Paper/Scissor): ")).lower()
    choice2 = (random.choice(options))
    print(f"Computer's choice: {choice2}")
    if choice1==choice2:
        print("Draw")
    elif choice1=='rock' and choice2=='paper':
        print("Player 2 Wins")
    elif choice1=='rock' and choice2=='scissor':
        print("Player 1 Wins")
    elif choice1=='paper' and choice2=='rock':
        print("Player 1 wins")
    elif choice1=='paper' and choice2=='scissor':
        print("Player 2 wins")
    elif choice1=='scissor' and choice2=='rock':
        print("Player 2 wins")
    elif choice1=='scissor' and choice2=='paper':
        print("Player 1 wins")
    
    in_option = input("Play again(yes/no): ").lower()
    if in_option == 'yes':
        check = True
    else:
        check = False'''

#prog to find frequency of elements of a list
'''original_list = [1,1,2,1,2,4,3,2,5,2,1,3,4,4,5,6,10,23]
original_list.sort()

element_list = set(original_list) 
element_list = list(l2) #list with each element once

print(l1)
d = {x:l1.count(x) for x in l1}
print(d)'''


#prog to reverse a list without fxn or slicing
#l1 = [1,2,3,4,5,6,7]
''' USING TEMP VARIABLE
l = len(l1)
i =0
while i<l:
    temp = l1[i]
    l1[i]=l1[l-1]
    l1[l-1]=temp
    i += 1
    l -= 1
print(l1)'''
''' USING EXTRA LIST
l2 = []
i = len(l1)
while i>0:
    l2.append(i)
    i -= 1
print(l2)'''

#number guessing game
import random
'''num_random = random.randint(1,10)
count = 0
status = True
print("Number guessing game!!!\nGuess a number betweem 1 and 10")
while status:
    guess = int(input(">>>"))
    if guess==num_random:
        print(f"Correct Guess! Number was {num_random}.")
        count +=1 
        print(f"You took {count} tries. ")
        break

    elif guess>num_random:
        print("Guess is too high. Guess AGAIN!")
        count +=1
        continue
        
    elif guess<num_random:
        print("Guess is too low. Guess AGAIN!")
        count +=1
        continue'''
'''def remove_dups(l):
    temp = []
    for i in l:
        if i not in temp:
            temp.append(i)
    temp.sort()
    l = temp
    return l'''

'''a = []
b = []
c = []

def generate_list(list):
    l1 = []
    r = int(input("Enter range of list: "))
    for i in range(0,r):
        element = random.randint(1,10)
        l1.append(element)
    list = l1
    return list

a = generate_list(a)
b = generate_list(b)
print(a,b)
c = [x for x in a if x in b not in c]

for i in a:
    if i in b:
        if i not in c:
            c.append(i)
            
print(c)'''