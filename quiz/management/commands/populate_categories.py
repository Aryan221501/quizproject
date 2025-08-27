from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from quiz.models import Category, Quiz, Question, Option

class Command(BaseCommand):
    help = 'Create comprehensive quiz data for all categories'

    def handle(self, *args, **options):
        # Create categories if they don't exist
        categories_data = [
            {"name": "Science", "description": "Test your knowledge of scientific concepts"},
            {"name": "History", "description": "Explore historical events and figures"},
            {"name": "Geography", "description": "Discover the world around you"},
            {"name": "Literature", "description": "Test your literary knowledge"},
            {"name": "Mathematics", "description": "Challenge your math skills"},
            {"name": "Technology", "description": "Test your tech knowledge"},
            {"name": "General", "description": "Mixed knowledge questions"}
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
                "description": "Fundamental science concepts",
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
                "description": "Historical events and figures",
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
                    },
                    {
                        "text": "Which civilization built the Machu Picchu?",
                        "difficulty": "hard",
                        "points": 3,
                        "options": [
                            {"text": "Aztec", "is_correct": False},
                            {"text": "Maya", "is_correct": False},
                            {"text": "Inca", "is_correct": True},
                            {"text": "Egyptian", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "World Geography Quiz",
                "description": "Countries, capitals, and landmarks",
                "category": categories[2],  # Geography
                "time_limit": 12,
                "questions": [
                    {
                        "text": "What is the capital of Canada?",
                        "difficulty": "easy",
                        "points": 1,
                        "options": [
                            {"text": "Toronto", "is_correct": False},
                            {"text": "Vancouver", "is_correct": False},
                            {"text": "Ottawa", "is_correct": True},
                            {"text": "Montreal", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which is the longest river in the world?",
                        "difficulty": "medium",
                        "points": 2,
                        "options": [
                            {"text": "Amazon River", "is_correct": False},
                            {"text": "Nile River", "is_correct": True},
                            {"text": "Yangtze River", "is_correct": False},
                            {"text": "Mississippi River", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is the only country that is completely surrounded by another country?",
                        "difficulty": "hard",
                        "points": 3,
                        "options": [
                            {"text": "Monaco", "is_correct": False},
                            {"text": "San Marino", "is_correct": False},
                            {"text": "Vatican City", "is_correct": True},
                            {"text": "Liechtenstein", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "Classic Literature Quiz",
                "description": "Famous authors and books",
                "category": categories[3],  # Literature
                "time_limit": 15,
                "questions": [
                    {
                        "text": "Who wrote 'Pride and Prejudice'?",
                        "difficulty": "easy",
                        "points": 1,
                        "options": [
                            {"text": "Charlotte Brontë", "is_correct": False},
                            {"text": "Jane Austen", "is_correct": True},
                            {"text": "Emily Dickinson", "is_correct": False},
                            {"text": "Virginia Woolf", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is the pen name of Samuel Clemens?",
                        "difficulty": "medium",
                        "points": 2,
                        "options": [
                            {"text": "Lewis Carroll", "is_correct": False},
                            {"text": "Mark Twain", "is_correct": True},
                            {"text": "Oscar Wilde", "is_correct": False},
                            {"text": "Charles Dickens", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which Shakespeare play features the character Shylock?",
                        "difficulty": "hard",
                        "points": 3,
                        "options": [
                            {"text": "Hamlet", "is_correct": False},
                            {"text": "Macbeth", "is_correct": False},
                            {"text": "The Merchant of Venice", "is_correct": True},
                            {"text": "King Lear", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "Basic Mathematics Quiz",
                "description": "Fundamental math concepts",
                "category": categories[4],  # Mathematics
                "time_limit": 10,
                "questions": [
                    {
                        "text": "What is the value of π (pi) approximately?",
                        "difficulty": "easy",
                        "points": 1,
                        "options": [
                            {"text": "3.14", "is_correct": True},
                            {"text": "2.71", "is_correct": False},
                            {"text": "1.61", "is_correct": False},
                            {"text": "4.67", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is the derivative of x²?",
                        "difficulty": "medium",
                        "points": 2,
                        "options": [
                            {"text": "x", "is_correct": False},
                            {"text": "2x", "is_correct": True},
                            {"text": "x²", "is_correct": False},
                            {"text": "2", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is the formula for the area of a circle?",
                        "difficulty": "hard",
                        "points": 3,
                        "options": [
                            {"text": "πr", "is_correct": False},
                            {"text": "πr²", "is_correct": True},
                            {"text": "2πr", "is_correct": False},
                            {"text": "2πr²", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "Modern Technology Quiz",
                "description": "Contemporary tech knowledge",
                "category": categories[5],  # Technology
                "time_limit": 12,
                "questions": [
                    {
                        "text": "What does CPU stand for?",
                        "difficulty": "easy",
                        "points": 1,
                        "options": [
                            {"text": "Computer Processing Unit", "is_correct": False},
                            {"text": "Central Processing Unit", "is_correct": True},
                            {"text": "Central Program Unit", "is_correct": False},
                            {"text": "Computer Program Unit", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which company developed the Python programming language?",
                        "difficulty": "medium",
                        "points": 2,
                        "options": [
                            {"text": "Microsoft", "is_correct": False},
                            {"text": "Google", "is_correct": False},
                            {"text": "Apple", "is_correct": False},
                            {"text": "Python Software Foundation", "is_correct": True}
                        ]
                    },
                    {
                        "text": "What is the name of the first electronic computer?",
                        "difficulty": "hard",
                        "points": 3,
                        "options": [
                            {"text": "ENIAC", "is_correct": True},
                            {"text": "UNIVAC", "is_correct": False},
                            {"text": "EDVAC", "is_correct": False},
                            {"text": "COLOSSUS", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "General Knowledge Quiz",
                "description": "Mixed knowledge questions",
                "category": categories[6],  # General
                "time_limit": 15,
                "questions": [
                    {
                        "text": "What is the largest mammal in the world?",
                        "difficulty": "easy",
                        "points": 1,
                        "options": [
                            {"text": "Elephant", "is_correct": False},
                            {"text": "Blue Whale", "is_correct": True},
                            {"text": "Giraffe", "is_correct": False},
                            {"text": "Hippopotamus", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which planet is known as the Red Planet?",
                        "difficulty": "medium",
                        "points": 2,
                        "options": [
                            {"text": "Venus", "is_correct": False},
                            {"text": "Mars", "is_correct": True},
                            {"text": "Jupiter", "is_correct": False},
                            {"text": "Saturn", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is the currency of Japan?",
                        "difficulty": "hard",
                        "points": 3,
                        "options": [
                            {"text": "Won", "is_correct": False},
                            {"text": "Yuan", "is_correct": False},
                            {"text": "Yen", "is_correct": True},
                            {"text": "Ringgit", "is_correct": False}
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
                    "time_limit": quiz_data["time_limit"],
                    "is_active": True
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
            else:
                self.stdout.write(f"Quiz '{quiz.title}' already exists")
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated all categories with quizzes')
        )