from django.urls import path

from .views import *


urlpatterns = [
    path('create-student/', StudentRegistrationView.as_view(), name='create-student'),
    path('create-teacher/', TeacherRegistrationView.as_view(), name='create_teacher'),
    path('create-class/', ClassRgeistraionView.as_view(), name='create-class'),
    path('create-subject/', SubjectRegistrationView.as_view(), name='create-subject'),
    path('create-exam/', ExamRegistrationView.as_view(), name='create-exam'),
    path('create-grade/', GradeRegistrationView.as_view(), name='create-grade'),
    path('', list_students, name='school')
]