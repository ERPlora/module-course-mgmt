from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description', 'duration_hours', 'price', 'max_students', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'code': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'description': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
            'duration_hours': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'price': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'max_students': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'toggle'}),
        }

