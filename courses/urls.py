from django.urls import path

from .views import (
    course_list,
    add_course,
    edit_course,
    delete_course
)

urlpatterns = [

    path(
        'courses/',
        course_list,
        name='course_list'
    ),

    path(
        'courses/add/',
        add_course,
        name='add_course'
    ),

    path(
        'courses/edit/<int:id>/',
        edit_course,
        name='edit_course'
    ),

    path(
        'courses/delete/<int:id>/',
        delete_course,
        name='delete_course'
    ),
]