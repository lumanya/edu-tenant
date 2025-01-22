from django.contrib import admin

from .models import Student, Class, Exam, Subject, Grade, Teacher


admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Exam)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Grade)
