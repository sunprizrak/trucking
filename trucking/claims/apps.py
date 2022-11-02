from django.apps import AppConfig


class ClaimsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'claims'
    verbose_name = 'Заявки'

    def ready(self):
        from . import signals
