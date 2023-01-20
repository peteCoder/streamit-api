from django.urls import path, include
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
from users.views import CustomAuthToken, ChangePasswordView


urlpatterns = [
    path('user/auth-token/', CustomAuthToken.as_view(), name="user-token"),
    path('user/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('user/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('user/', user_list, name='user_list'),
    path('user/<int:pk>/', user_detail, name='user_detail'),
    
    path('profile/', profile_list, name='profile_list'),
    path('profile/<int:pk>/', profile_detail, name='profile_detail'),
    path('video/', video_list, name='video_list'),
    path('video/<int:pk>/', video_detail, name='video_detail'),
    
    # Likes
    path('video/<int:pk>/likes/', like_video, name='like_video'),
    
    path('video/category/', video_category_list, name='video_category_list'),
    path('video/category/<int:pk>/', video_category_detail, name='video_category_detail'),
]
