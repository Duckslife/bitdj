from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^blog/', views.post_list, name='post_list'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^post_new', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)