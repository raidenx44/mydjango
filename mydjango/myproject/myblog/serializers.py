from rest_framework import serializers
from .models import MyBlog, MyBlogDetails

class MyBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBlog
        fields = ['Title', 'Category']

class MyBlogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBlogDetails
        fields = ['myblog', 'content']