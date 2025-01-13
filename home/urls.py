from django.urls import path
from .views import home_view, school_directory_page


urlpatterns = [
    path('', home_view, name='home'),
    path('schools/', school_directory_page, name='schools')
]


