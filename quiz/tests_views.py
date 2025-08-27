from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from quiz.models import Category, Quiz, Question, Option

class QuizDetailViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create a category
        self.category = Category.objects.create(
            name='Test Category',
            description='A test category'
        )
        
        # Create a quiz
        self.quiz = Quiz.objects.create(
            title='Test Quiz',
            description='A test quiz',
            category=self.category,
            is_active=True
        )
        
        # Create questions and options
        self.question1 = Question.objects.create(
            quiz=self.quiz,
            text='What is 2+2?',
            difficulty='easy',
            points=1
        )
        self.option1_1 = Option.objects.create(
            question=self.question1,
            text='3',
            is_correct=False
        )
        self.option1_2 = Option.objects.create(
            question=self.question1,
            text='4',
            is_correct=True
        )
        
        self.question2 = Question.objects.create(
            quiz=self.quiz,
            text='What is the capital of France?',
            difficulty='medium',
            points=2
        )
        self.option2_1 = Option.objects.create(
            question=self.question2,
            text='London',
            is_correct=False
        )
        self.option2_2 = Option.objects.create(
            question=self.question2,
            text='Paris',
            is_correct=True
        )
    
    def test_quiz_detail_view(self):
        """Test that the quiz detail view works"""
        # Login the user
        self.client.login(username='testuser', password='testpass123')
        
        # Test accessing the quiz detail view
        response = self.client.get(reverse('quiz_detail', args=[self.quiz.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Quiz')
        self.assertContains(response, 'What is 2+2?')
        self.assertContains(response, 'What is the capital of France?')
    
    def test_inactive_quiz_not_accessible(self):
        """Test that inactive quizzes are not accessible"""
        # Make the quiz inactive
        self.quiz.is_active = False
        self.quiz.save()
        
        # Login the user
        self.client.login(username='testuser', password='testpass123')
        
        # Try to access the quiz detail view - should return 404
        response = self.client.get(reverse('quiz_detail', args=[self.quiz.id]))
        self.assertEqual(response.status_code, 404)