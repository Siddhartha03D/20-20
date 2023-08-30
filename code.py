def rules():
    print("*anyone can start the game")
    print("*number should starts from 1")
    print("*each player can tell either of minimum one maximum 3 consecutive numbers")
    print("*the one who reaches 20 first wins the game")

#defining a function on the logic of game
def game():
    print("1.player 1")
    print("2.player 2") 
    p=int(input("who wants to start the game:"))
    if p==1:
        n=0
        cn1=0
        cn2=0
        b=1
        while(b!=0):
            n=list(map(int,input("how many numbers player1 wants to tell:").split()))
            if len(n)>3:
                print("invalid input")
                n=list(map(int,input("how many numbers player1 wants to tell:").split()))
            cn1=cn2+len(n)
            for i in n:
                print(i,end=' ')
            print("\ncurrent num:",cn1)
            n=list(map(int,input("how many numbers player2 wants to tell:").split()))
            if len(n)>3:
                print("invalid input")
                n=list(map(int,input("how many numbers player2 wants to tell:").split()))
            cn2=cn1+len(n)
            for i in n:
                print(i,end=' ')
            print("\ncurrent num:",cn2)
            if cn1==20:
                print("player 1 won the game")
                break
            if cn2==20:
                print("player 2 won the game")
                break
    else:
            n=0
            cn1=0
            cn2=0
            b=1
            while(b!=0):
                n=list(map(int,input("how many numbers player2 wants to tell:").split()))
                if len(n)>3:
                    print("invalid input")
                    n=list(map(int,input("how many numbers player2 wants to tell:").split()))
                cn1=cn2+len(n)
                for i in n:
                  print(i,end=' ')
                print("\ncurrent num:",cn1)
                n=list(map(int,input("how many numbers player1 wants to tell:").split()))
                if len(n)>3:
                    print("invalid input")
                    n=list(map(int,input("how many numbers player1 wants to tell:").split()))
                cn2=cn1+len(n)
                for i in n:
                  print(i,end=' ')
                print("\ncurrent num:",cn2)
                if cn1==20:
                    print("player 2 won the game")
                    break
                if cn2==20:
                    print("player 1 won the game")
                    break
print("1.rules")
print("2.start game")
a=int(input("enter the option:"))
if a==1:
    print(rules())#rules function call
    c=int(input("want to start the game enter 1:"))
    if c==1:
        print(game())
    else:
        print("exit the game")
    
if a==2:
    print(game())#game function call
