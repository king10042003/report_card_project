"""
URL configuration for report_card_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# report_card_project/urls.py

from django.urls import path
from report_card import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('search_results/', views.search_results, name='search_results'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_mark/<int:student_pk>/', views.add_mark, name='add_mark'),
    path('student_report/<int:student_pk>/', views.student_report, name='student_report'),
    path('student/<int:student_pk>/', views.student_detail, name='student_detail'),
    path('student/<int:student_pk>/delete/', views.delete_student, name='delete_student'),
    path('students/', views.student_list, name='student_list'),
    path('student/edit/<int:student_pk>/', views.student_edit, name='student_edit'),
    path('student/delete/<int:student_pk>/', views.student_delete, name='student_delete'),
]

