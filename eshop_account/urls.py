from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user),
    path('register/', views.register),
    path('logout/', views.logout_user),
    path('dashboard/', views.dashboard_page),
    path('dashboard/edit/', views.edit_dashboard_page),
]
