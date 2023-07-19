from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('home',views.home,name='home'),
]
