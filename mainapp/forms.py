from django import forms
from django.db.models import fields
from .models import Artist, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
