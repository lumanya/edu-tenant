from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *

@login_required
def list_students(request):
    students = Student.objects.all()
    
    context = {
        'students': students,
    }
    return render(request, 'home_tenant.html', context)

class StudentRegistrationView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm    
    template_name = 'student_registration.html'
    success_url = reverse_lazy('school')
    
    
class TeacherRegistrationView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher_reg_form.html'
    success_url = reverse_lazy('school')
    


class ClassRgeistraionView(LoginRequiredMixin, CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'class_reg_form.html'
    success_url = reverse_lazy('school')
    
class SubjectRegistrationView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject_add_form.html'
    success_url = reverse_lazy('school')
    
    
class ExamRegistrationView(LoginRequiredMixin, CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'exam_add_form.html'
    success_url = reverse_lazy('school')
    
    
class GradeRegistrationView(LoginRequiredMixin, CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'grade_add_form.html'
    success_url = reverse_lazy('school')
    