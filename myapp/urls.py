from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('post',views.post,name='post'),
    path('signUpData',views.signUpData,name='signUpData'),
    path('table',views.table,name='table'),
]