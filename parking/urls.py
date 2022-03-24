from django.urls import path
from parking import views

urlpatterns = [
    path('cars/', views.car_List),
    path('cars/<int:pk>', views.car_get_info)
]