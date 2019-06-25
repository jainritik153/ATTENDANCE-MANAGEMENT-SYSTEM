from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', home),
    url(r'^tregister/', Tregister),
    url(r'^time/', Time),
    url(r'^success/', Success),
    url(r'^sregister/',Sregister),
    url(r'^thome/', Teacher1),
    url(r'^student2/', Student2),
    url(r'^student1/', Student1),
    url(r'^update/', update)

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)