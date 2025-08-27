from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create initial data for the quiz application'

    def handle(self, *args, **options):
        from quiz.models import Category, Quiz, Question, Option
        from django.contrib.auth.models import User
        
        # Create categories
        categories_data = [
            {"name": "Science", "description": "Test your knowledge of scientific concepts"},
            {"name": "History", "description": "Explore historical events and figures"},
            {"name": "Geography", "description": "Discover the world around you"},
            {"name": "Literature", "description": "Test your literary knowledge"},
            {"name": "Mathematics", "description": "Challenge your math skills"},
        ]
        
        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data["name"],
                defaults={"description": cat_data["description"]}
            )
            categories.append(category)
            if created:
                self.stdout.write(f"Created category: {category.name}")
        
        # Create quizzes for each category
        quizzes_data = [
            {
                "title": "Basic Science Quiz",
                "description": "A fundamental science knowledge test",
                "category": categories[0],  # Science
                "time_limit": 10,
                "questions": [
                    {
                        "text": "What is the chemical symbol for gold?",
                        "difficulty": "easy",
                        "points": 1,
                        "options": [
                            {"text": "Go", "is_correct": False},
                            {"text": "Gd", "is_correct": False},
                            {"text": "Au", "is_correct": True},
                            {"text": "Ag", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is the hardest natural substance on Earth?",
                        "difficulty": "medium",
                        "points": 2,
                        "options": [
                            {"text": "Gold", "is_correct": False},
                            {"text": "Iron", "is_correct": False},
                            {"text": "Diamond", "is_correct": True},
                            {"text": "Platinum", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is the study of mushrooms called?",
                        "difficulty": "hard",
                        "points": 3,
                        "options": [
                            {"text": "Mycology", "is_correct": True},
                            {"text": "Alchemy", "is_correct": False},
                            {"text": "Microbiology", "is_correct": False},
                            {"text": "Botany", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "World History Quiz",
                "description": "Test your knowledge of world history",
                "category": categories[1],  # History
                "time_limit": 15,
                "questions": [
                    {
                        "text": "In which year did World War II end?",
                        "difficulty": "easy",
                        "points": 1,
                        "options": [
                            {"text": "1944", "is_correct": False},
                            {"text": "1945", "is_correct": True},
                            {"text": "1946", "is_correct": False},
                            {"text": "1947", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Who was the first President of the United States?",
                        "difficulty": "medium",
                        "points": 2,
                        "options": [
                            {"text": "Thomas Jefferson", "is_correct": False},
                            {"text": "John Adams", "is_correct": False},
                            {"text": "George Washington", "is_correct": True},
                            {"text": "Benjamin Franklin", "is_correct": False}
                        ]
                    }
                ]
            }
        ]
        
        # Create quizzes and questions
        for quiz_data in quizzes_data:
            quiz, created = Quiz.objects.get_or_create(
                title=quiz_data["title"],
                category=quiz_data["category"],
                defaults={
                    "description": quiz_data["description"],
                    "time_limit": quiz_data["time_limit"]
                }
            )
            
            if created:
                self.stdout.write(f"Created quiz: {quiz.title}")
                
                # Create questions for this quiz
                for q_data in quiz_data["questions"]:
                    question = Question.objects.create(
                        quiz=quiz,
                        text=q_data["text"],
                        difficulty=q_data["difficulty"],
                        points=q_data["points"]
                    )
                    
                    # Create options for this question
                    for opt_data in q_data["options"]:
                        Option.objects.create(
                            question=question,
                            text=opt_data["text"],
                            is_correct=opt_data["is_correct"]
                        )
                        
                self.stdout.write(f"Added {len(quiz_data['questions'])} questions to {quiz.title}")
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created initial data')
        )