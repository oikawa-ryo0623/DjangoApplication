from django.shortcuts import render

from django.http import request,HttpResponseRedirect
from django.urls import reverse
#ToDo

#グリッド数8を取得
#その後...

class colt():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = 0

    def flip(self):
        self.state = self.state*(-1)

    def put(self,turn):
        self.state = turn
        
field = []
for i in range(0,8):
    for j in range(0,8):
        field.append(colt(i,j))

# Create your views here.


def index(request):

    context = {'field':field,}
    return render(request,'ocero/index.html',context)

def change(request):
    if request.method =='POST':
        for i in range(0,4):
            for j in range(0,4):

                if str(i)+ ' '+ str(j) in request.POST:
                    flick(i,j)
    
    return HttpResponseRedirect(reverse('ocero:index'))


def flick(i,j):
    for col in field:
        if col.x == i and col.y == j:
            col.put(1)







