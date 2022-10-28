from django.urls import path
from .views import ShippingClaimView

urlpatterns = [
    path('', ShippingClaimView.as_view(), name='shipping_claim'),
]




