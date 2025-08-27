# QuizMaster - Advanced Quiz Application

QuizMaster is a Django-based quiz application that allows users to create, take, and track quizzes. The application includes user authentication, quiz management, scoring, leaderboard features, and a REST API for integration with other systems.

![QuizMaster Dashboard](screenshots/dashboard.png)

## Features

- **User Authentication**: Secure registration and login system
- **Quiz Categories**: Organize quizzes by topics (Science, History, Geography, etc.)
- **Quiz Management**: Create quizzes with multiple choice questions and difficulty levels
- **Scoring System**: Automatic scoring with detailed results
- **Quiz History**: Track all quiz attempts with scores and dates
- **Leaderboard**: See how you rank against other users
- **User Profiles**: Personalized dashboard with statistics and progress tracking
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Dark Theme**: Modern dark UI with smooth animations
- **REST API**: Comprehensive API for quiz operations
- **Performance Optimizations**: Caching, database indexing, and query optimization
- **Security Features**: Rate limiting, CSRF protection, and secure headers

## Technologies Used

- Python 3.8+
- Django 4.2
- Django REST Framework 3.14.0
- Bootstrap 5.3 (Frontend Framework)
- Chart.js (Data Visualization)
- SQLite (Default database)
- HTML5/CSS3/JavaScript (Frontend)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd quizproject
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Navigate to `http://127.0.0.1:8000/` in your browser
2. Register for a new account or login with existing credentials
3. Browse available quizzes by category
4. Take quizzes and view your detailed results
5. Check the leaderboard to see how you rank against other users
6. View your profile dashboard with statistics and progress charts
7. Access your quiz history to review past attempts

## Project Structure

```
quizproject/
├── quiz/                     # Main application
│   ├── models.py            # Data models (Category, Quiz, Question, etc.)
│   ├── views.py             # Frontend views
│   ├── views_api.py         # API views
│   ├── views_auth.py        # Authentication views
│   ├── urls.py              # URL routing
│   ├── forms.py             # User registration form
│   ├── serializers.py       # API serializers
│   ├── middleware.py        # Custom middleware (rate limiting)
│   ├── templates/           # HTML templates
│   │   └── quiz/            # Template files
│   └── static/              # Static files (CSS, JS, images)
├── quizproject/             # Project settings
│   ├── settings.py          # Configuration
│   └── urls.py              # Main URL routing
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── db.sqlite3               # SQLite database file
```

## Data Models

### Category
- `name`: Unique category name
- `description`: Description of the category
- `created_at`: Timestamp of creation

### Quiz
- `title`: Quiz title
- `description`: Description of the quiz
- `category`: Foreign key to Category
- `is_active`: Boolean to enable/disable quiz
- `time_limit`: Time limit in minutes (0 for no limit)
- `created_at`: Timestamp of creation

### Question
- `quiz`: Foreign key to Quiz
- `text`: Question text
- `difficulty`: Easy, Medium, or Hard
- `points`: Points awarded for correct answer
- `created_at`: Timestamp of creation

### Option
- `question`: Foreign key to Question
- `text`: Option text
- `is_correct`: Boolean indicating correct answer

### QuizAttempt
- `user`: Foreign key to User
- `quiz`: Foreign key to Quiz
- `score`: User's score
- `max_score`: Maximum possible score
- `percentage`: Percentage score
- `completed_at`: Timestamp of completion
- `time_taken`: Time taken in seconds

## API Endpoints

- `GET /api/categories/` - List all categories
- `GET /api/categories/<id>/` - Get details for a specific category
- `GET /api/quizzes/` - List all active quizzes
- `GET /api/quizzes/<id>/` - Get details for a specific quiz
- `POST /api/quizzes/<id>/submit/` - Submit answers for a quiz
- `GET /api/attempts/` - List authenticated user's quiz attempts
- `POST /api/attempts/` - Create a new quiz attempt

## Security Features

- User authentication and session management
- Rate limiting middleware to prevent abuse
- Secure HTTP headers (XSS protection, content type sniffing protection)
- CSRF protection on forms
- SQL injection prevention through Django ORM
- Password validation and encryption
- HTTPS configuration options

## Performance Optimizations

- Database indexing on frequently queried fields
- Query optimization with `select_related` and `prefetch_related`
- Caching for homepage data (5-minute cache)
- Pagination for lists (12 quizzes per page, 10 attempts per page)
- Database connection pooling
- QuerySet optimization to prevent N+1 queries

## UI/UX Features

- Responsive design with Bootstrap 5
- Dark theme with custom styling
- Interactive charts using Chart.js
- Smooth animations and hover effects
- Mobile-friendly navigation
- Loading states and feedback
- Form validation

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Development

To run tests:
```bash
python manage.py test
```

To collect static files (in production):
```bash
python manage.py collectstatic
```

## Configuration

Key settings in `quizproject/settings.py`:
- Database configuration (SQLite by default)
- Cache configuration (in-memory cache)
- Security settings (HTTPS, HSTS, etc.)
- Static files configuration
- Logging configuration
- REST Framework throttling rates

## Screenshots

![Quiz List](screenshots/quiz-list.png)
*Browse quizzes by category*

![Quiz Taking](screenshots/quiz-taking.png)
*Interactive quiz interface*

![Results](screenshots/results.png)
*Detailed quiz results*

![Leaderboard](screenshots/leaderboard.png)
*Top performers ranking*

![Profile](screenshots/profile.png)
*User dashboard with statistics*