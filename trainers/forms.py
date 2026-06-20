from django import forms
from .models import Trainer

class TrainerForm(forms.ModelForm):

    class Meta:
        model = Trainer

        fields = [
            'user',
            'full_name',
            'email',
            'phone',
            'specialization',
            'experience',
            'availability_status'
        ]