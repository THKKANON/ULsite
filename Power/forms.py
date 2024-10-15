from django import forms
from Power.models import Post_Band

class Post_BandForm(forms.ModelForm):
    class Meta:
        model = Post_Band
        fields = ['subject']
        labels = {
            'subject': 'Band',
        } 