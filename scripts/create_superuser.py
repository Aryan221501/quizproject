from django.contrib.auth import get_user_model
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizproject.settings')
django.setup()

# Create superuser
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created successfully!')
else:
    print('Superuser already exists!')