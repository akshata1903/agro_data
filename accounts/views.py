from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'accounts/home.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('login')
    context={'form':form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.method=="POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/crudcrop/')
            else:
                messages.info(request, "Username Or password is incorrect. ")
                # return render(request, 'login.html')
    else:
        fm=AuthenticationForm()

    fm=AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':fm})



def registerexpert(request):
    form = CreateUserForm()

    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('expertlogin')
    context={'form':form}
    return render(request, 'accounts/expertregister.html', context)

def loginexpert(request):
    if request.method=="POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/issueexpert/')
            else:
                messages.info(request, "Username Or password is incorrect. ")
                # return render(request, 'login.html')
    else:
        fm=AuthenticationForm()

    fm=AuthenticationForm()
    return render(request, 'accounts/expertlogin.html', {'form':fm})

#otheruser
def otherregister(request):
    form = CreateUserForm()

    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('otherlogin')
    context={'form':form}
    return render(request, 'accounts/otherregister.html', context)

def otherlogin(request):
    if request.method=="POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/otheruser/')
            else:
                messages.info(request, "Username Or password is incorrect. ")
                # return render(request, 'login.html')
    else:
        fm=AuthenticationForm()

    fm=AuthenticationForm()
    return render(request, 'accounts/otherlogin.html', {'form':fm})