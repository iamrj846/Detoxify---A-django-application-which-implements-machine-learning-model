from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts import forms

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'