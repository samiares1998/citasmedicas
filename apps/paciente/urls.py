from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.paciente import views
urlpatterns = [
    path('pacientelist/', views.pacienteList.as_view()),
    path('pacientedet/<int:pk>', views.pacienteDetail.as_view()),

]