from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('our_way/', views.our_way, name='our_way'),
    path('contacts/', views.contacts, name='contacts'),
    path('questions/', views.questions, name='questions'),
    path('businessman/<int:p_id>/', views.businessman, name='businessman'),
    path('api/peoples/', views.api_peoples),
    path('api/peoples/<int:pk>/', views.api_people_detail)
]
