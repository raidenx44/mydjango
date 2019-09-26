from django.db import models

# Create your models here.
class MyBlog(models.Model):
	Title = models.CharField(max_length=200)
	Category = models.CharField(max_length=100)

	def __str__(self):
		return self.Title

class MyBlogDetails(models.Model):
	myblog = models.ForeignKey(MyBlog, on_delete=models.CASCADE, null=False, blank=False)
	content = models.TextField(max_length=5000, blank=False)
