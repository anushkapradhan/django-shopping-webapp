from os import name
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('category',views.category,name='category'),
    path('ganpatiFest',views.ganpatiFest,name='ganpatiFest'),
    path('diwaliFest',views.diwaliFest,name='diwaliFest'),
    path('christmasFest',views.christmasFest,name='christmasFest'),
    path('about', views.aboutus,name='aboutus')
]