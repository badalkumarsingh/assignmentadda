from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('myblog', views.MyblogViewSet)

urlpatterns = [
    path('', views.blog, name="blog"),
    path('<str:blog_title>', views.read, name="read"),
    path('api/', views.MyblogViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
