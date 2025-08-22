from django.db import models

# Create your models here.

class Course(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)  # e.g., "6 weeks", "10 hours"
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.title
