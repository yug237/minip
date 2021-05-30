from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Interest
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class Intr(ModelForm):
	gender = forms.CharField(max_length=8, required=False)
	age = forms.IntegerField(required=False)
	occupation = forms.CharField(max_length=100, required=False)
	choice = forms.CharField(max_length=10,label='Enter mode of shopping')

	class Meta:
		model = Interest
		fields = ['gender', 'age', 'occupation', 'choice']