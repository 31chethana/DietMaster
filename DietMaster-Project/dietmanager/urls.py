from django.conf.urls import url
from . import views

app_name = 'dietmanager'
urlpatterns = [
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^main/$', views.main, name="main"),
    url(r'^login/$', views.login_user, name="login_user"),
    url(r'^health/$', views.health, name="health"),
    url(r'^store/$', views.store, name="store"),
    url(r'^getdiet/$', views.getDiet, name="getdiet"),
    url(r'^track/$',views.store, name="track"),
    url(r'^getdiet/$',views.getDiet, name="getdiet"),
    url(r'^response/$',views.store,name="response"),

]
