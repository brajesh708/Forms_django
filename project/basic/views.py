from django.shortcuts import render

# Create your views here.
def  home(request):
    return render(request, 'home.html')
from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.

def home(request):
    form=RegistrationForm()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        
        if form.is_valid():
            fname=form.cleaned_data["fname"]
            lname=form.cleaned_data["lname"]
            email=form.cleaned_data["email"]
            contact=form.cleaned_data["contact"]
            print(fname,lname,email,contact)
            # data={"fname":fname,"lname":lname,"email":email,"contact":contact}
            # Registration.objects.create(fname=fname,lname=lname,email=email,contact=contact)
            form.save()
    return render(request,"home.html",{"form":form})