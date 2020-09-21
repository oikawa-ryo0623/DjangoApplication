from django.shortcuts import render

from django.http import request,HttpResponseRedirect
from django.urls import reverse


class colt():
    def __init__(self,x,y):
        self.state = 0
        self.x = x
        self.y = y

    def flip(self):
        self.state = self.state*(-1)

    def put(self,turn):
        self.state = turn

field =[[0 for j in range(8)] for i in range(8)]
turncount = 0
judge = 0

def init():
    for k in range(0,8):
        for l in range(0,8):
            field[l][k] = colt(l,k)
            if k==3 and l==3 or k==4 and l==4:
                field[l][k].put(1)
            if k==3 and l==4 or k==4 and l==3:
                field[l][k].put(-1)

init()

# Create your views here.


def index(request):
    global turncount
    global judge
    turncount+=1
    explore()
    black = countBW(1)
    white = countBW(-1)
    putbool = putjudge()
    if black+white==64 or black==0 or white==0:
        judge = 2
    context = {'field':field,'black':black,'white':white,'putbool':putbool,'judge':judge}
    return render(request,'ocero/index.html',context)

def putjudge():
    for i in range(0,8):
        for j in range(0,8):
            if field[j][i].state==2:
                return False
    global judge
    judge+=1
    return True

def onceindex(request):
    return HttpResponseRedirect(reverse('ocero:index'))


def change(request):
    global turncount
    if request.method =='POST':
        for i in range(0,8):
            for j in range(0,8):
                if str(j)+ ' '+ str(i) in request.POST:
                    if field[j][i].state == 2:
                        global judge
                        judge=0
                        putColt(j,i)
                        flick(j,i,True)
                    else:
                        turncount+=1
    
    return HttpResponseRedirect(reverse('ocero:index'))

def putColt(x,y):
    turn = count()
    field[x][y].put(turn)

def deleteColt(x,y):
    field[x][y].put(0)

def countBW(bwcolt):
    coltcount = 0
    for i in range(0,8):
        for j in range(0,8):
            if field[j][i].state==bwcolt:
                coltcount += 1
    return coltcount

def count():
    #total = countBW(1) + countBW(-1)
    if turncount%2==0:
        turn = 1
    else:
        turn = -1
    return turn

def explore():
    for i in range(0,8):
        for j in range(0,8):
            if field[j][i].state == 0 or field[j][i].state == 2:
                putColt(j,i)
                flick(j,i,False)
                if field[j][i].state != 2:
                    deleteColt(j,i)

def flick(x,y,mode):
    for i in range(-1,2):
        for j in range(-1,2):
            if i != 0 or j != 0:
                changeColt(x,y,j,i,mode)


def changeColt(x,y,xarrow,yarrow,mode):
    if x+xarrow>=0 and x+xarrow<=7 and y+yarrow>=0 and y+yarrow<=7:
        next = field[x+xarrow][y+yarrow].state
        if next*(-1) == field[x][y].state:
            for i in range(2,8):
                if xarrow<0 and x-i<0:
                    break
                elif xarrow>0 and x+i>7:
                    break
                if yarrow<0 and y-i<0:
                    break
                elif yarrow>0 and y+i>7:
                    break
                if field[x+i*xarrow][y+i*yarrow].state == 0:
                    break
                if field[x+i*xarrow][y+i*yarrow].state == field[x][y].state:
                    if mode == True:
                        for j in range(1,i):
                            field[x+j*xarrow][y+j*yarrow].state = field[x][y].state
                    else:
                        field[x][y].state = 2





