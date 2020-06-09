from random import randint
A=1
B=1
player1=input("Enter your name Player 1: ")
player2=input("Enter your name Player 2: ")
#Game Board

def game():
    global A
    e=input(f"{player1} Press Enter to roll a die")
    d=randint(1,6)
    print(f"Die :{d}")
    A=A+d
    if A<=100:
        print(f'your position {A}')
    #Bitten by Snake
    if A==17 or A==44 or A==75 or A==97:
        A = A-5
        print(f"Bitten By snake and moved to :{A}")
    elif A==15 or A==46 or A==91:
        A= A-10
        print(f"Bitten By snake and moved to :{A}")
    elif A==13 or A==42:
        A =A-7
        print(f"Bitten By snake and moved to :{A}")
    elif A==73 or A== 77 or A==94:
        A=A-5
        print(f"Bitten By snake and moved to :{A}")
    elif A==99:
        A=1
        print(f"Bitten By snake and moved to :{A}")
    #Ladder
    if A==14 or A==76:
        A =A+7
        print(f"You got ladder and moved to :{A}")
    elif A==16 or A==78 or A==43:
        A= A+6
        print(f"You got ladder and moved to :{A}")
    elif A==18 or A==47:
        A= A+4
        print(f"You got ladder and moved to :{A}")
    elif A==45 or A==74:
            print(f"You got ladder and moved to :{A}")
    elif A==40:
        A=80
        print(f"You got ladder and moved to :{A}")

def game2():
    global B
    e=input(f"{player2} Press Enter to roll a die")
    d=randint(1,6)
    print(f"Die :{d}")
    B=B+d
    if B<=100:
        print(f'your position {B}')
    #Bitten by Snake
    if B==17 or B==44 or B==75 or B==97:
        B = B-5
        print(f"Bitten By snake and moved to :{B}")
    elif B==15 or B==46 or B==91:
        B= B-10
        print(f"Bitten By snake and moved to :{B}")
    elif B==13 or B==42:
        B =B-7
        print(f"Bitten By snake and moved to :{B}")
    elif B==73 or B== 77 or B==94:
        B=B-5
        print(f"Bitten By snake and moved to :{B}")
    elif B==99:
        B=1
        print(f"Bitten By snake and moved to :{B}")
    #Ladder
    if B==14 or B==76:
        B =B+7
        print(f"You got ladder and moved to :{B}")
    elif B==16 or B==78 or B==43:
        B= B+6
        print(f"You got ladder and moved to :{B}")
    elif B==18 or B==47:
        B= B+4
        print(f"You got ladder and moved to :{B}")
    elif B==45 or B==74:
            print(f"You got ladder and moved to :{B}")
    elif B==40:
        B=80
        print(f"You got ladder and moved to :{B}")

#To roll a die
while True:
    e=input(f"{player1} Press Enter to roll a die!")
    a=randint(1,6)
    print(a)
    if a==1:
        print(f"{player1} You In!")
        while True:
            e=input(f"{player2} Press Enter to roll a die!")
            b=randint(1,6)
            print(b)
            if b==1:
                print(f"{player2} You In!")
                game()
                break
            else:
                game()
        if a==1 and b==1:
            c=1
            break            
    else:
        e=input(f"{player2} Press Enter to roll a die!")
        b=randint(1,6)
        print(b)
        if b==1:
            print(f"{player2} You In!")
            while True:
                e=input(f"{player1} Press Enter to roll a die!")
                a=randint(1,6)
                print(a)
                if a==1:
                    print(f"{player1} You In!")
                    game2()
                    break
                else:
                    game2()
        if a==1 and b==1:
            c=2
            break  
while True:
    if c==1:
        game2()
        if B<100:
            game()
        if A>=100:
            print(f"{player1} Yeahh!! You Won.")
            break
        elif B>=100:
            print(f"{player2} Yeahhh!! You Won.")
            break
    elif c==2:
        game()
        if A<100:
            game2()
        if A>=100: 
            print(f"{player1} Yeahh!! You Won.")
            break
        elif B>=100:
            print(f"{player2} Yeahhh!! You Won.")
            break