from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from Accounts.forms import UserCreateForm

# Create your views here.
class SignUpView(CreateView):
	form_class = UserCreateForm
	success_url = reverse_lazy('Accounts:login_url')
	template_name = 'Accounts/signup.html'