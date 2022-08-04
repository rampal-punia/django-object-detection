from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import CustomUser as User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            user.is_active = False
            user.save()
            messages.success(
                request, f'Your account with {username} has been created! You are now able to log in')
            return redirect('users:registration_under_approval_url')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class RegistrationUnderApproval(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Do something here!
        return context


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
