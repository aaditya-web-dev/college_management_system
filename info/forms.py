from django import forms
from .models import Assignment, Submissions

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = ['file']
