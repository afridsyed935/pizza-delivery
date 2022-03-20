from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='Orders'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='OrdersDetaiulView'),
    path('update-order/<int:order_id>/', views.UpdateOrderStatusView.as_view(), name='OrdersDetaiulView'),
    path('user/<int:user_id>/orders/', views.GetAllOrderForUserView.as_view(), name='All OrdersDetaiulView for a user'),
    path('user/<int:user_id>/orders/<int:order_id>/', views.GetSpecificOrderOfUserView.as_view(), name='OrdersDetaiulView for a user'),
]