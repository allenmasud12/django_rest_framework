from django.urls import path
from myapp import views

urlpatterns = [
     path('gnapi/', views.GnapiList.as_view()),
]