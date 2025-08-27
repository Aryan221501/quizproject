from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.db import connection
from quiz.models import QuizAttempt

class Command(BaseCommand):
    help = 'Perform database maintenance tasks'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear-cache',
            action='store_true',
            help='Clear application cache',
        )
        parser.add_argument(
            '--vacuum',
            action='store_true',
            help='Perform database vacuum (SQLite only)',
        )

    def handle(self, *args, **options):
        if options['clear_cache']:
            cache.clear()
            self.stdout.write(
                self.style.SUCCESS('Successfully cleared cache')
            )
        
        if options['vacuum']:
            with connection.cursor() as cursor:
                cursor.execute("VACUUM")
            self.stdout.write(
                self.style.SUCCESS('Successfully vacuumed database')
            )
        
        # Update all quiz attempt percentages
        attempts = QuizAttempt.objects.all()
        updated_count = 0
        for attempt in attempts:
            if attempt.max_score > 0:
                old_percentage = attempt.percentage
                attempt.percentage = (attempt.score / attempt.max_score) * 100
                if abs(old_percentage - attempt.percentage) > 0.01:  # Only update if changed significantly
                    attempt.save(update_fields=['percentage'])
                    updated_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Updated {updated_count} quiz attempt percentages')
        )