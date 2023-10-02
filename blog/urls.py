from django.urls import path

from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail<slug:slug>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('edit<slug:slug>/', views.edit_post, name='edit_post'),

    
]
