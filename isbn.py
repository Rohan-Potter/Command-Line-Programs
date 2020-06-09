n=input("Enter the ISBN no. :")
n=list(n)
if  n[9]=='X':
    del n[9]
    n.insert(9,'10')
    print(n)
s=0
j=10
for i in range(0,10):
    c=int(n[i])*j
    s=s+(c)
    j=j-1
print(s)
if s%11==0:
    print("Valid")
else:
    print("Invalid")

