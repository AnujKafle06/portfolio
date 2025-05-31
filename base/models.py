from django.db import models
from django.db import connections




# Create your models here.

from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='base/')
    SKILL_CHOICES = (
        ('1', 'Python'),
        ('2', 'HTML'),
        ('3', 'CSS'),
        ('4', 'Django'),
        ('5', 'Tailwind'),
        ('6', 'WordPress'),
    )
    skill_id = models.CharField(max_length=1, primary_key=True, choices=SKILL_CHOICES)

    def __str__(self):
        return self.name


connections['default'].cursor()

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio')
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    purpose = models.TextField()

    def __str__(self):
        return self.name