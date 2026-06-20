from django.db import models
from users.models import User

class Trainer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    specialization = models.CharField(max_length=100, null=True, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True)

    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
