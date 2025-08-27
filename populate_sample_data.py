import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizproject.settings')
django.setup()

from quiz.models import Category, Quiz, Question, Option

# --- Clear existing data ---
def clear_data():
    print("Clearing existing data...")
    Option.objects.all().delete()
    Question.objects.all().delete()
    Quiz.objects.all().delete()
    Category.objects.all().delete()
    print("Data cleared.")

# --- Data to be populated ---
categories_data = [
    {"name": "Science", "description": "Test your knowledge of scientific concepts."},
    {"name": "History", "description": "Explore historical events and figures."},
    {"name": "Geography", "description": "Challenge your geographical knowledge."},
    {"name": "Literature", "description": "Quizzes on famous books and authors."},
    {"name": "Mathematics", "description": "Solve mathematical problems."},
    {"name": "Technology", "description": "Stay updated with the latest in tech."},
    {"name": "Movies", "description": "Test your knowledge of cinema."},
    {"name": "General Knowledge", "description": "A mix of questions from various fields."}
]

quizzes_data = {
    "Science": [
        {
            "title": "Advanced Physics Quiz",
            "questions": [
                {"text": "What is the speed of light in a vacuum?", "difficulty": "easy", "options": [
                    {"text": "300,000 km/s", "is_correct": True},
                    {"text": "150,000 km/s", "is_correct": False},
                    {"text": "450,000 km/s", "is_correct": False},
                    {"text": "600,000 km/s", "is_correct": False}
                ]},
                {"text": "Who formulated the theory of relativity?", "difficulty": "easy", "options": [
                    {"text": "Isaac Newton", "is_correct": False},
                    {"text": "Albert Einstein", "is_correct": True},
                    {"text": "Galileo Galilei", "is_correct": False},
                    {"text": "Nikola Tesla", "is_correct": False}
                ]},
                {"text": "What is the unit of electrical resistance?", "difficulty": "medium", "options": [
                    {"text": "Volt", "is_correct": False},
                    {"text": "Ampere", "is_correct": False},
                    {"text": "Ohm", "is_correct": True},
                    {"text": "Watt", "is_correct": False}
                ]},
                {"text": "What is the most abundant gas in Earth's atmosphere?", "difficulty": "medium", "options": [
                    {"text": "Oxygen", "is_correct": False},
                    {"text": "Nitrogen", "is_correct": True},
                    {"text": "Carbon Dioxide", "is_correct": False},
                    {"text": "Argon", "is_correct": False}
                ]},
                {"text": "What is the principle behind fiber optics?", "difficulty": "hard", "options": [
                    {"text": "Total internal reflection", "is_correct": True},
                    {"text": "Refraction", "is_correct": False},
                    {"text": "Diffraction", "is_correct": False},
                    {"text": "Interference", "is_correct": False}
                ]},
                {"text": "What is the escape velocity of Earth?", "difficulty": "hard", "options": [
                    {"text": "11.2 km/s", "is_correct": True},
                    {"text": "9.8 km/s", "is_correct": False},
                    {"text": "15.5 km/s", "is_correct": False},
                    {"text": "22.4 km/s", "is_correct": False}
                ]},
                {"text": "What is the phenomenon where light bends around obstacles?", "difficulty": "medium", "options": [
                    {"text": "Reflection", "is_correct": False},
                    {"text": "Refraction", "is_correct": False},
                    {"text": "Diffraction", "is_correct": True},
                    {"text": "Dispersion", "is_correct": False}
                ]},
                {"text": "What is the main component of natural gas?", "difficulty": "easy", "options": [
                    {"text": "Methane", "is_correct": True},
                    {"text": "Ethane", "is_correct": False},
                    {"text": "Propane", "is_correct": False},
                    {"text": "Butane", "is_correct": False}
                ]},
                {"text": "What type of energy is stored in a battery?", "difficulty": "easy", "options": [
                    {"text": "Kinetic energy", "is_correct": False},
                    {"text": "Potential energy", "is_correct": False},
                    {"text": "Chemical energy", "is_correct": True},
                    {"text": "Mechanical energy", "is_correct": False}
                ]},
                {"text": "What is the study of earthquakes called?", "difficulty": "medium", "options": [
                    {"text": "Seismology", "is_correct": True},
                    {"text": "Geology", "is_correct": False},
                    {"text": "Volcanology", "is_correct": False},
                    {"text": "Meteorology", "is_correct": False}
                ]}
            ]
        }
    ],
    "History": [
        {
            "title": "Ancient Civilizations",
            "questions": [
                {"text": "Which civilization built the pyramids?", "difficulty": "easy", "options": [
                    {"text": "Ancient Rome", "is_correct": False},
                    {"text": "Ancient Greece", "is_correct": False},
                    {"text": "Ancient Egypt", "is_correct": True},
                    {"text": "Mesopotamia", "is_correct": False}
                ]},
                {"text": "Who was the first emperor of Rome?", "difficulty": "medium", "options": [
                    {"text": "Julius Caesar", "is_correct": False},
                    {"text": "Augustus", "is_correct": True},
                    {"text": "Nero", "is_correct": False},
                    {"text": "Constantine", "is_correct": False}
                ]},
                {"text": "In which country did the Renaissance begin?", "difficulty": "medium", "options": [
                    {"text": "France", "is_correct": False},
                    {"text": "Italy", "is_correct": True},
                    {"text": "Spain", "is_correct": False},
                    {"text": "England", "is_correct": False}
                ]},
                {"text": "What was the primary cause of the Trojan War?", "difficulty": "hard", "options": [
                    {"text": "The abduction of Helen", "is_correct": True},
                    {"text": "A trade dispute", "is_correct": False},
                    {"text": "A religious conflict", "is_correct": False},
                    {"text": "A territorial dispute", "is_correct": False}
                ]},
                {"text": "Who wrote 'The Art of War'?", "difficulty": "medium", "options": [
                    {"text": "Confucius", "is_correct": False},
                    {"text": "Laozi", "is_correct": False},
                    {"text": "Sun Tzu", "is_correct": True},
                    {"text": "Mencius", "is_correct": False}
                ]},
                {"text": "Which empire was ruled by Genghis Khan?", "difficulty": "easy", "options": [
                    {"text": "The Ottoman Empire", "is_correct": False},
                    {"text": "The Mongol Empire", "is_correct": True},
                    {"text": "The Roman Empire", "is_correct": False},
                    {"text": "The Persian Empire", "is_correct": False}
                ]},
                {"text": "What event marked the beginning of the Middle Ages?", "difficulty": "hard", "options": [
                    {"text": "The fall of the Western Roman Empire", "is_correct": True},
                    {"text": "The crowning of Charlemagne", "is_correct": False},
                    {"text": "The Battle of Hastings", "is_correct": False},
                    {"text": "The signing of the Magna Carta", "is_correct": False}
                ]},
                {"text": "Who discovered the sea route to India from Europe?", "difficulty": "medium", "options": [
                    {"text": "Christopher Columbus", "is_correct": False},
                    {"text": "Ferdinand Magellan", "is_correct": False},
                    {"text": "Vasco da Gama", "is_correct": True},
                    {"text": "James Cook", "is_correct": False}
                ]},
                {"text": "What was the name of the ship that carried the Pilgrims to America?", "difficulty": "easy", "options": [
                    {"text": "The Santa Maria", "is_correct": False},
                    {"text": "The Mayflower", "is_correct": True},
                    {"text": "The Titanic", "is_correct": False},
                    {"text": "The Endeavour", "is_correct": False}
                ]},
                {"text": "In which year did the French Revolution begin?", "difficulty": "medium", "options": [
                    {"text": "1789", "is_correct": True},
                    {"text": "1776", "is_correct": False},
                    {"text": "1812", "is_correct": False},
                    {"text": "1848", "is_correct": False}
                ]}
            ]
        }
    ],
    "Geography": [
        {
            "title": "World Capitals",
            "questions": [
                {"text": "What is the capital of Australia?", "difficulty": "easy", "options": [
                    {"text": "Sydney", "is_correct": False},
                    {"text": "Melbourne", "is_correct": False},
                    {"text": "Canberra", "is_correct": True},
                    {"text": "Perth", "is_correct": False}
                ]},
                {"text": "What is the capital of Brazil?", "difficulty": "easy", "options": [
                    {"text": "Rio de Janeiro", "is_correct": False},
                    {"text": "São Paulo", "is_correct": False},
                    {"text": "Brasília", "is_correct": True},
                    {"text": "Salvador", "is_correct": False}
                ]},
                {"text": "What is the capital of Japan?", "difficulty": "easy", "options": [
                    {"text": "Kyoto", "is_correct": False},
                    {"text": "Osaka", "is_correct": False},
                    {"text": "Tokyo", "is_correct": True},
                    {"text": "Hiroshima", "is_correct": False}
                ]},
                {"text": "What is the capital of Egypt?", "difficulty": "medium", "options": [
                    {"text": "Alexandria", "is_correct": False},
                    {"text": "Cairo", "is_correct": True},
                    {"text": "Giza", "is_correct": False},
                    {"text": "Luxor", "is_correct": False}
                ]},
                {"text": "What is the capital of Argentina?", "difficulty": "medium", "options": [
                    {"text": "Santiago", "is_correct": False},
                    {"text": "Buenos Aires", "is_correct": True},
                    {"text": "Montevideo", "is_correct": False},
                    {"text": "Lima", "is_correct": False}
                ]},
                {"text": "What is the capital of South Korea?", "difficulty": "easy", "options": [
                    {"text": "Busan", "is_correct": False},
                    {"text": "Seoul", "is_correct": True},
                    {"text": "Incheon", "is_correct": False},
                    {"text": "Daegu", "is_correct": False}
                ]},
                {"text": "What is the capital of Nigeria?", "difficulty": "hard", "options": [
                    {"text": "Lagos", "is_correct": False},
                    {"text": "Abuja", "is_correct": True},
                    {"text": "Kano", "is_correct": False},
                    {"text": "Ibadan", "is_correct": False}
                ]},
                {"text": "What is the capital of Switzerland?", "difficulty": "medium", "options": [
                    {"text": "Geneva", "is_correct": False},
                    {"text": "Zurich", "is_correct": False},
                    {"text": "Bern", "is_correct": True},
                    {"text": "Lucerne", "is_correct": False}
                ]},
                {"text": "What is the capital of New Zealand?", "difficulty": "medium", "options": [
                    {"text": "Auckland", "is_correct": False},
                    {"text": "Wellington", "is_correct": True},
                    {"text": "Christchurch", "is_correct": False},
                    {"text": "Queenstown", "is_correct": False}
                ]},
                {"text": "What is the capital of Turkey?", "difficulty": "hard", "options": [
                    {"text": "Istanbul", "is_correct": False},
                    {"text": "Ankara", "is_correct": True},
                    {"text": "Izmir", "is_correct": False},
                    {"text": "Bursa", "is_correct": False}
                ]}
            ]
        }
    ],
    "Literature": [
        {
            "title": "Famous Authors and Books",
            "questions": [
                {"text": "Who wrote 'To Kill a Mockingbird'?", "difficulty": "easy", "options": [
                    {"text": "Harper Lee", "is_correct": True},
                    {"text": "Mark Twain", "is_correct": False},
                    {"text": "Ernest Hemingway", "is_correct": False},
                    {"text": "F. Scott Fitzgerald", "is_correct": False}
                ]},
                {"text": "Which Shakespeare play features the character Hamlet?", "difficulty": "easy", "options": [
                    {"text": "Romeo and Juliet", "is_correct": False},
                    {"text": "Hamlet", "is_correct": True},
                    {"text": "Macbeth", "is_correct": False},
                    {"text": "Othello", "is_correct": False}
                ]},
                {"text": "Who wrote '1984'?", "difficulty": "medium", "options": [
                    {"text": "Aldous Huxley", "is_correct": False},
                    {"text": "George Orwell", "is_correct": True},
                    {"text": "Ray Bradbury", "is_correct": False},
                    {"text": "Kurt Vonnegut", "is_correct": False}
                ]},
                {"text": "What is the pen name of Samuel Clemens?", "difficulty": "medium", "options": [
                    {"text": "Lewis Carroll", "is_correct": False},
                    {"text": "Mark Twain", "is_correct": True},
                    {"text": "Charles Dickens", "is_correct": False},
                    {"text": "Washington Irving", "is_correct": False}
                ]},
                {"text": "Which novel features the character Jay Gatsby?", "difficulty": "hard", "options": [
                    {"text": "The Great Gatsby", "is_correct": True},
                    {"text": "The Sun Also Rises", "is_correct": False},
                    {"text": "Of Mice and Men", "is_correct": False},
                    {"text": "The Grapes of Wrath", "is_correct": False}
                ]},
                {"text": "Who wrote 'Pride and Prejudice'?", "difficulty": "easy", "options": [
                    {"text": "Emily Brontë", "is_correct": False},
                    {"text": "Charlotte Brontë", "is_correct": False},
                    {"text": "Jane Austen", "is_correct": True},
                    {"text": "Mary Shelley", "is_correct": False}
                ]},
                {"text": "In which novel would you find the character Scout?", "difficulty": "medium", "options": [
                    {"text": "The Catcher in the Rye", "is_correct": False},
                    {"text": "To Kill a Mockingbird", "is_correct": True},
                    {"text": "Lord of the Flies", "is_correct": False},
                    {"text": "The Adventures of Huckleberry Finn", "is_correct": False}
                ]},
                {"text": "Who wrote 'The Lord of the Rings'?", "difficulty": "easy", "options": [
                    {"text": "C.S. Lewis", "is_correct": False},
                    {"text": "J.R.R. Tolkien", "is_correct": True},
                    {"text": "George R.R. Martin", "is_correct": False},
                    {"text": "Terry Pratchett", "is_correct": False}
                ]},
                {"text": "What is the name of the fictional detective created by Sir Arthur Conan Doyle?", "difficulty": "easy", "options": [
                    {"text": "Hercule Poirot", "is_correct": False},
                    {"text": "Sherlock Holmes", "is_correct": True},
                    {"text": "Miss Marple", "is_correct": False},
                    {"text": "Philip Marlowe", "is_correct": False}
                ]},
                {"text": "Which author created the character Atticus Finch?", "difficulty": "medium", "options": [
                    {"text": "Truman Capote", "is_correct": False},
                    {"text": "Harper Lee", "is_correct": True},
                    {"text": "Tennessee Williams", "is_correct": False},
                    {"text": "John Steinbeck", "is_correct": False}
                ]}
            ]
        }
    ],
    "Mathematics": [
        {
            "title": "Mathematical Concepts",
            "questions": [
                {"text": "What is the value of π (pi) approximately?", "difficulty": "easy", "options": [
                    {"text": "3.14", "is_correct": True},
                    {"text": "2.71", "is_correct": False},
                    {"text": "1.61", "is_correct": False},
                    {"text": "4.67", "is_correct": False}
                ]},
                {"text": "What is the square root of 144?", "difficulty": "easy", "options": [
                    {"text": "10", "is_correct": False},
                    {"text": "12", "is_correct": True},
                    {"text": "14", "is_correct": False},
                    {"text": "16", "is_correct": False}
                ]},
                {"text": "What is the formula for the area of a circle?", "difficulty": "medium", "options": [
                    {"text": "2πr", "is_correct": False},
                    {"text": "πr²", "is_correct": True},
                    {"text": "4πr²", "is_correct": False},
                    {"text": "πd", "is_correct": False}
                ]},
                {"text": "What is the sum of angles in a triangle?", "difficulty": "easy", "options": [
                    {"text": "90 degrees", "is_correct": False},
                    {"text": "180 degrees", "is_correct": True},
                    {"text": "270 degrees", "is_correct": False},
                    {"text": "360 degrees", "is_correct": False}
                ]},
                {"text": "What is the derivative of x²?", "difficulty": "hard", "options": [
                    {"text": "x", "is_correct": False},
                    {"text": "2x", "is_correct": True},
                    {"text": "x²", "is_correct": False},
                    {"text": "2", "is_correct": False}
                ]},
                {"text": "What is the value of 5!", "difficulty": "medium", "options": [
                    {"text": "20", "is_correct": False},
                    {"text": "60", "is_correct": False},
                    {"text": "120", "is_correct": True},
                    {"text": "240", "is_correct": False}
                ]},
                {"text": "What is the Pythagorean theorem?", "difficulty": "medium", "options": [
                    {"text": "a + b = c", "is_correct": False},
                    {"text": "a² + b² = c²", "is_correct": True},
                    {"text": "a² - b² = c²", "is_correct": False},
                    {"text": "a × b = c²", "is_correct": False}
                ]},
                {"text": "What is the value of e (Euler's number) approximately?", "difficulty": "hard", "options": [
                    {"text": "2.71", "is_correct": True},
                    {"text": "3.14", "is_correct": False},
                    {"text": "1.61", "is_correct": False},
                    {"text": "4.67", "is_correct": False}
                ]},
                {"text": "What is the next number in the sequence: 2, 4, 8, 16, ...?", "difficulty": "easy", "options": [
                    {"text": "20", "is_correct": False},
                    {"text": "24", "is_correct": False},
                    {"text": "32", "is_correct": True},
                    {"text": "64", "is_correct": False}
                ]},
                {"text": "What is the name of a polygon with 8 sides?", "difficulty": "medium", "options": [
                    {"text": "Hexagon", "is_correct": False},
                    {"text": "Heptagon", "is_correct": False},
                    {"text": "Octagon", "is_correct": True},
                    {"text": "Nonagon", "is_correct": False}
                ]}
            ]
        }
    ],
    "Technology": [
        {
            "title": "Tech Innovations",
            "questions": [
                {"text": "Who is the founder of Microsoft?", "difficulty": "easy", "options": [
                    {"text": "Steve Jobs", "is_correct": False},
                    {"text": "Bill Gates", "is_correct": True},
                    {"text": "Mark Zuckerberg", "is_correct": False},
                    {"text": "Elon Musk", "is_correct": False}
                ]},
                {"text": "What does CPU stand for?", "difficulty": "easy", "options": [
                    {"text": "Computer Processing Unit", "is_correct": False},
                    {"text": "Central Processing Unit", "is_correct": True},
                    {"text": "Central Programming Unit", "is_correct": False},
                    {"text": "Computer Programming Unit", "is_correct": False}
                ]},
                {"text": "Which company developed the Android operating system?", "difficulty": "medium", "options": [
                    {"text": "Apple", "is_correct": False},
                    {"text": "Microsoft", "is_correct": False},
                    {"text": "Google", "is_correct": True},
                    {"text": "Samsung", "is_correct": False}
                ]},
                {"text": "What is the main programming language used for Android app development?", "difficulty": "medium", "options": [
                    {"text": "Swift", "is_correct": False},
                    {"text": "JavaScript", "is_correct": False},
                    {"text": "Java", "is_correct": True},
                    {"text": "Python", "is_correct": False}
                ]},
                {"text": "What does HTTP stand for?", "difficulty": "hard", "options": [
                    {"text": "Hyper Text Transfer Protocol", "is_correct": True},
                    {"text": "High Tech Transfer Program", "is_correct": False},
                    {"text": "Hyperlink Text Transmission Process", "is_correct": False},
                    {"text": "Home Tool Transfer Protocol", "is_correct": False}
                ]},
                {"text": "What is the name of Apple's virtual assistant?", "difficulty": "easy", "options": [
                    {"text": "Cortana", "is_correct": False},
                    {"text": "Alexa", "is_correct": False},
                    {"text": "Siri", "is_correct": True},
                    {"text": "Google Assistant", "is_correct": False}
                ]},
                {"text": "Which programming language is primarily used for iOS app development?", "difficulty": "medium", "options": [
                    {"text": "Java", "is_correct": False},
                    {"text": "Python", "is_correct": False},
                    {"text": "Swift", "is_correct": True},
                    {"text": "C++", "is_correct": False}
                ]},
                {"text": "What is the name of the first electronic computer?", "difficulty": "hard", "options": [
                    {"text": "ENIAC", "is_correct": True},
                    {"text": "UNIVAC", "is_correct": False},
                    {"text": "EDVAC", "is_correct": False},
                    {"text": "COLOSSUS", "is_correct": False}
                ]},
                {"text": "What does RAM stand for?", "difficulty": "medium", "options": [
                    {"text": "Random Access Memory", "is_correct": True},
                    {"text": "Read Access Memory", "is_correct": False},
                    {"text": "Rapid Access Memory", "is_correct": False},
                    {"text": "Remote Access Memory", "is_correct": False}
                ]},
                {"text": "Which company developed the JavaScript programming language?", "difficulty": "hard", "options": [
                    {"text": "Microsoft", "is_correct": False},
                    {"text": "Netscape", "is_correct": True},
                    {"text": "Apple", "is_correct": False},
                    {"text": "IBM", "is_correct": False}
                ]}
            ]
        }
    ],
    "Movies": [
        {
            "title": "Cinema Classics",
            "questions": [
                {"text": "Which actor played the lead role in 'The Dark Knight' trilogy?", "difficulty": "easy", "options": [
                    {"text": "Robert Downey Jr.", "is_correct": False},
                    {"text": "Christian Bale", "is_correct": True},
                    {"text": "Chris Evans", "is_correct": False},
                    {"text": "Ryan Reynolds", "is_correct": False}
                ]},
                {"text": "What is the highest-grossing film of all time?", "difficulty": "medium", "options": [
                    {"text": "Avatar", "is_correct": False},
                    {"text": "Avengers: Endgame", "is_correct": True},
                    {"text": "Titanic", "is_correct": False},
                    {"text": "Star Wars: The Force Awakens", "is_correct": False}
                ]},
                {"text": "Which movie won the Academy Award for Best Picture in 2020?", "difficulty": "hard", "options": [
                    {"text": "Joker", "is_correct": False},
                    {"text": "1917", "is_correct": False},
                    {"text": "Parasite", "is_correct": True},
                    {"text": "Once Upon a Time in Hollywood", "is_correct": False}
                ]},
                {"text": "Who directed the movie 'Inception'?", "difficulty": "medium", "options": [
                    {"text": "Steven Spielberg", "is_correct": False},
                    {"text": "Christopher Nolan", "is_correct": True},
                    {"text": "James Cameron", "is_correct": False},
                    {"text": "Quentin Tarantino", "is_correct": False}
                ]},
                {"text": "What is the name of the fictional wizarding school in Harry Potter?", "difficulty": "easy", "options": [
                    {"text": "Beauxbatons", "is_correct": False},
                    {"text": "Durmstrang", "is_correct": False},
                    {"text": "Hogwarts", "is_correct": True},
                    {"text": "Ilvermorny", "is_correct": False}
                ]},
                {"text": "Which movie features the quote 'I'll be back'?", "difficulty": "easy", "options": [
                    {"text": "Die Hard", "is_correct": False},
                    {"text": "The Terminator", "is_correct": True},
                    {"text": "Predator", "is_correct": False},
                    {"text": "Commando", "is_correct": False}
                ]},
                {"text": "Who played Jack Dawson in 'Titanic'?", "difficulty": "easy", "options": [
                    {"text": "Orlando Bloom", "is_correct": False},
                    {"text": "Leonardo DiCaprio", "is_correct": True},
                    {"text": "Matt Damon", "is_correct": False},
                    {"text": "Johnny Depp", "is_correct": False}
                ]},
                {"text": "What is the name of the spaceship in 'Alien'?", "difficulty": "hard", "options": [
                    {"text": "Enterprise", "is_correct": False},
                    {"text": "Nostromo", "is_correct": True},
                    {"text": "Sulaco", "is_correct": False},
                    {"text": "Prometheus", "is_correct": False}
                ]},
                {"text": "Which movie is based on the novel by J.R.R. Tolkien?", "difficulty": "easy", "options": [
                    {"text": "The Chronicles of Narnia", "is_correct": False},
                    {"text": "The Lord of the Rings", "is_correct": True},
                    {"text": "Harry Potter", "is_correct": False},
                    {"text": "The Hobbit", "is_correct": False}
                ]},
                {"text": "Who played Neo in 'The Matrix'?", "difficulty": "easy", "options": [
                    {"text": "Keanu Reeves", "is_correct": True},
                    {"text": "Will Smith", "is_correct": False},
                    {"text": "Johnny Depp", "is_correct": False},
                    {"text": "Brad Pitt", "is_correct": False}
                ]}
            ]
        }
    ],
    "General Knowledge": [
        {
            "title": "Mixed Trivia Challenge",
            "questions": [
                {"text": "What is the largest organ in the human body?", "difficulty": "easy", "options": [
                    {"text": "Heart", "is_correct": False},
                    {"text": "Brain", "is_correct": False},
                    {"text": "Skin", "is_correct": True},
                    {"text": "Liver", "is_correct": False}
                ]},
                {"text": "Which planet is known as the Red Planet?", "difficulty": "easy", "options": [
                    {"text": "Venus", "is_correct": False},
                    {"text": "Mars", "is_correct": True},
                    {"text": "Jupiter", "is_correct": False},
                    {"text": "Saturn", "is_correct": False}
                ]},
                {"text": "What is the chemical symbol for gold?", "difficulty": "medium", "options": [
                    {"text": "Go", "is_correct": False},
                    {"text": "Gd", "is_correct": False},
                    {"text": "Au", "is_correct": True},
                    {"text": "Ag", "is_correct": False}
                ]},
                {"text": "Which country is known as the Land of the Rising Sun?", "difficulty": "medium", "options": [
                    {"text": "China", "is_correct": False},
                    {"text": "Thailand", "is_correct": False},
                    {"text": "Japan", "is_correct": True},
                    {"text": "South Korea", "is_correct": False}
                ]},
                {"text": "What is the tallest mammal?", "difficulty": "easy", "options": [
                    {"text": "Elephant", "is_correct": False},
                    {"text": "Giraffe", "is_correct": True},
                    {"text": "Hippopotamus", "is_correct": False},
                    {"text": "Rhino", "is_correct": False}
                ]},
                {"text": "Which element has the atomic number 1?", "difficulty": "hard", "options": [
                    {"text": "Helium", "is_correct": False},
                    {"text": "Oxygen", "is_correct": False},
                    {"text": "Hydrogen", "is_correct": True},
                    {"text": "Carbon", "is_correct": False}
                ]},
                {"text": "What is the largest ocean on Earth?", "difficulty": "easy", "options": [
                    {"text": "Atlantic Ocean", "is_correct": False},
                    {"text": "Indian Ocean", "is_correct": False},
                    {"text": "Pacific Ocean", "is_correct": True},
                    {"text": "Arctic Ocean", "is_correct": False}
                ]},
                {"text": "Which gas makes up about 78% of Earth's atmosphere?", "difficulty": "medium", "options": [
                    {"text": "Oxygen", "is_correct": False},
                    {"text": "Carbon Dioxide", "is_correct": False},
                    {"text": "Nitrogen", "is_correct": True},
                    {"text": "Argon", "is_correct": False}
                ]},
                {"text": "How many bones are in an adult human body?", "difficulty": "medium", "options": [
                    {"text": "206", "is_correct": True},
                    {"text": "256", "is_correct": False},
                    {"text": "306", "is_correct": False},
                    {"text": "156", "is_correct": False}
                ]},
                {"text": "Which is the smallest country in the world?", "difficulty": "hard", "options": [
                    {"text": "Monaco", "is_correct": False},
                    {"text": "Vatican City", "is_correct": True},
                    {"text": "San Marino", "is_correct": False},
                    {"text": "Liechtenstein", "is_correct": False}
                ]}
            ]
        }
    ]
}

