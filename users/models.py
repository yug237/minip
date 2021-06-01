from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(str):
		return f'{self.user.username} Profile'

class Interest(models.Model):
	user_t = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.CharField(max_length=8, null=True)
	age = models.IntegerField(null=True)
	Price = models.IntegerField(null=True)
	Genre = models.CharField(max_length=20, null=True)
	Movie = models.CharField(max_length=50, null=True)
	choice = models.CharField(max_length=10, null=True)

	def __str__(self):
		return self.Genre