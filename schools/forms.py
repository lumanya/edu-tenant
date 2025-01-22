from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'course', 'gender', 'age']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border-4 border-gray-300 rounded-lg focus:ring-red-500 focus:border-sky-500 shadow-sm',
                'placeholder': 'Full Name..'
            }),
            'course': forms.TextInput(attrs={
                'class': 'w-full p-2 border-4 border-gray-300 rounded-lg focus:ring-red-500 focus:border-sky-500 shadow-sm',
                'placeholder': 'Course ..'
            }),
            'gender': forms.Select(attrs={
                'class': 'w-full p-2 border-4 border-gray-300 rounded-lg focus:ring-red-500 focus:border-sky-500 shadow-sm',
             }),
            'age': forms.NumberInput(attrs={
                'class': 'w-full p-2 border-4 border-gray-300 rounded-lg focus:ring-red-500 focus:border-sky-500 shadow-sm',
                'placeholder': 'Age ..'
            }),
        }
        
        labels = {
            'name': '',
            'course': '',
            'gender': '',
            'age': ''
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'phone', 'email']
        

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'section', 'teacher']
        

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'class_assigned']
        
        
class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['subject', 'exam_date', 'total_marks']
        
        
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['exam', 'student', 'marks_scored']