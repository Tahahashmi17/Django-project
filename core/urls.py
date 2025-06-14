from django.urls import path
from . import views
from .views import register_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('public/', views.public_view, name='public-api'),
    path('protected/', views.protected_view, name='protected-api'),
    path('login/', obtain_auth_token, name='api_token_auth'),  # Token Login
    path('register/', register_view, name='register')
]
