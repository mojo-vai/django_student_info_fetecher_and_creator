from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_students),
    path('<int:pk>/', views.get_student),
    path('create/', views.create_student),
]