from django.core.management.base import BaseCommand
from backe.models import Product


class Command(BaseCommand):
    help = 'Seed the database with sample products'

    def handle(self, *args, **options):
        products_data = [
            {
                'title': "GLOBAL Sports shoes, Walking, Lightweight, Trekking, Stylish Running Shoes For Men  (White , 9)",
                'price': "₹927",
                'image': "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&q=80",
                'store': 'Flipkart',
                'affiliate_link': "https://fktr.in/D9EAR1W",
                'category': "shoes",
            },
            {
                'title': "Men's Casual Cotton T-Shirt - Pack of 3",
                'price': "₹799",
                'image': "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500&q=80",
                'store': 'myntra',
                'affiliate_link': "https://myntra.com",
                'category': "Fashion",
            },
            {
                'title': "Women's Ethnic Kurta Set with Dupatta",
                'price': "₹599",
                'image': "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=500&q=80",
                'store': 'meesho',
                'affiliate_link': "https://meesho.com",
                'category': "Ethnic Wear",
            },
            {
                'title': "Smart Watch with Fitness Tracker",
                'price': "₹3,499",
                'image': "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&q=80",
                'store': 'Flipkart',
                'affiliate_link': "https://Flipkart.in",
                'category': "Electronics",
            },
            {
                'title': "HRX by Hrithik Roshan Unisex Back To School Shoes",
                'price': "₹999",
                'image': "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&q=80",
                'store': 'myntra',
                'affiliate_link': "https://myntr.it/4F2uIFi",
                'category': "Footwear",
            },
            {
                'title': "Kitchen Cookware Set - Non Stick",
                'price': "₹899",
                'image': "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=500&q=80",
                'store': 'meesho',
                'affiliate_link': "https://meesho.com",
                'category': "Home & Kitchen",
            },
            {
                'title': "Backpack Laptop Bag with USB Charging Port",
                'price': "₹1,199",
                'image': "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500&q=80",
                'store': 'Flipkart',
                'affiliate_link': "https://Flipkart.in",
                'category': "Bags",
            },
            {
                'title': "Women's Designer Handbag",
                'price': "₹1,599",
                'image': "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=500&q=80",
                'store': 'myntra',
                'affiliate_link': "https://myntra.com",
                'category': "Accessories",
            },
            {
                'title': "Portable Bluetooth Speaker - Waterproof",
                'price': "₹1,899",
                'image': "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500&q=80",
                'store': 'Flipkart',
                'affiliate_link': "https://Flipkart.in",
                'category': "Electronics",
            },
            {
                'title': "Men's Running Shoes - Lightweight",
                'price': "₹1,499",
                'image': "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&q=80",
                'store': 'myntra',
                'affiliate_link': "https://myntra.com",
                'category': "Footwear",
            },
            {
                'title': "Bedsheet Set with Pillow Covers",
                'price': "₹699",
                'image': "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=500&q=80",
                'store': 'meesho',
                'affiliate_link': "https://meesho.com",
                'category': "Home & Kitchen",
            },
            {
                'title': "Wireless Mouse - Ergonomic Design",
                'price': "₹599",
                'image': "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&q=80",
                'store': 'Flipkart',
                'affiliate_link': "https://Flipkart.in",
                'category': "Electronics",
            },
        ]

        # Clear existing products (optional - comment out if you want to keep existing data)
        # Product.objects.all().delete()

        created_count = 0
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                title=product_data['title'],
                defaults=product_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created product: {product.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {created_count} products')
        )

