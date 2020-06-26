from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.snip, name="snip"),
    path('mylinks', views.link, name="link"),
    path('p/<link_c>/', views.show_snip, name='show_snips'),
    path('edit_snip/<snip_id>', views.edit_snip, name='edit_snip'),
]
