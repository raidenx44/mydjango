from django.shortcuts import render
#from django.http import HttpResponse
from .models import *

# Create your views here.
def BlogView(request):
	tit = myblog.object.all()
	return render(request, '', 'Title: ', tit)

"""def index(request):
	return HttpResponse("Hello django!")
"""