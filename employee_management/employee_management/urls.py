from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from employees import views  # Import your app views

from django.urls import path

urlpatterns = [
    path('', views.employee_list, name='employee_list'),  # Employee List (Homepage)
    path('employee/create/', views.employee_create, name='employee_create'),  # Add Employee
    path('employee/update/<int:pk>/', views.employee_update, name='employee_update'),  # Update Employee
    path('employee/delete/<int:pk>/', views.employee_delete, name='employee_delete'),  # Delete Employee
    path('register/', views.register, name='register'),  # User Registration
    path('login/', auth_views.LoginView.as_view(template_name='employees/login.html'), name='login'),  # Login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
]
