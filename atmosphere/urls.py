from django.conf.urls import url
from . import views
from .views import AtmosView
urlpatterns = [
    url(r'^atmos_form/$', AtmosView.as_view(), name="inputform"),
    url(r'^atmos_show/$', views.get_atmophere_show, name='aaa'),
]