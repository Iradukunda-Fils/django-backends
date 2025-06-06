from django.urls import path
from .views import login_view, home_view, logout_view

app_name = 'login'

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    # Add other account-related URLs here
]