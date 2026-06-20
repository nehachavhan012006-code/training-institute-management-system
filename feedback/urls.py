from django.urls import path

from .views import (
    feedback_list,
    add_feedback,
    edit_feedback,
    delete_feedback
)

urlpatterns = [

    path(
        'feedback/',
        feedback_list,
        name='feedback_list'
    ),

    path(
        'feedback/add/',
        add_feedback,
        name='add_feedback'
    ),

    path(
        'feedback/edit/<int:id>/',
        edit_feedback,
        name='edit_feedback'
    ),

    path(
        'feedback/delete/<int:id>/',
        delete_feedback,
        name='delete_feedback'
    ),
]