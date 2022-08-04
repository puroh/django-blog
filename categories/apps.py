from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    name = "categories"

    def ready(self) -> None:
        import categories.signals
