
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
a=input()

for i in contacts:
    if i[0]==a:
        print(i[0]+' is '+str(i[1]))
        break
else:
    print("Not Found")