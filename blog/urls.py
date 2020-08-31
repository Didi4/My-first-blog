from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/cv/', views.cv_list, name='cv'),
    path('post/<int:pk>/', views.cv_detail, name='cv_detail'),
    path('post/cv_edit', views.cv_edit, name='cv_edit'),
    #path('post/cv/', views.cv_edit, name='cv_edit'),
]