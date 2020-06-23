"""Adda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import register
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sites.models import Site

admin.site.unregister(Site)
class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')
admin.site.register(Site, SiteAdmin)

handler404 = 'assignment_adda.views.error_404_view'
handler500 = 'assignment_adda.views.error_500_view'

urlpatterns = [
    path('', include('assignment_adda.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    path('registration/', register, name='register'),
    path('admin/', admin.site.urls),
    path('blog/', include('myblog.urls')),
    path('users/', include('allauth.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Assignment Adda"
admin.site.site_title = "Assignment Adda"
admin.site.index_title = "Welcome to Assignment Adda Portal"


