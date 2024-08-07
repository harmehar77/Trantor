with open('file.txt', 'r') as in_data:
    in_data = in_data.read()
parts = in_data.split()

p1 = parts[0].split(",")
sum1 = int(p1[1])+int(p1[2])+int(p1[3])

p2 = parts[1].split(",")
sum2 = int(p2[1])+int(p2[2])+int(p2[3])

p3 = parts[2].split(",")
sum3 = int(p3[1])+int(p3[2])+int(p3[3])

output = f"{p1[0]}:{sum1}\n{p2[0]}:{sum2}\n{p3[0]}:{sum3}"

with open('output.txt','w') as out_data :
    out_data.write(output)


'''sum = []
for element in p1,p2,p3:
    sum[i] = int(p[i][1])+int(person1[2])+int(person1[3])

p1 = parts[0]
p1 = p1.split(",")

p2 = parts[1]
p2 = p2.split(",")

p3 = parts[2]
p3 = p3.split(",")

sum = []

for i in range(1,len(parts)+1):
    sum[i] = p[i][i]+p[i][i+1]+p[i][i+2]
    print(sum) '''