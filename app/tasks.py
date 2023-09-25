from app.models import Product
from background_task import background

@background(schedule=10)
def move_products_from_collector_to_available(product_id):
    try:
        product = Product.objects.get(pk=product_id)

        # Check if the product is with the collector
        if product.with_collector:
            # Mark the product as available again
            product.with_collector = False
            product.is_available = True
            product.save()
    except Product.DoesNotExist:
        pass  # Handle the case where the product doesn't exist
