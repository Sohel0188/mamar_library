from django import forms
from books.models import Review

# class PostForm(forms.ModelForm):
#     class Meta: 
#         model = Review
        # fields = '__all__'
        # exclude = ['author']
        
class ReviewForm(forms.ModelForm):
    class Meta: 
        model = Review
        fields = ['name', 'body']