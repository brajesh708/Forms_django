from django.shortcuts import render

# Create your views here.

def ragister_views(request):
    return render(request, 'register.html')

def login_views(request):
    return render(request, 'login.html' )

