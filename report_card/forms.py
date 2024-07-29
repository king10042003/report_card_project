from django import forms
from .models import Student

CLASS_CHOICES = [
    ('8th', '8th'),
    ('9th', '9th'),
    ('10th', '10th'),
    ('11th JEE', '11th JEE'),
    ('11th NEET', '11th NEET'),
    ('12th JEE', '12th JEE'),
    ('12th NEET', '12th NEET'),
]

class StudentForm(forms.ModelForm):
    class_name = forms.ChoiceField(choices=CLASS_CHOICES, required=True)
    
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'class_name']


class MarkForm(forms.Form):
    subject = forms.ChoiceField(choices=[])  # Choices will be set dynamically
    marks_obtained = forms.IntegerField(required=False)
    total_marks = forms.IntegerField(required=False)
    test_date = forms.DateField(required=False)  # If you are using this field



