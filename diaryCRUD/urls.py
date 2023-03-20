from django.urls import path
from . import views

urlpatterns=[
    path('', views.DiaryListAPIView.as_view()),
    path('<int:pk>/', views.DiaryDetailAPIView.as_view())
]