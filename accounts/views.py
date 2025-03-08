from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from . forms import CustomUserCreationForm, CustomAuthenticationForm


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form=CustomAuthenticationForm(data=request.POST)
            
            if form.is_valid():
                user=form.get_user()
                if user is not None:
                    login(request,user)
                    return redirect('/')
            
        form=CustomAuthenticationForm()
        context={'form':form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')
        
 
  
  
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')



def signup_view(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form=CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        
        form=CustomUserCreationForm()
        context={'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')
        
    
    
    
