from django.db import models


class Student(models.Model):
    """Student Registration"""
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    name = models.CharField(max_length=120)
    course = models.CharField()
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, default='Male')
    create_date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name        

#Academic Management models
class Class(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10, blank=True, null=True)
    