from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('display/<str:category>/', views.display_data_from_db, name='display_data_from_db'),
]