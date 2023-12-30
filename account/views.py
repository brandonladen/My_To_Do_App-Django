from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,logout,authenticate
from .forms import LoginForm, SignUpForm, EditProfileForm
from django.contrib import messages
from To_do_app.models import To_Do_List

# Create your views here.
def view_profile(request):
    return render(request, 'account/profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating profile. Please correct the errors.')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'account/edit_profile.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    context = {
        'form' : form
    }
    return render(request, 'account/signup.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('login.html')