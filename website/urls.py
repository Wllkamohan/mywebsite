from django.conf import settings
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.views.static import serve

urlpatterns = {
    path('admin/', admin.site.urls),
    path('', include('affiliate.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
}
