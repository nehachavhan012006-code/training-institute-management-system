from django.urls import path

from .views import (
    trainer_list,
    add_trainer,
    edit_trainer,
    delete_trainer
)

urlpatterns = [

    path(
        'trainers/',
        trainer_list,
        name='trainer_list'
    ),

    path(
        'trainers/add/',
        add_trainer,
        name='add_trainer'
    ),

    path(
        'trainers/edit/<int:id>/',
        edit_trainer,
        name='edit_trainer'
    ),

    path(
        'trainers/delete/<int:id>/',
        delete_trainer,
        name='delete_trainer'
    ),
]