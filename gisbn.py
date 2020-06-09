from random import randint
n=[]
s=0
j=10
while True:
    for i in range(0,10):
        a=randint(0,9)
        n.append(a)
    for i in range(0,10):
        c=int(n[i])*j
        s=s+(c)
        j=j-1
    if s%11==0:
        print(s)
        print(n)
        break
    else:
        s=0
        n.clear()
        j=10



