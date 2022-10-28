from django.urls import path
from .views import logout_user, ProfileView

urlpatterns = [
    path('logout', logout_user, name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
]