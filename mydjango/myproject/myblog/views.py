from django.shortcuts import render
from django.http import HttpResponse
from .models import MyBlog, MyBlogDetails
from .serializers import MyBlogSerializer, MyBlogDetailsSerializer
from rest_framework import viewsets

# Create your views here.
class BlogView(viewsets.ModelViewSet):
	queryset = MyBlog.objects.all()
	serializer_class = MyBlogSerializer

class BlogViewDetails(viewsets.ModelViewSet):
	queryset = MyBlogDetails.objects.all()
	serializer_class = MyBlogDetailsSerializer

def index(request):
	return HttpResponse("Hello django!")
