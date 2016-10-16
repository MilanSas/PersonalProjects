import random
def check_winner():
        if t1+t2+t3 == "xxx" or t1+t2+t3 == "ooo":
            return True
        elif m1+m2+m3 == "xxx" or m1+m2+m3 == "ooo":
            return True
        elif b1+b2+b3 == "xxx" or b1+b2+b3 == "ooo":
            return True
        #vertical
        elif t1+m1+b1 == "xxx" or t1+m1+b1 == "ooo":
            return True
        elif t2+m2+b2 == "xxx" or t2+m2+b2 == "ooo":
            return True
        elif t3+m3+b3 == "xxx" or t3+m3+b3 == "ooo":
            return True
        #diagonal
        elif t1+m2+b3 == "xxx" or t1+m2+b3 == "ooo":
            return True
        elif t3+m2+b1 == "xxx" or t3+m2+b1 == "ooo":
            return True
        else:
            return False
def winnertext(x, y):
    if x == True:
        print("it's a draw")
    elif y % 2 == 0:
        print("{} wins".format(p2))
    else:
        print("{} wins".format(p1))

def x_or_o(x, y):
    if y == "o":
        return "x"
    if y == "x":
        return "o"
    while x != "x" and x != "o":
        x = input("choose 'x' or 'o'\n")
    return x

def inputplayer(x, y):
        print("type {}".format(inputlist))
        p1place = input("'{}' where do you want to put your '{}'\n".format(x, y)).lower()
        print("\n")
        
        while p1place not in inputlist or p1place in excludelist:
            
            if p1place not in inputlist:
                print("wrong input\n")
            elif p1place in excludelist:
                print("place taken\n")
                
            board()           
            print("type {}".format(inputlist))
            p1place = input("'{}' where do you want to put your '{}'\n".format(x, y)).lower()
            print("\n")
        
        return p1place

def board():
    board = t1+" "+t2+" "+t3+"\n"+m1+" "+m2+" "+m3+"\n"+b1+" "+b2+" "+b3+"\n"
    print(board)

def playagain():
    x = input("Would you like to play again? 'y' for yes, 'n' for no: \n").lower()
    while x != "y" and x != "n":
        x = input("Would you like to play again? 'y' for yes, 'n' for no: \n").lower()
    if x == "y":
        return True
    return False

def new_players():
    x = input("Start with new players? 'y' for yes, 'n' for no: \n").lower()
    while x != "n" and x != "y":
        x = input("Start with new players? 'y' for yes, 'n' for no: \n").lower()
    if x == "y":
        return True
    return False
    
tl = "top left"
tm = "top mid"
tr= "top right"
ml = "mid left"
m = "mid"
mr = "mid right"
bl = "bottom left"
bm = "bottom mid"
br = "bottom right"

inputlist = [tl,tm,tr,ml,m,mr,bl,bm,br]

restart = True
newplayers = True

print("Welcome to X's and O's")

while restart:
    p1in = ""
    p2in = ""
    winner = False
    draw = False
    turn = 0
    
    t1 = "."
    t2 = "."
    t3 = "."
    m1 = "."
    m2 = "."
    m3 = "."
    b1 = "."
    b2 = "."
    b3 = "."
    excludelist = []
    
    if newplayers:
        p1 = input("player 1 name:\n")
        p2 = input("player 2 name:\n")
        switch = random.randint(0,1)
    print("\n")
    
    while not winner:
    
        if switch % 2 == 0:    
    
            print("{}'s turn".format(p1))
        
            p1in = x_or_o(p1in, p2in)
        
            board()        
        
            p1place = inputplayer(p1, p1in)
        
            excludelist.append(p1place)
        
            if p1place == "top left":
                t1 = p1in
            if p1place == "top mid":
                t2 = p1in
            if p1place == "top right":
                t3 = p1in
            if p1place == "mid left":
                m1 = p1in
            if p1place == "mid":
                m2 = p1in
            if p1place == "mid right":
                m3 = p1in
            if p1place == "bottom left":
                b1 = p1in
            if p1place == "bottom mid":
                b2 = p1in
            if p1place == "bottom right":
                b3 = p1in
        
            winner = check_winner()
            switch += 1
            turn += 1
        
            if turn == 9:
                if winner == False:
                    draw = True
                    winner = True
        else:
            print("{}'s turn".format(p2))
            
            p2in = x_or_o(p2in, p1in)

            board()

            p2place = inputplayer(p2, p2in)

            excludelist.append(p2place)
            
            if p2place == "top left":
                t1 = p2in
            if p2place == "top mid":
                t2 = p2in
            if p2place == "top right":
                t3 = p2in
            if p2place == "mid left":
                m1 = p2in
            if p2place == "mid":
                m2 = p2in
            if p2place == "mid right":
                m3 = p2in
            if p2place == "bottom left":
                b1 = p2in
            if p2place == "bottom mid":
                b2 = p2in
            if p2place == "bottom right":
                b3 = p2in
            winner = check_winner()
            turn += 1
            switch += 1
        
            if turn == 9:
                if winner == False:
                    draw = True
                    winner = True
            
    print("Game Over!")
    board()
    winnertext(draw, switch)
    restart = playagain()
    if restart:
        newplayers = new_players()
print("\n")
print("Thanks for playing!")
            
            
        
        
        
