from django.db import models

# Create your models here.
class Date_one(models.Model):
	#id=models.CharField(max_length=200)
	name=models.CharField(max_length=23)
	email_id=models.CharField(max_length=23)
	password=models.CharField(max_length=23)
	age=models.CharField(max_length=23)
	def  __str__(self):
		return self.name