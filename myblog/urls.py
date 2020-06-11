from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.blog, name="blog"),
    path('<str:blog_title>', views.read, name="read"),
]
