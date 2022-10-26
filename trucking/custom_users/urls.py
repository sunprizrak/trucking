from django.urls import path
from .views import logout_user, ProfileView, ShippingClaimView

urlpatterns = [
    path('logout', logout_user, name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('shipping_claim', ShippingClaimView.as_view(), name='shipping_claim'),
]