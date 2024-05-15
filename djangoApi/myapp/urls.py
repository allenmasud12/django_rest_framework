from django.urls import path
from myapp import views

urlpatterns = [
    path('myapi/', views.BlogList.as_view()),
    path('apidetails/<int:pk>/', views.apiDetail.as_view()),
    path('gnapidetails/<int:pk>/', views.GanapiDetail.as_view()),
    path('gnapi/', views.GnapitList.as_view()),
]