from django.forms import ModelForm
from .models import animalabuse

class SubmitForm(ModelForm):
    class Meta:
        model = animalabuse
        exclude = ('Address', 'DOB','expirationdate','image')