# --- Population script ---
def populate_data():
    """
    Populates the database with categories, quizzes, questions, and options.
    """
    print("Starting data population...")
    
    # Create categories
    categories = {}
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data["name"],
            defaults={'description': cat_data["description"]}
        )
        categories[cat_data["name"]] = category
        if created:
            print(f"Created category: {category.name}")

    # Create quizzes, questions, and options
    for category_name, quizzes in quizzes_data.items():
        category = categories.get(category_name)
        if not category:
            print(f"Warning: Category '{category_name}' not found. Skipping quizzes.")
            continue
            
        for quiz_data in quizzes:
            quiz, created = Quiz.objects.get_or_create(
                title=quiz_data["title"],
                category=category,
                defaults={'description': quiz_data.get('description', '')}
            )
            
            if created:
                print(f"  Creating quiz: {quiz.title}")
                for q_data in quiz_data["questions"]:
                    question = Question.objects.create(
                        quiz=quiz,
                        text=q_data["text"],
                        difficulty=q_data["difficulty"]
                    )
                    
                    for opt_data in q_data["options"]:
                        Option.objects.create(
                            question=question,
                            text=opt_data["text"],
                            is_correct=opt_data["is_correct"]
                        )
                print(f"    Added {len(quiz_data['questions'])} questions to '{quiz.title}'")
            else:
                print(f"  Quiz '{quiz.title}' already exists. Skipping.")

    print("Data population complete!")

if __name__ == '__main__':
    # Clear existing data before populating
    clear_data()
    # Populate the database
    populate_data()