from django.shortcuts import render
from .forms import *

# Create your views here.


def home(request):
    form=Ragistration()
    # return render(request,"home.html",{"form":form})
    if request.method=="POST":
        form=Ragistration(request.POST)
        
        if form.is_valid():
            fname=form.cleaned_data["fname"]
            lname=form.cleaned_data["lname"]
            email=form.cleaned_data["email"]
            contact=form.cleaned_data["contact"]
            print(fname,lname,email,contact)
            data={"fname":fname,"lname":lname,"email":email,"contact":contact}
    return render(request,"home.html",{"form":form})