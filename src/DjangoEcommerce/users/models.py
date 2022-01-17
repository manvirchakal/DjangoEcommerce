from django.db import models

# Create your models here.
class RegisteredUser(models.Model):
	name 		= models.CharField(max_length=100)
	email 		= models.CharField(max_length=200)
	phone 		= models.IntegerField()