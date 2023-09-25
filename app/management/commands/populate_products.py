from django.core.management.base import BaseCommand
from app.models import Product
import uuid

class Command(BaseCommand):
    help = 'Populate the Product model with sample data'

    def handle(self, *args, **kwargs):
        # Create sample products
        sample_products = [
            {
                'brand_name': 'Brand A',
                'product_name': 'Product 1',
                'material_type': 'Glass',
                'price': 10.99,
            },
            {
                'brand_name': 'Brand B',
                'product_name': 'Product 2',
                'material_type': 'Plastic',
                'price': 5.99,
            },
            {
                'brand_name': 'Brand C',
                'product_name': 'Product 3',
                'material_type': 'Metal',
                'price': 11.99,
            },
            {
                'brand_name': 'Brand D',
                'product_name': 'Product 4',
                'material_type': 'Glass',
                'price': 1.99,
            },
            {
                'brand_name': 'Brand E',
                'product_name': 'Product 5',
                'material_type': 'Metal',
                'price': 14.99,
            },
            {
                'brand_name': 'Brand F',
                'product_name': 'Product 6',
                'material_type': 'Plastic',
                'price': 2.99,
            },
            {
                'brand_name': 'Brand G',
                'product_name': 'Product 7',
                'material_type': 'Plastic',
                'price': 25.99,
            },
            {
                'brand_name': 'Brand H',
                'product_name': 'Product 8',
                'material_type': 'Metal',
                'price': 13.99,
            },
            {
                'brand_name': 'Brand I',
                'product_name': 'Product 9',
                'material_type': 'Plastic',
                'price': 3.99,
            },
            {
                'brand_name': 'Brand J',
                'product_name': 'Product 10',
                'material_type': 'Glass',
                'price': 8.99,
            },
            # Add more sample products as needed
        ]

        for product_data in sample_products:
            Product.objects.create(
                uuid=uuid.uuid4(),
                brand_name=product_data['brand_name'],
                product_name=product_data['product_name'],
                material_type=product_data['material_type'],
                price=product_data['price']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Product model with sample data.'))
