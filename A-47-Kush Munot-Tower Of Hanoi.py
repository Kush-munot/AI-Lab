from turtle import *

numOfDiscs = 6

class Disc(Turtle) :
    def __init__(self,n) :
        global numOfDiscs
        Turtle.__init__(self , shape = "square" , visible = False)
        self.pu()
        self.shapesize(1.5 , n*1.5 , 2)
        self.fillcolor(n/numOfDiscs, 0, 1-n/numOfDiscs)
        self.st()

class Tower(list):
    def __init__(self,x) :
        self.x = x
    def push(self,d) :
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self) :
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n,from_,with_,to_):
    if n>0:
        hanoi(n-1,from_,to_,with_)
        to_.push(from_.pop())
        hanoi(n-1,with_,from_,to_)

def play():
    global numOfDiscs
    onkey(None , "space")
    clear()
    try:
        hanoi(numOfDiscs,t1,t2,t3)
        # write("Press STOP Button To exit",align = "center" , font=("courier",16,"bold"))
    except Terminator:
        pass

def main() :
    global t1,t2,t3
    ht() ; penup() ; goto(0,-255)
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)

    for i in range(numOfDiscs,0,-1):
        t1.push(Disc(i))

    play()

main()
