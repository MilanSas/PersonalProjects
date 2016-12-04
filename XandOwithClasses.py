import random

class player:
    def __init__ (self, name):
        self.NAME = name
        self.XO = ""
    def XorO(self, other):
        if other.XO == "X":
            self.XO = "O"
        elif other.XO == "O":
            self.XO = "X"
        else:
            while self.XO != "X" and self.XO != "O": 
                self.XO = input("X or O") 
        return self.XO
class xando:
    def __init__(self, player1, player2):
        self.P1 = player1
        self.P2 = player2
        self.WINNER = ""
        self.DRAW = False
    
    def Board(self, t1, t2, t3, m1, m2, m3, b1, b2, b3):
        board = "Game\t\t" + "Input\n" + t1+" "+t2+" "+t3+"\t\t7 8 9\n"+m1+" "+m2+" "+m3+"\t\t4 5 6\n"+b1+" "+b2+" "+b3+"\t\t1 2 3\n"
        print(board)
    
    def Game(self):
        tl = "7"
        tm = "8"
        tr= "9"
        ml = "4"
        m = "5"
        mr = "6"
        bl = "1"
        bm = "2"
        br = "3"
        
        t1 = "."
        t2 = "."
        t3 = "."
        m1 = "."
        m2 = "."
        m3 = "."
        b1 = "."
        b2 = "."
        b3 = "."
        inputlist = [tl,tm,tr,ml,m,mr,bl,bm,br]
        excludelist = []   
        turn = 0
        switch = random.randint(0,1)
        
        while self.WINNER == "" and self.DRAW == False:
            if switch % 2 == 0:
                speler = self.P1
                other = self.P2
            else:
                speler = self.P2
                other = self.P1
            
            print(speler.NAME + "'s turn")
            
            pinput = speler.XorO(other)
            
            self.Board(t1, t2, t3, m1, m2, m3, b1, b2, b3)
            
            print("Type the number corresponding to the input".format(inputlist))
            p1place = input("'{}' where do you want to put your '{}'\n".format(speler.NAME, pinput)).lower()
            print("\n")
        
            while p1place not in inputlist or p1place in excludelist:
            
                if p1place not in inputlist:
                    print("Wrong input")
                elif p1place in excludelist:
                    print("Place taken")
                self.Board(t1, t2, t3, m1, m2, m3, b1, b2, b3)
                print("Type the number corresponding to the input".format(inputlist))
                p1place = input("'{}' where do you want to put your '{}'\n".format(speler.NAME, pinput)).lower()
            
        
            excludelist.append(p1place)
        
            if p1place == "7":
                t1 = pinput
            if p1place == "8":
                t2 = pinput
            if p1place == "9":
                t3 = pinput
            if p1place == "4":
                m1 = pinput
            if p1place == "5":
                m2 = pinput
            if p1place == "6":
                m3 = pinput
            if p1place == "1":
                b1 = pinput
            if p1place == "2":
                b2 = pinput
            if p1place == "3":
                b3 = pinput
                
            if t1+t2+t3 == "XXX" or t1+t2+t3 == "OOO":
                self.WINNER = speler.NAME
            elif m1+m2+m3 == "XXX" or m1+m2+m3 == "OOO":
                self.WINNER = speler.NAME
            elif b1+b2+b3 == "XXX" or b1+b2+b3 == "OOO":
                self.WINNER = speler.NAME
            #vertical
            elif t1+m1+b1 == "XXX" or t1+m1+b1 == "OOO":
                self.WINNER = speler.NAME
            elif t2+m2+b2 == "XXX" or t2+m2+b2 == "OOO":
                self.WINNER = speler.NAME
            elif t3+m3+b3 == "XXX" or t3+m3+b3 == "OOO":
                self.WINNER = speler.NAME
            #diagonal
            elif t1+m2+b3 == "XXX" or t1+m2+b3 == "OOO":
                self.WINNER = speler.NAME
            elif t3+m2+b1 == "XXX" or t3+m2+b1 == "OOO":
                self.WINNER = speler.NAME
            
            switch += 1
            turn += 1
        
            if turn == 9:
                if self.WINNER == "":
                    self.DRAW = True
        
        print("Game over")
        if self.DRAW == True:
            print("DRAW")
        else:
            print(speler.NAME + " WON!")
                    
            

player1 = player(input("Player1 put in your name"))
player2 = player(input("Player2 put in your name"))
game1 = xando(player1, player2)
game1.Game()

            
            
            
                
            
        
        