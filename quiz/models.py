from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=500)
    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.text} ({'correct' if self.is_correct else 'wrong'})"
