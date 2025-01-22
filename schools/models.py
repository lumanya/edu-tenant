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
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True,
                                related_name='classes')
    
    def __str__(self):
        return f"{self.name} {self.section}"
    
class Subject(models.Model):
    name = models.CharField(max_length=50)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subjects')
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):   
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subjects')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='students')
    
    class Meta:
        unique_together = ('student', 'subject')
        
    def __str__(self):
        return f"{self.student} - {self.subject}"
    
    
class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')
    exam_date = models.DateField()
    total_marks = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Exam for {self.subject} on {self.exam_date} "
    
class Grade(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    marks_scored = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.student} - {self.exam} - {self.marks_scored}"