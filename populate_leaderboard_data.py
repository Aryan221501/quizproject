import os
import django
import random
from datetime import datetime, timedelta

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizproject.settings')
django.setup()

from django.contrib.auth.models import User
from quiz.models import Quiz, Question, Option, QuizAttempt

def create_users():
    """Create test users for leaderboard"""
    users_data = [
        {'username': 'alice', 'email': 'alice@example.com', 'password': 'testpass123'},
        {'username': 'bob', 'email': 'bob@example.com', 'password': 'testpass123'},
        {'username': 'charlie', 'email': 'charlie@example.com', 'password': 'testpass123'},
        {'username': 'diana', 'email': 'diana@example.com', 'password': 'testpass123'},
        {'username': 'eve', 'email': 'eve@example.com', 'password': 'testpass123'},
    ]
    
    users = []
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email']
            }
        )
        if created:
            user.set_password(user_data['password'])
            user.save()
            print(f"Created user: {user.username}")
        else:
            print(f"User already exists: {user.username}")
        users.append(user)
    
    return users

def create_quiz_attempts():
    """Create multiple quiz attempts for different users"""
    users = create_users()
    quizzes = Quiz.objects.filter(is_active=True)
    
    if not quizzes:
        print("No active quizzes found!")
        return
    
    # Create multiple attempts for each user
    for user in users:
        # Each user will take 3-5 quizzes
        num_quizzes = random.randint(3, 5)
        selected_quizzes = random.sample(list(quizzes), min(num_quizzes, len(quizzes)))
        
        for quiz in selected_quizzes:
            # Simulate taking the quiz with random scores
            max_score = sum(q.points for q in quiz.questions.all())
            
            # Random score between 60% and 100% to make it realistic
            score = random.randint(int(max_score * 0.6), max_score)
            
            # Random time taken between 5 and 30 minutes
            time_taken = random.randint(300, 1800)
            
            # Random completion time within the last 30 days
            days_ago = random.randint(0, 30)
            completed_at = datetime.now() - timedelta(days=days_ago)
            
            attempt = QuizAttempt.objects.create(
                user=user,
                quiz=quiz,
                score=score,
                max_score=max_score,
                time_taken=time_taken,
            )
            
            # Update the percentage (it's calculated in the save method)
            attempt.save()
            
            print(f"Created attempt: {user.username} - {quiz.title} - Score: {score}/{max_score} ({attempt.percentage:.1f}%)")

if __name__ == '__main__':
    print("Populating quiz attempts for leaderboard...")
    create_quiz_attempts()
    print("Leaderboard population complete!")