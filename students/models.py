from django.db import models
from courses.models import Course

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    course = models.ForeignKey(
    Course,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    admission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name