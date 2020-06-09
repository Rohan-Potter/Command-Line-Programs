from random import randint
a= randint(1,10)
def winning(n,z):
    if n==a:
        return ("Yeah you won!! NO. of chances you have taken :"+ str(z))
    elif n>a:
        return ("You'r no is greater than the winning no")
    else:
        return ("You'r no. is less than the winning no ")
for i in range(1,20):
    b=int(input("enter the no :"))
    print(winning(b,i))
    if a==b:
        break