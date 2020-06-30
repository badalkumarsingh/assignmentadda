from django import forms
from .models import Snip
class snipForm(forms.ModelForm):
    class Meta:
        model=Snip
        fields=('text','title','lang','theme','lines')
        labels={'title':'Snippet Title','text':'New Snippet','lang': 'Syntax Highlighting','theme': 'Choose Themes'}