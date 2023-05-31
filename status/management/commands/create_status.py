from django.core.management import BaseCommand

from status.models import Status


class Command(BaseCommand):
    help = "Create status if they aren't present."

    def handle(self, *args, **options):
        if options["verbosity"] != 0:
            self.stdout.write(f"Checking if status are present...")
        self.create_status(self)

    @staticmethod
    def create_status(self):
        status_list = ('PENDING', 'SIGNED', 'CREATED', 'CANCELLED', 'POSTPONED', 'COMPLETE')

        for name in status_list:
            Status.objects.get_or_create(name=name)
