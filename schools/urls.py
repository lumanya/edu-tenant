from django.urls import path

from .views import StudentRegistrationView, list_students


urlpatterns = [
    path('create-student/', StudentRegistrationView.as_view(), name='create-student'),
    path('', list_students, name='school')
]