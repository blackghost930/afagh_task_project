from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy

from . import forms
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


# def login_page_view(request):
#     if request.method == 'POST':
#         form = forms.LoginForm(request.Post)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = forms.LoginForm
#     return render(request, 'accounts/signin.html', {'LoginForm': form})
#
#
# def register_page_view(request):
#     if request.method == 'POST':
#         form = forms.NewUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             messages.success(request,f'ثبت نام شما با موفقیت انجام شد')
#             return redirect('home')
#     else:
#         form = forms.NewUserForm()
#     return render(request, 'accounts/signup.html', {'NewUserForm': form})
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('accounts/login.html')



