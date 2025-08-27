from django.core.management.base import BaseCommand
from quiz.models import Category, Quiz, Question, Option

class Command(BaseCommand):
    help = 'Verify quiz data and fix any issues'

    def handle(self, *args, **options):
        # Check categories
        categories = Category.objects.all()
        self.stdout.write(f"Found {categories.count()} categories")
        
        # Check quizzes
        quizzes = Quiz.objects.all()
        self.stdout.write(f"Found {quizzes.count()} quizzes")
        
        # Check questions and options
        questions = Question.objects.all()
        self.stdout.write(f"Found {questions.count()} questions")
        
        options = Option.objects.all()
        self.stdout.write(f"Found {options.count()} options")
        
        # Verify each quiz has questions and options
        for quiz in quizzes:
            quiz_questions = quiz.questions.all()
            self.stdout.write(f"Quiz '{quiz.title}' has {quiz_questions.count()} questions")
            
            if quiz_questions.count() == 0:
                self.stdout.write(self.style.WARNING(f"Quiz '{quiz.title}' has no questions"))
                continue
                
            for question in quiz_questions:
                question_options = question.options.all()
                self.stdout.write(f"  Question '{question.text}' has {question_options.count()} options")
                
                if question_options.count() == 0:
                    self.stdout.write(self.style.WARNING(f"  Question '{question.text}' has no options"))
                    continue
                    
                correct_options = question_options.filter(is_correct=True)
                if correct_options.count() == 0:
                    self.stdout.write(self.style.WARNING(f"  Question '{question.text}' has no correct options"))
                elif correct_options.count() > 1:
                    self.stdout.write(self.style.WARNING(f"  Question '{question.text}' has multiple correct options"))
        
        # Check if any quizzes are inactive
        inactive_quizzes = Quiz.objects.filter(is_active=False)
        if inactive_quizzes.exists():
            self.stdout.write(self.style.WARNING(f"Found {inactive_quizzes.count()} inactive quizzes"))
            for quiz in inactive_quizzes:
                self.stdout.write(f"  - {quiz.title}")
                
        self.stdout.write(
            self.style.SUCCESS('Quiz data verification complete')
        )