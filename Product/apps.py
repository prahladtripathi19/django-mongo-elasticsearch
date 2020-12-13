from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'Product'
    def ready(self):
        import Product.signals
