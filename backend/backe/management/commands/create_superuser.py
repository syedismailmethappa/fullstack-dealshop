from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='syed',
            help='Username for the superuser',
        )
        parser.add_argument(
            '--email',
            type=str,
            default='syedmethappa0987@gmail.com',
            help='Email for the superuser',
        )
        parser.add_argument(
            '--password',
            type=str,
            default=None,
            help='Password for the superuser (if not provided, will use DJANGO_SUPERUSER_PASSWORD env var)',
        )

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password'] or self.get_password_from_env()

        if not password:
            self.stdout.write(
                self.style.WARNING(
                    'Password not provided. Skipping superuser creation. '
                    'Set DJANGO_SUPERUSER_PASSWORD environment variable or use --password flag.'
                )
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'Superuser "{username}" already exists.')
            )
            return

        if User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.WARNING(f'User with email "{email}" already exists.')
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created superuser "{username}" with email "{email}"'
            )
        )

    def get_password_from_env(self):
        import os
        return os.environ.get('DJANGO_SUPERUSER_PASSWORD')

