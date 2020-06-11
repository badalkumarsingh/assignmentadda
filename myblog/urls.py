from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.blog, name="blog"),
    path('<int:blog_id>', views.read, name="read"),
]
