from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView,UserProfileAPIView,UserProfileUpdateAPIView

urlpatterns = [
    # your other urlpatterns here
    path('api/register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('api/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('api/profile/', UserProfileAPIView.as_view(), name='user-profile'),
    path('api/profile/update', UserProfileUpdateAPIView.as_view(), name='user-update-view'),
]
