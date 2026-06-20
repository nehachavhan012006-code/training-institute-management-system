from django.urls import path
from .views import student_list, add_student
from .views import (
    student_list,
    add_student,
    edit_student,
    delete_student
)

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/add/', add_student, name='add_student'),
    path(
    'students/edit/<int:id>/',
    edit_student,
    name='edit_student'
),

path(
    'students/delete/<int:id>/',
    delete_student,
    name='delete_student'
),
]