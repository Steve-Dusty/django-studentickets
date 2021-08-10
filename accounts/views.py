from django.contrib.auth import views as auth_views, logout
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')


def logout_view(request):
    logout(request)
    return redirect('home')
