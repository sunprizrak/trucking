from django.contrib import admin
from .models import PreliminaryClaim, ShippingClaim, ClaimDoc


@admin.register(ClaimDoc)
class ClaimDocAdmin(admin.ModelAdmin):
    pass


@admin.register(PreliminaryClaim)
class PreliminaryClaimAdmin(admin.ModelAdmin):
    list_display = ('contact_person', 'created')
    fieldsets = (
        ('Информация о грузе', {'fields': (('shipping_name', 'gross_weight'), ('count_seats', 'type_seats'),)}),
        ('Габариты места', {'fields': (('length_seats', 'width_seats', 'height_seats'),)}),
        ('Вид транспорта', {'fields': (('fly', 'train', 'ship', 'auto'),)}),
        (None, {'fields': (('point_departure', 'destination'),)}),
        ('Предпологаемая дата отгрузки', {'fields': (('start_date', 'end_date'),)}),
        ('Контактная информация', {'fields': ('contact_person', 'phone_number', ('messenger', 'messenger_number'))}),
    )
    search_fields = ("contact_person", "phone_number")
    ordering = ("-created",)


@admin.register(ShippingClaim)
class ShippingClaimAdmin(admin.ModelAdmin):
    list_display = ('get_email', 'get_name', 'shipping_name', 'created')

    @admin.display(ordering='user__email', description='Пользователь')
    def get_email(self, obj):
        return obj.user.email

    @admin.display(ordering='user__name', description='Наименование организации')
    def get_name(self, obj):
        return obj.user.name

    fieldsets = (
        (None, {'fields': ('user', )}),
        ('Информация о грузе', {'fields': ('shipping_name', 'code', ('gross_weight', 'cargo_features', 'cargo_insurance', ),  ('count_seats', 'type_seats'),)}),
        ('Габариты места', {'fields': (('length_seats', 'width_seats', 'height_seats'),)}),
        (None, {'fields': ('transport', ('point_departure', 'destination'), 'date_loading',)}),
        ('Контактная информация', {'fields': ('person_loading', 'per_load_number', ('per_load_msg', 'per_load_msg_number'),
                                              'person_unloading', 'per_unload_number', ('per_unload_msg', 'per_unload_msg_number'))}),
    )
    search_fields = ('user__email', 'user__name',)
    ordering = ('-created',)