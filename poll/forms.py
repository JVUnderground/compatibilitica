from django.forms import ModelForm, NumberInput
from .models import Answer

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ['question']
        widgets = {
            'social': NumberInput(attrs={'type': 'range', 'min': '-100', 'max': '100'}),
            'economic': NumberInput(attrs={'type': 'range', 'min': '-100', 'max': '100'}),
        }