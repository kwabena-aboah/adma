from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login_now/', views.login_now, name='login_now'),
    path('login/', views.login, name='login'),
    path('user_logout/', views.user_logout, name='user_logout'),
]
