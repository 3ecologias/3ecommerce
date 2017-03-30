from django.conf.urls import include, url
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import settings
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
