import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizproject.settings')
django.setup()

from django.contrib.auth.models import User
from quiz.models import Category, Quiz, Question, Option

# Create categories
science_category, created = Category.objects.get_or_create(name="Science")
history_category, created = Category.objects.get_or_create(name="History")

# Create a quiz
quiz, created = Quiz.objects.get_or_create(
    title="General Knowledge Quiz",
    category=science_category
)

# Create questions and options if quiz was just created
if created:
    # Question 1
    q1 = Question.objects.create(
        quiz=quiz,
        text="What is the chemical symbol for water?",
        difficulty="easy"
    )
    Option.objects.create(question=q1, text="H2O", is_correct=True)
    Option.objects.create(question=q1, text="CO2", is_correct=False)
    Option.objects.create(question=q1, text="NaCl", is_correct=False)
    Option.objects.create(question=q1, text="O2", is_correct=False)
    
    # Question 2
    q2 = Question.objects.create(
        quiz=quiz,
        text="Which planet is known as the Red Planet?",
        difficulty="easy"
    )
    Option.objects.create(question=q2, text="Venus", is_correct=False)
    Option.objects.create(question=q2, text="Mars", is_correct=True)
    Option.objects.create(question=q2, text="Jupiter", is_correct=False)
    Option.objects.create(question=q2, text="Saturn", is_correct=False)
    
    # Question 3
    q3 = Question.objects.create(
        quiz=quiz,
        text="What is the powerhouse of the cell?",
        difficulty="medium"
    )
    Option.objects.create(question=q3, text="Nucleus", is_correct=False)
    Option.objects.create(question=q3, text="Mitochondria", is_correct=True)
    Option.objects.create(question=q3, text="Ribosome", is_correct=False)
    Option.objects.create(question=q3, text="Endoplasmic Reticulum", is_correct=False)
    
    print("Sample data created successfully!")
else:
    print("Sample data already exists!")