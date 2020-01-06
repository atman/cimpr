from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import AuthAPIView, RegisterAPIView

app_name = 'accounts'

urlpatterns = [

    path('register/', RegisterAPIView.as_view(), name="register"),
    path('jwt/', AuthAPIView.as_view(), name="obtain-token"),
    path('jwt/refresh/', refresh_jwt_token, name="refresh-token"),

]