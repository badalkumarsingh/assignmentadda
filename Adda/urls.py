from django.contrib import admin
from django.urls import path, include
from assignment_adda.views import about
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
    path('assignmentadda/', include('assignment_adda.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('myblog.urls')),
    path('users/', include('allauth.urls')),
    path('profile/', include('users.urls')),
    path('snip/', include('snipshare.urls'), name="snip"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', about, name="about"),
    path('weather/', include('weather.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Assignment Adda"
admin.site.site_title = "Assignment Adda"
admin.site.index_title = "Welcome to Assignment Adda Portal"
