from django.urls import path

from  . import  views
urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('welcome', views.welcome, name='welcome'),
    path('loadusername', views.loadusername, name='loadusername'),
    path('addtask', views.addtask, name='addtask'),
    path('fetchtask', views.fetchtask, name='fetchtask'),
    path('updatetask', views.updatetask, name='updatetask'),
    path('deletetask', views.deletetask, name='deletetask'),


]