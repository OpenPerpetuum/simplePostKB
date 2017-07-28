from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^(?P<pagenum>\d+)$', views.home, name="home"),
    url(r'^postkill', views.postkill, name="postkill"),
]