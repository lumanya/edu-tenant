from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Student
from .forms import StudentForm

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