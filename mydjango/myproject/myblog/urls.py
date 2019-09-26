from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('blog', views.BlogView)
router.register('blog-details', views.BlogViewDetails)

urlpatterns = [
    path('index', views.index, name='index'),
    path('', include(router.urls)),
]