# collector_checker_logic.py
from app.models import Product
from django.utils import timezone

def check_collector():
    products_with_collector = Product.objects.filter(with_collector=True)

    for product in products_with_collector:
        time_diff = (timezone.now() - product.updated_at).total_seconds()

        if time_diff >= 20:
            # Unassociate the product from the collector and make it available
            product.with_collector = False
            product.is_available = True
            product.save()
