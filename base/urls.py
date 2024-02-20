from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/<str:id>/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('update/<str:id>', views.update, name='update'),
]