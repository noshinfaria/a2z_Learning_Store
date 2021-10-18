from django import forms
from .models import Reply, Question


class QuestionForm(forms.ModelForm):
    question = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        })
    )

    class Meta:
        model = Question
        fields = ['question']


class ReplyForm(forms.ModelForm):
    reply = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        })
    )

    class Meta:
        model = Reply
        fields = ['reply']

