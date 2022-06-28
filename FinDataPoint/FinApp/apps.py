from django.apps import AppConfig


class FinappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FinApp'

    def ready(self):
        import FinApp.signals