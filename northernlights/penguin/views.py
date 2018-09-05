from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def bstest(request):
    return render(request, 'bstest.html')
