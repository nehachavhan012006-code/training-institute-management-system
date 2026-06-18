from django.db import models

class Trainer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    specialization = models.CharField(max_length=100, null=True, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True)

    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
