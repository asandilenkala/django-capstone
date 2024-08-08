from django.urls import path
from . import views

# URL patterns for routing different views in the Django application.
urlpatterns = [
    path('', views.home, name='home'),  # Route for the homepage view.
    path('projects/', views.projects, name='projects'),  # Route for the projects page view.
    path('about/', views.about, name='about'),  # Route for the about page view.
    path('login/', views.user_login, name='login'),  # Route for the user login view.
    path('logout/', views.user_logout, name='logout'),  # Route for the user logout view.
]
