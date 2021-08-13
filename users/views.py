from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created succesfully')
            return redirect('login')
    else:

        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        UserForm = UserUpdateForm(request.POST, instance=request.user)
        ProfileForm = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if UserForm.is_valid() and ProfileForm.is_valid():
            UserForm.save()
            ProfileForm.save()
            messages.success(request, f'Infos Updated succesfully')
            return redirect('profile')
    else:
        UserForm = UserUpdateForm(instance=request.user)
        ProfileForm = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'UserForm': UserForm,
        'ProfileForm': ProfileForm

    }
    return render(request, 'users/profile.html', context)
