from django.urls import path
from .views import ShippingClaimView, StaticDeclarationView, ImportDeclarationView

urlpatterns = [
    path('shipping_claim', ShippingClaimView.as_view(), name='shipping_claim'),
    path('static_declaration', StaticDeclarationView.as_view(), name='static_declaration'),
    path('import_declaration', ImportDeclarationView.as_view(), name='import_declaration'),
]




