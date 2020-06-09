from random import randint
#To generate random word
s=[]
q=[]
l=int(input("Enter the length of word :"))
for i in range(1,l+1):
    g=randint(97,122)
    s.append(chr(g))
    q.append("*")
#print(s) To Check you'r word
print("You'r word is ready :",end="")
print("".join(q))
#User input
h=int(input("Enter How many chances you want :"))
if h>l:
    for j in range(0,h):
        w=input("Enter the letter :")
        if w in s:
            print("You Guess Right!!")
            q.pop(s.index(w))
            q.insert(s.index(w),w)
            print("".join(q))
            if ("".join(q))==("".join(s)):
                print("Yeah!! you Won!!")
                break         
        else:
            print("Wrong Letter!!")
else:
    print("ERROR!! Chances must be greater than word length!!")