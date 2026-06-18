from django.db import models
from students.models import Student
from courses.models import Course

class Exam(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    marks = models.IntegerField()

    exam_date = models.DateField()

    def __str__(self):
        return f"{self.student.full_name} - {self.marks}"
