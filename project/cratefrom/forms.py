# from django import forms
# from .models import RegistrationModel

# class Registration(forms.ModelForm):
    
#     class Meta:
#         model = RegistrationModel
#         fields = '__all__'
#         widgets = {
#             'stu_name' : forms.CharField(attrs={'class':'form-control'}),
#             "stu_email" : forms.EmailInput(attrs={'class':'form-control'}),
#             'stu_city' : forms.CharField(attrs={'class':'form-control'}),
#             'stu_mobile' : forms.IntegerField(attrs={'class':'form-control'}), 
#         }

from django import forms
from .models import StudentModel,StudentQuery

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=100, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password"
    )
    class Meta:
        model = StudentModel
        fields = ('stu_name', 'stu_email', 'stu_city', 'stu_mobile', 'stu_password')
        widgets = {
            'stu_name': forms.TextInput(attrs={'class': 'form-control'}),
            'stu_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'stu_city': forms.TextInput(attrs={'class': 'form-control'}),
            'stu_mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'stu_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class LoginForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ('stu_email','stu_password')
        widgets = {
            'stu_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'stu_password':forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class QueryForm(forms.ModelForm):
    class Meta:
        model = StudentQuery
        fields = ('stu_email','stu_name','stu_query')
        widgets = {
            'stu_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'stu_name': forms.TextInput(attrs={'class': 'form-control'}),
            'stu_query': forms.TextInput(attrs={'class': 'form-control'}),  
        }