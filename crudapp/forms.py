from django.core import validators
from django import forms
from .models import User

class Studentregistartion(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password','image']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),      
            }
        labels={
            'name':'Enter your name',
            'email':'Enter your email',
            'password':'Enter your password'
            
        }
        
        error_messages={
                'name':{'required':'please Enter your name'},
                'password':{'required':'please Enter your password'},
                'email':{'required':' please Enter your email'}}
  
        widgets={
            'password':forms.PasswordInput(attrs={'class':'myclass','placeholder':'Enter your password'}),
            'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter your name',}),
            'email':forms.EmailInput(attrs={'class':'myclass','placeholder':'Enter your email'}),
        }