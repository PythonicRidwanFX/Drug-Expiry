# dashboard/management/commands/create_periodic_task.py

from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Create a periodic task to check for expiring products'

    def handle(self, *args, **options):
        # Create an interval schedule (e.g., every day)
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.DAYS,
        )

        # Create the periodic task
        task_name = 'Check for expiring products'
        task, created = PeriodicTask.objects.get_or_create(
            name=task_name,
            defaults={
                'interval': schedule,
                'task': 'dashboard.tasks.check_expiring_products',
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully created task "{task_name}"'))
        else:
            self.stdout.write(self.style.WARNING(f'Task "{task_name}" already exists'))
