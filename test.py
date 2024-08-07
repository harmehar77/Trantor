'''list1 = [1,2,3,4,5]
list2 = list1 #by directly assigning list1 to list2, the memory space of l1 is shared to l2  
list2[4] = 6 
print(list2)
print(list1)'''
'''
#
l = [1,2,3]
l1 = l[:] #sliciing, by doing slicing copy of a list we create a new object of the list
l1[0]=5
print(l1)
print(l)'''
    
'''l1 = [1,2,1,4,5,2]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)'''

'''def performOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    for i in range(len(A)):
        B[i] = A[i]
        B[i + len(A)] = A[(len(A) - i) % len(A)]
    return B
A = [5,10,2,1]
performOps(A)
print(performOps(A))'''
'''Lets say performOps was called with A : [5, 10, 2, 1].
What would be the output of the following call :
( NOTE : The output shoudl be written in the below provided text field , 
there should not be any ‘,’ between the numbers . For example: 1 2 3 4 )
B = performOps(A)
for i in xrange(len(B)):
    print B[i],'''

#prog for if duplicates present in list print true
'''l1=[1,2,3,4,5,6]
s1=set(l1)
if len(l1)!=len(s1):
    print(True)
else:
    print(False)
'''
'''for i in range(len(l1)):
    for j in range(0,i):
        if l1[i]==l1[j]:
            print(True)
        else:
            print(False)
            continue'''


'''in_file = open('file.txt', 'r')
in_data = in_file.read()
parts = in_data.split()

person1 = parts[0]
person1 = person1.split(",")
sum1 = int(person1[1])+int(person1[2])+int(person1[3])

person2 = parts[1]
person2 = person2.split(",")
sum2 = int(person2[1])+int(person2[2])+int(person2[3])

person3 = parts[2]
person3 = person3.split(",")
sum3 = int(person3[1])+int(person3[2])+int(person3[3])

output = f"{person1[0]}:{sum1}\n{person2[0]}:{sum2}\n{person3[0]}:{sum3}"

with open('output.txt','w') as out_data :
    out_data.write(output)'''
