from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('businessman/<int:p_id>/', views.businessman, name='businessman'),
]
