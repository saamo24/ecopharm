from django.urls import path, include
from .views import MedicineAPIView, MedicineDetailAPIView


urlpatterns = [
    path('', MedicineAPIView.as_view()),
    path('<uuid:c_pk>', MedicineDetailAPIView.as_view()),
]