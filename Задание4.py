a = int(input(""))
s = ' '
q=a
i = 0
u = a
while q!=1:
    print(s*i+ a*"*")
    a-=2
    q-=1
    i+=1
while u!=1:
    print(s*i+a*"*")
    a+=2
    i-=1
    u-=1