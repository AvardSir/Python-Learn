
ages = []
i = 0
while i<3:
   age = int(input())
   ages.append(age)
   i+=1

for i in ages:
    if i<16:
        print("Too young!")
        break

else:
    print("Get ready!")   
   