from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def criollo(request):
    return render(request, 'criollo.html')
