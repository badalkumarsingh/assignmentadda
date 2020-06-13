from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.TextInput(attrs={'class':'form-control display-7'})}
        
class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        fields = ['text','img']
        lables = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80,'class':'form-control display-7'})}
    
