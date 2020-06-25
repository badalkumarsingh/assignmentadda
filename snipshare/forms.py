from django import forms
from .models import Snip
class snipForm(forms.ModelForm):
    class Meta:
        model=Snip
        fields=('text','title','lang')
        labels={'title':'Snippet Title','text':'New Snippet','lang': 'Syntax Highlighting'}