from django.urls import path
from . import views

from django.contrib.auth import views as view
urlpatterns=[
    path('', views.index,name='index'),
   # path('get/<int:pk>/',PostDetailView.as_view(),name='get'),
    
    path('post/create/',views.create,name='create'),
    path('contact/',views.contact,name='contact'),

    path('register/',views.register,name='register'),
    path('login/',view.LoginView. as_view(template_name='blog/register.html'),name='login'),
    path('logout/',view.LogoutView.as_view(template_name='blog/logout.html'),name='logout'),
    path('profile/',views.profile,name='profile'),


]