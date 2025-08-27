from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Category, Quiz, Question, Option, QuizAttempt

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4
    fields = ('text', 'is_correct')
    ordering = ('text',)

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    fields = ('text', 'difficulty', 'points')
    inlines = [OptionInline]
    ordering = ('text',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'quiz_count', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('name',)
    
    def quiz_count(self, obj):
        return obj.quizzes.count()
    quiz_count.short_description = 'Number of Quizzes'

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'question_count', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    inlines = [QuestionInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'category')
        }),
        ('Settings', {
            'fields': ('is_active', 'time_limit'),
            'classes': ('collapse',)
        }),
    )
    
    def question_count(self, obj):
        return obj.questions.count()
    question_count.short_description = 'Number of Questions'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'difficulty', 'points')
    list_filter = ('quiz__category', 'quiz', 'difficulty')
    search_fields = ('text',)
    ordering = ('quiz', 'text')
    inlines = [OptionInline]
    fieldsets = (
        (None, {
            'fields': ('quiz', 'text')
        }),
        ('Settings', {
            'fields': ('difficulty', 'points'),
        }),
    )

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('is_correct', 'question__quiz__category', 'question__quiz')
    search_fields = ('text',)
    ordering = ('question', 'text')

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'max_score', 'percentage', 'completed_at')
    list_filter = ('quiz__category', 'quiz', 'completed_at')
    search_fields = ('user__username', 'quiz__title')
    ordering = ('-completed_at',)
    readonly_fields = ('user', 'quiz', 'score', 'max_score', 'percentage', 'completed_at', 'time_taken')
    
    def has_add_permission(self, request):
        return False  # Prevent adding attempts manually
    
    def has_change_permission(self, request, obj=None):
        return False  # Prevent changing attempts

# Extend UserAdmin to show additional info
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('quiz_attempts_count',)
    
    def quiz_attempts_count(self, obj):
        return obj.quiz_attempts.count()
    quiz_attempts_count.short_description = 'Quiz Attempts'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
