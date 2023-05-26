from django.core.management import BaseCommand

from status.models import Status


class Command(BaseCommand):
    help = "Create status."

    def handle(self, *args, **options):
        if options["verbosity"] != 0:
            self.stdout.write(f"Creating status...")
        self.create_status(self)

    @staticmethod
    def create_status(self):
        if Status.objects.filter(id=1):
            self.stdout.write(f"Status already created")
        else:
            status_list = ('PENDING', 'SIGNED', 'CREATED', 'CANCELLED', 'POSTPONED', 'COMPLETE')

            for name in status_list:
                Status.objects.create(name=name)
