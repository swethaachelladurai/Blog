from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Post
from .forms import RegistrationForm,PostForm,ContactForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from blog.models import User
user=User
# Create your views here.
def index(request):
    post=Post.objects.all()

    return render(request,"blog/index.html",{'posts':post}) 
  
   




def register(request):
        form=RegistrationForm(request.POST or None)
        if request.method=='POST':

            form=RegistrationForm(request.POST)
        if form.is_valid():
            
            form.save()
            data=form.cleaned_data
            name=data['first_name']
            messages.success(request,f"Your account has been created Successfully {name}")
            return redirect('login')
        

        return render(request,"blog/register.html",{'form':form})
@login_required             
def profile(request):
    return render(request,'blog/profile.html')

def contact(request):
    form= ContactForm(request.POST or None)
    if request.method=='POST':
        
        if form.is_valid():
            form.save(commit=True)
            data=form.cleaned_data
            name=data['name']
            messages.success(request,f"Thank You {name} we will reach you Shortly")
            return redirect('index')

            
    return render(request,"blog/contact.html",{'form':form})
@login_required
def create(request):

    form=PostForm(request.POST or None)
    if request.method=='POST':
            if form.is_valid():
                i=form.save(commit=False)
                i.author=request.user
                form.save(commit=True)
                messages.success(request,"Post created Succesfully")
                return redirect('index')
        
    return render(request,"blog/post_form.html",{'form':form})            

        


