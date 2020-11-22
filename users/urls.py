from .views import RegisterAPI, CustomUserView, CustomUserViewSet
from django.urls import path


urlpatterns = [
    path('api-token-auth/', RegisterAPI.as_view(), name='register'),
    path('api/v1/users/', CustomUserView.as_view()),
    path('api/v1/users/<str:id>/', CustomUserViewSet.as_view()),
]   
    