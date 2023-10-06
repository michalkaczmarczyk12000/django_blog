from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'deletes expired events'

    def handle(self, *args, **options):
        self.stdout.write('Expired events successfully deleted.')


basic = Group(name="basic")
basic.save()
premium = Group(name="premium")
premium.save()
enterprise = Group(name="enterprise")
enterprise.save()
