import random
a = []
for i in range(4):
    a.append(random.randint(0,100))
print(a)
b=[]
for elem in a:
    k = elem*2
    a+=b[k]
print(a)
