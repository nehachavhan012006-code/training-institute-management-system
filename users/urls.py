from django.urls import path
from .views import (
    login_view,
    trainer_dashboard,
    student_dashboard
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('trainer-dashboard/', trainer_dashboard, name='trainer_dashboard'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
]