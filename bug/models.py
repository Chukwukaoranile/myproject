from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here
class Bug(models.Model):
    BUG_TYPES = [
        ('error', 'Error'),
        ('feature', 'New Feature'),
        ('enhancement', 'Enhancement'),
        ('other', 'Other'),

    ]

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),

    ]

    description = models.TextField()
    bug_type = models.CharField(max_length=35, choices=BUG_TYPES, default='error')
    report_date = models.DateField(default=datetime.now)
    status = models.CharField(max_length=35, choices=STATUS_CHOICES, default='todo')

    def __str__(self):
        return self.description
