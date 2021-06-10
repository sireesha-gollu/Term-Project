from django.forms import ModelForm
from django import forms
from . models import exam_table

class ExamForm(forms.ModelForm):
    class Meta:
        model = exam_table
        fields = ('Faculty_name' , 'Subject' , 'Exam' , 'Upload')
