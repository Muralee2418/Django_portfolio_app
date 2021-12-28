from django import forms
from .models import comments

class commentforms(forms.ModelForm):
    class Meta:
        model=comments
        fields=['comment_info']