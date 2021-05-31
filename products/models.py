from django.db import models
from django.utils import timezone 
from django.urls import reverse
from django.contrib.auth.models import User


class compP(models.Model):
	Pcomp = models.CharField(max_length=200)
	Pname = models.CharField(max_length=200)
	Pcategory = models.CharField(max_length=200, default='Random')
	Pdesc = models.TextField()
	Pprice = models.IntegerField(default=0)
	Pimage = models.ImageField(upload_to='Product_pics', default='/media/Product_pics/default.jpg')
	Pemp = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.Pname

	def get_absolute_url(self):

		return reverse('home1')
