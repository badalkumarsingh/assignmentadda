from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('mylinks', views.link, name="link"),
    path('p/<link_c>/', views.show_snip, name='show_snips'),
]
