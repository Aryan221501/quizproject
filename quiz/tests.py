from django.test import TestCase
from django.contrib.auth.models import User
from quiz.models import Category, Quiz, Question, Option, QuizAttempt

class QuizModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name='Test Category',
            description='A test category'
        )
        self.quiz = Quiz.objects.create(
            title='Test Quiz',
            description='A test quiz',
            category=self.category,
            time_limit=10
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            text='What is 2+2?',
            difficulty='easy',
            points=1
        )
        self.option1 = Option.objects.create(
            question=self.question,
            text='3',
            is_correct=False
        )
        self.option2 = Option.objects.create(
            question=self.question,
            text='4',
            is_correct=True
        )
        self.attempt = QuizAttempt.objects.create(
            user=self.user,
            quiz=self.quiz,
            score=1,
            max_score=1,
            percentage=100.0,
            time_taken=30
        )
    
    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(str(self.category), 'Test Category')
    
    def test_quiz_creation(self):
        self.assertEqual(self.quiz.title, 'Test Quiz')
        self.assertEqual(self.quiz.time_limit, 10)
        self.assertTrue(self.quiz.is_active)
    
    def test_question_creation(self):
        self.assertEqual(self.question.text, 'What is 2+2?')
        self.assertEqual(self.question.points, 1)
    
    def test_option_creation(self):
        self.assertEqual(self.option1.text, '3')
        self.assertFalse(self.option1.is_correct)
        self.assertEqual(self.option2.text, '4')
        self.assertTrue(self.option2.is_correct)
    
    def test_quiz_attempt_creation(self):
        self.assertEqual(self.attempt.score, 1)
        self.assertEqual(self.attempt.percentage, 100.0)
        self.assertEqual(self.attempt.time_taken, 30)