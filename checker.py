#code for frequency counter program that takes input from a file 
# and returns the count of specific word in file
'''from sys import argv
script, incoming_file, word = argv

in_file = open(incoming_file,'r+')
in_text = in_file.read()
print(in_text,"\n")

words = in_text.split()
print(words)
count = 0
for i in words:
    if i==word:
        count = count+1
print(count)'''

from sys import argv
script, incoming_file, word = argv

in_file = open(incoming_file,'r+')
in_text = in_file.read()
#format of in_text is string

#split fxn converts string into list with each word an element of the original string
splited = in_text.split()
print(splited)

num = splited.count(word)
print(f"The number of occurences of '{word}' is {num}")

'''
d = {}
for line in in_text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] += 1

        else:
            d[word] = 1

for key in list(d.keys()): 
    print(key, ":", d[key])'''