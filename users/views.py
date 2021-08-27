from django.forms import Form
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .decorators import authenticated_user

def register(request):
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully')
            return redirect('login')
    else:    
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@authenticated_user
def logout(request):
    messages.success(request, f'You have been logged out')
    return redirect('login')   

@login_required
def profile(request):
  if request.method == 'POST' :
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
 
    if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Account updated successfully')
            return redirect('profile')

  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html',context)
