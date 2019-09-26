from django.contrib import admin
from .models import MyBlog, MyBlogDetails
# Register your models here.

admin.site.register(MyBlog)

admin.site.register(MyBlogDetails)