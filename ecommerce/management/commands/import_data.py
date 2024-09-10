import json
import os
from django.core.files import File
from django.core.management.base import BaseCommand
from ecommerce.models import Category, Product
from django.conf import settings

class Command(BaseCommand):
    help = 'Import categories and products from JSON files'

    def handle(self, *args, **kwargs):
        self.import_categories()
        self.import_products()

    def import_categories(self):
        with open('shop/data/categories.json', 'r') as file:
            data = json.load(file)
            for item in data:
                category, created = Category.objects.update_or_create(
                    name=item['name'],
                    defaults={
                        'description': item.get('description', '')
                    }
                )
                if 'image' in item:
                    image_path = os.path.join(settings.MEDIA_ROOT, item['image'])
                    if os.path.exists(image_path):
                        with open(image_path, 'rb') as image_file:
                            category.image.save(os.path.basename(image_path), File(image_file))
                self.stdout.write(self.style.SUCCESS(f'Category "{item["name"]}" imported successfully'))

    def import_products(self):
        with open('ecommerce/data/products.json', 'r') as file:
            data = json.load(file)
            for item in data:
                category = Category.objects.get(id=item['category'])
                
                # Create or update product
                product, created = Product.objects.update_or_create(
                    name=item['name'],
                    defaults={
                        'description': item['description'],
                        'price': item['price'],
                        'stock': item['stock'],
                        'category': category
                    }
                )

                # Handle image upload
                image_path = item.get('image')
                if image_path:
                    # Construct the full path to the image file in the media folder
                    media_image_path = os.path.join(settings.MEDIA_ROOT, 'products', image_path)
                    self.stdout.write(self.style.SUCCESS(f'Processing image: {media_image_path}'))

                    if os.path.exists(media_image_path):
                        with open(media_image_path, 'rb') as img_file:
                            product.image.save(image_path, File(img_file))
                            product.save()  # Save the product to update the image field
                            self.stdout.write(self.style.SUCCESS(f'Image saved: {image_path}'))
                    else:
                        self.stdout.write(self.style.ERROR(f'Image file not found: {media_image_path}'))
        
        self.stdout.write(self.style.SUCCESS('Products imported successfully'))
