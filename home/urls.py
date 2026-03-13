from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    # path('', views.home, name='home')
    # path('user/', views.home),
    path('', views.default, name='default'),
    path('project', views.project, name='project'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('portfolio', views.portfolio, name='portfolio'),
    # path('user', views.user, name='user'),
    # path('home', views.home, name='home'),
]
