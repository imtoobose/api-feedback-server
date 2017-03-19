from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Teacher(models.Model):
	feedback = models.TextField()
	name = models.CharField(max_length=600)
	subject = models.CharField(max_length=600)
	comments = models.CharField(max_length=1000)
	isPractical = models.BooleanField(default=False)
	division = models.CharField(max_length=600, default="NA")