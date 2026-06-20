from django.urls import path
from .views import (
    exam_list,
    add_exam,
    edit_exam,
    delete_exam,
    result_list
)

from .views import (
    exam_list,
    add_exam,
    edit_exam,
    delete_exam
)

urlpatterns = [

    path(
        'exams/',
        exam_list,
        name='exam_list'
    ),

    path(
        'exams/add/',
        add_exam,
        name='add_exam'
    ),

    path(
        'exams/edit/<int:id>/',
        edit_exam,
        name='edit_exam'
    ),

    path(
        'exams/delete/<int:id>/',
        delete_exam,
        name='delete_exam'
    ),

    path(
    'results/',
    result_list,
    name='result_list'
),
]