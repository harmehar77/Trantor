''''
#LISTS
list = [23, 25, 9 ,70 ,47]
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.insert(3,45)
print(list)
l2 = list.copy()
print(f"This is copied list: {l2}")'''

#Lists questions
#Q1
'''
movies = []
for i in range(0,3):
    x = input(f"Enter the name of {i+1} favourite movie: ")
    movies.append(x)
print(f"Your favourite movies are: {movies}")'''

#Q2 check if a list contains a palindrome of elements 
'''
list1 = []
n = int(input("Enter the number of elements of the list: "))

for i in range(0,n):
    x = input(f"Enter the {i+1} element of list: ")
    list1.append(x)
print(list1)

mid = (len(list1)-1)//2
start = 0
last = len(list1)-1
flag = 0

for i in range(0,mid):
    if(list1[start]==list1[last]):
        start += 1
        last -= 1
    else:
        flag = 1

if(flag==0):
    print("List has palindrome elements.")
else:
    print("List does not have palindrome elements.")'''

#TUPLE QUESTIONSW
#Q1
tuple1 = ('A','C','B','B','C','B','C','D','D','C','A','A','E','F','A','A')
print(f"The number of students with grade 'A' is: {tuple1.count('A')}")
a = len(tuple1)
list = []
for i in range(0,a):
    x = tuple1[i]
    list.append(x)
list.sort()
print(list)
'''
grade_list = ['A','C','B','B','C','B','C','D','D','C','A','A','E','F','A','A']
grade_list.sort()
print(grade_list)
'''