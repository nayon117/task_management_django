from django.db import models
from django.db.models import CASCADE

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


# project model
class Project(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField()


# task model
class Task (models.Model):
    project = models.ForeignKey(Project, 
                                on_delete = models.CASCADE, 
                                default = 1)
    assigned_to = models.ManyToManyField(Employee)
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# task detail model
class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    assigned_to = models.CharField(max_length=250)
    task = models.OneToOneField(Task, on_delete = models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_OPTIONS, default='MEDIUM')



