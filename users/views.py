from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, Intr
from django.contrib.auth.models import User
from .models import Interest

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('interest')
	form = UserRegistrationForm()
	return render(request, 'users/register.html', { 'form' : form})


def interest(request):
	if request.method == 'POST':
		form2 = Intr(request.POST)
		if form2.is_valid():	
			user_1 = User.objects.last()
			gender = form2.cleaned_data.get('gender')
			age = form2.cleaned_data.get('age')
			occupation = form2.cleaned_data.get('occupation')
			choice = form2.cleaned_data.get('choice')

			add = Interest(user_t = user_1, gender = gender, age = age, occupation = occupation, choice = choice)
			add.save()

			messages.success(request, f'Account created for {user_1.username}!')

			return redirect('login')

	form2 = Intr()
	return render(request, 'users/interest.html', { 'form12' : form2})

def register1(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('login1')

	form = UserRegistrationForm()
	return render(request, 'users/register1.html', { 'form' : form})

@login_required
def profile(request):
	return render(request, 'users/profile.html')