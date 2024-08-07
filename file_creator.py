import os, string
if not os.path.exists("letters"):
    os.mkdir("letters")

for letter in string.ascii_lowercase:
        with open(letter + ".txt",'w') as file:
            file.write(letter)