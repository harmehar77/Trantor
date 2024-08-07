'''string = "Hi i am Harmehar"
for i in range(0,11):
    print(i)
list = ["Harmehar", "Josh", "Tripat", "Karan", "Chiru"]
for count, element in enumerate(list):
    print(count,element)

for i in range(1,5):
    for j in range(6,10):
        print(i,j) '''

str = "abcdefgh"

for i in str:
    if i=="c" or i=="e":
        print(f"Breaking element is {i}")
        break 
    else:
        print(i)

