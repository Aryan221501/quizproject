from rest_framework import serializers
from .models import Category, Quiz, Question, Option, QuizAttempt

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'is_correct']
        read_only_fields = ['is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'difficulty', 'options']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'category', 'created_at', 'questions']

class CategorySerializer(serializers.ModelSerializer):
    quizzes = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'quizzes']
    
    def get_quizzes(self, obj):
        # Only include active quizzes
        active_quizzes = obj.quizzes.filter(is_active=True)
        return QuizSerializer(active_quizzes, many=True).data

class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'score', 'completed_at']
        read_only_fields = ['user']