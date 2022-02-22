from datetime import datetime
from django.db import models


# Create your models here.
class resume(models.Model):
    id = models.AutoField(primary_key=True)
    cv_template = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=14, blank=False)
    career_objective = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    address = models.TextField(blank=True)
    hobbies = models.TextField(blank=True)
    created_on = models.DateTimeField(default=datetime.now, blank=True)