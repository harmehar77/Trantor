'''in_year = int(input("Enter year: "))
#for i in range(2000,2100):
if in_year%100==0 and in_year%4==0:
        print(f"{in_year} is a leap year")
else:
        print("NO")'''

#prog to find frequency of a word in a file
'''from sys import argv
script, file1 = argv
with open(file1,'r') as in_data:
    in_text = in_data.read().lower()
#print(in_text)
lst = in_text.split()
count = 0
search_word = str(input("Enter the word you want to count in the file: "))
for word in lst:
    if word==search_word:
        count += 1
print(f"'{search_word}' is {count} times in the file.")'''

'''from sys import argv
script, file1, file2 = argv

with open(file1,'r') as in_data:
    in_text = in_data.read()

with open(file2,'w') as out_text:
    out_text.write(in_text)'''

'''import os, string
if not os.path.exists("letters"):
    os.mkdir("letters")

for letter in string.ascii_lowercase:
        with open(letter + ".txt",'w') as file:
            file.write(letter)'''

'''import string
with open('alphabet.txt','a') as out_file:
    alphabet = string.ascii_uppercase
    letters = [alphabet[i] + "\n" for i in range(0,len(alphabet))]
    for i in range(0,len(letters)):
        out_file.write(letters[i])'''

'''x= (i for i in range(0,10))
for i in x:
    print(i)'''

# class Person(object):
#     def __init__(self,name,dob):
#         self.name = name
#         self.dob = dob

#     def printer(self):
#         print(f"Hello {self.name}, ")
sum = 0
for i in range(1,9996):
    sum += i
print(sum)