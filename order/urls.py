from django.urls import path, include
from .views import OrderAPIView, OrderDetailAPIView, CheckoutAPIView


urlpatterns = [
    path('order', OrderAPIView.as_view()),
    path('order-detail/<pk>', OrderDetailAPIView.as_view()),
    path('checkout', CheckoutAPIView.as_view()),
    path('checkout-detail', CheckoutAPIView.as_view()),
]