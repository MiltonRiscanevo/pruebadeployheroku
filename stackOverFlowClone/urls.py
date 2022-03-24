from django.urls import path
from stackOverFlowClone import views

urlpatterns = [
    path('question/', views.question_list),
    path('answer/', views.answer_list)
    #path('cars/<int:pk>', views.car_get_info)
]