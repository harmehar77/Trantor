'''file1 = open('essay.txt','r')
file2 = open('paragraph.txt','r')

with open('paragraph.txt') as file:
    data = file.read()
print(data)'''

'''file1 = open('essay.txt','r')
print(file1.readlines(4))


file3 = open("written.txt", "w+")
file3.write("This text is written into the file by python.\n")
file3.write("This will be line 2 in the file.\n")

L = ["I am in Chandigarh.\n", "I am at IT Park.\n", "I am inside Trantor INC.\n"]
file3.writelines(L) 
file3.close()

file3 = open("written.txt","r+")
print(file3.read())

with open("written.txt") as file:
    f.write

from sys import argv 
script, filename =  argv

text = open(filename)

print(f"This is your filename {filename}")
print(text.read())

filename2 = input("Enter filename again: ")

text2 = open(filename2)
print(text2.read())

filename = input("Enter the filename you want to open: ")
filetext = open(f"filename", "r+")

print(filetext.read())

print("Enter the text you want to add to the file\n")
additions = input(">")

filetext.write(additions)
filetext.close()

filetext.open()
print(filetext.read())

'''
#prog to copy data from one file to another
from sys import argv
from os.path import exists
script, from_file, to_file = argv

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exists? {exists(to_file)}")
print(f"Ready to copy data of {from_file} to the {to_file}. Press enter to copy.")

input()

out_file = open(to_file,"w")
out_file.write(indata)

print("Copying is done.")
out_file.close()
in_file.close()

text=open(to_file)
print(text.read())