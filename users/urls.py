from django.urls import path, include
from . import views



urlpatterns = [
    # path('auth-token/', views.CustomAuthToken.as_view(), name="user-token"),
    # path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    # Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('email/', views.my_email, name='email')
]

