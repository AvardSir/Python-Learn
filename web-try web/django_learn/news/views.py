from django.shortcuts import render

# Create your views here.
def news_hone(request):
    return render(request, 'main/about.html')