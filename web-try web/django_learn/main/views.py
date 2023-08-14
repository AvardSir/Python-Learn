from django.shortcuts import render
from django.http import HttpResponse
#def index():

# Create your views here.
def hmm(request):
    return HttpResponse("<h4>Пpoверка работы</h4>")
    #print('hi!') # нету ттут принта....

def about(request):
    #return HttpResponse("<h4>ЭБАУНТ РАБОТАЕТ</h4>")
    return render(request, 'main/about.html')

def index (request):
    return render(request, 'main/index.html')
def lol(request):
    return HttpResponse("<h4>lol</h4>")