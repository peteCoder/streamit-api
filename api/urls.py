from django.urls import path
from .views import (
    user_list, 
    user_detail, 
    profile_detail, 
    profile_list, 
    video_category_detail, 
    video_category_list, 
    video_detail, 
    video_list,
    like_video
)

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('profiles/', profile_list, name='profile_list'),
    path('profiles/<int:pk>/', profile_detail, name='profile_detail'),
    path('videos/', video_list, name='video_list'),
    path('videos/<int:pk>/', video_detail, name='video_detail'),
    # Likes
    path('videos/<int:pk>/likes/', like_video, name='like_video'),
    
    path('videos/categories/', video_category_list, name='video_category_list'),
    path('videos/categories/<int:pk>/', video_category_detail, name='video_category_detail'),
]
