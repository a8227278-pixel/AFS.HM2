import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from routes.models import Station, Route


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', '', os.environ.get('ADMIN_PASS', 'admin12345'))
            self.stdout.write('Superuser created.')

        if not Station.objects.exists():
            s1 = Station.objects.create(name='Central', city='Ramadi')
            s2 = Station.objects.create(name='University', city='Ramadi')
            s3 = Station.objects.create(name='Downtown', city='Baghdad')
            s4 = Station.objects.create(name='Airport', city='Baghdad')
            Route.objects.create(origin=s1, destination=s3, duration=120)
            Route.objects.create(origin=s2, destination=s4, duration=90)
            Route.objects.create(origin=s3, destination=s1, duration=130)
            self.stdout.write('Seed data created.')
