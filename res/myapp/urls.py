from django.urls import path 
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login', views.login, name='login'),
    path('register',views.register,name='register'),
    path('new',views.new,name='new'),
    path('res',views.res,name='res'),
    path('res2',views.res2,name='res2'),
    path('templ', views.templ,name='templ'),
    path('res3',views.res3,name='res3'),
    path('res4',views.res4,name='res4'),
    path('username',views.username, name='username'),
    path('logout', views.logout, name='logout'),
    
]