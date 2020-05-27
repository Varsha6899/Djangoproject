from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Command for creating entire team with superuser access'

    #def add_arguments(self, parser):
     #   parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for i in range(10):
            user = User.objects.create_superuser(username='user'+str(1), password='user'+str(1), email='user'+str(1)+'@gmail.com')
            print(user)
        return "True"