from django.conf.urls import url
from risk import views


urlpatterns = [
    url(r'^risk/$', views.risk_list, name='index'),
    url(r'^risk/(?P<pk>[0-9]+)/$', views.risk_detail),
]