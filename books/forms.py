from django import forms
from .models import BookModel,Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields= '__all__'
        
        
class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ['name','email','body']