from django.db import models
from students.models import Student
from trainers.models import Trainer

class Feedback(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

    def __str__(self):
        return f"{self.student.full_name} - {self.rating}"