from django import forms

class Ragistration(forms.Form):
    fname=forms.CharField(max_length=50,label="first name")
    lname=forms.CharField(max_length=20,label="last name")
    email=forms.EmailField(label="email")
    contact=forms.IntegerField(label="contact")