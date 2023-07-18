
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home),
    
    path('post/<int:pk>/', views.postDetail, name='post_detail'),
    
    
    path('olderpost/', views.olderPost, name= 'older_post'),
    path('tags/', views.tags, name= 'tags'),
    path('tags/<str:tag>/', views.tagSpecific, name="tag_specific")
]
