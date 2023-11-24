from django.urls import path
from .views import UserCreate,UserList,EjercitoList,EjercitoCreate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', UserList.as_view(), name='user-list'),
    path('api/ejercitos/',EjercitoList.as_view(), name ='ejercito-list'),
    path('api/ejercitos/create/',EjercitoCreate.as_view(),name='ejercito-create')
    # ... otras rutas ...
]