from django.db import models


class Question(models.Model):
	name = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	apartment = models.CharField(max_length=200)
	block = models.CharField(max_length=200)
	flat_no = models.CharField(max_length=200)
	bhk = models.CharField(max_length=200)
	rent = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	date_added = models.DateField(auto_now_add=True)