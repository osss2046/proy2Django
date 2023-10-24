from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('create_post', views.create_post, name='create_post'),
    path('index', views.index, name='index'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post')
    
    
]
