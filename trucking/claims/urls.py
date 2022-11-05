from django.urls import path
from .views import ShippingClaimView, StaticDeclarationView, ImportDeclarationView, ArchiveShippingView, ArchiveStaticView, ArchiveImportView

urlpatterns = [
    path('make/shipping_claim', ShippingClaimView.as_view(), name='make_shipping_claim'),
    path('make/static_declaration', StaticDeclarationView.as_view(), name='make_static_declaration'),
    path('make/import_declaration', ImportDeclarationView.as_view(), name='make_import_declaration'),
    path('archive/shipping_claim', ArchiveShippingView.as_view(), name='archive_shipping_claim'),
    path('archive/static_declaration', ArchiveStaticView.as_view(), name='archive_static_declaration'),
    path('archive/import_declaration', ArchiveImportView.as_view(), name='archive_import_declaration'),
]




