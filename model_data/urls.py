from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_customers, name='search_customers'),
    path('model-data/', views.model_data_list, name='model_data_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
