from django.shortcuts import render , redirect 
from .forms import Signup_form
from django.contrib.auth import authenticate ,login
from accounts.models import Profile






# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = Signup_form(request.POST)
        if form.is_valid():
            form.save()
        

        username= form.cleaned_data[ 'username' ]
        password = form.cleaned_data[ 'password1' ]
        user1 = authenticate (username =  username , password = password)

        login(request,user1)
        return redirect ('/accounts/profile')

    else:
        form = Signup_form()
        return render(request , 'registration/signup.html',{'form':form})

print('3')

def profile (request):
    profile = Profile.objects.get(user=request.user)
    return render (request,'profile/profile.html',{"profile":profile})

print('4')