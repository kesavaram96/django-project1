from app.models import user
from django import forms

class userForm(forms.ModelForm):
    class Meta:
        Model=user
        fields=[
            'UId','UName','EMail','password'
        ]