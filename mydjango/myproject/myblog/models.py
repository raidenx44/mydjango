from django.db import models

# Create your models here.
class myblog(models.Model):
	Title = models.CharField(max_length=200)


def __str__(self):
	return self.Title