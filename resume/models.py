from django.db import models

# Create your models here.
class Profile(models.Model):
    objective = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField(blank=True,null=True)

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_ongoing = models.BooleanField(default=False)
    grade = models.CharField(max_length=10, blank=True)

class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    is_ongoing = models.BooleanField(default=False)
    end_date = models.DateField(blank=True,null=True)
    description = models.TextField()

class Skills(models.Model):
    skill = models.CharField(max_length=100)
    level = models.CharField(max_length=10)

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    link = models.URLField(blank=True)

class Courses(models.Model):
    course_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=100, blank=True)
    certificate_link = models.URLField(blank=True)
    organization = models.CharField(max_length=100, blank=True)
    
