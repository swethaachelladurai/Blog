from django.contrib.auth.forms import UserCreationForm
from django import forms
from  django.contrib.auth.models import User
from django.db import models
from . models import Post,Contact

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username',
                
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2']
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=[
            'title',
            'name',
            'email',
            'description'
        ]                

class PostForm(forms.ModelForm): 
    class Meta:
        model=Post
        fields=['title','content']       

   


        
   
       

