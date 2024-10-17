from django import forms
from RDS.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'exposure', 'mode', 'state', 'dist', 'position', 'content']
        labels = {
            'subject': 'Band',
            'exposure': "exposure",
            'mode' : 'mode',
            'state' : 'state',
            'dist' : 'dist',
            'position' : 'position',
            'content': '내용',
        } 

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }