from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloAuthView.as_view(), name='Hello Auth!'),
    path('signup/', views.CreateUserView.as_view(), name='User Signup')
]