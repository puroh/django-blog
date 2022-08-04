from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blogs"

    def ready(self) -> None:
        import blogs.signals
