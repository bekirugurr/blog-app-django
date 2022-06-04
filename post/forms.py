from .models import  Post, Comment
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'post_pic', 'category', 'status')
        labels = {'post_pic': 'Image'}
        widgets = {
                'title': forms.TextInput(attrs={'placeholder': '🥚 Enter post title',  'style':'margin:  1rem 0; padding: .5rem 1rem;  border-color: #0D6EFD;'}),
                'content': forms.Textarea(attrs={'placeholder': '🐣 → 🐓 → 🍗 \n Enter post content', 'class': 'input-style', 'rows' :7, 'style':'margin: 1rem 0; padding: .5rem 1rem;  border-color: #0D6EFD;' }),
                'category': forms.Select(attrs={'style' : 'padding: .5rem 1rem; border-color: #0D6EFD; width: 16rem'}),
                'status': forms.Select(attrs={'style':'margin: 1rem 0; padding: .5rem;  border-color: #0D6EFD;'}),
                'post_pic': forms.ClearableFileInput(attrs={ 'style':'margin-top: 1rem 0; padding: .5rem 0;  border-color: #0D6EFD;' }),
            } 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        labels = {'content': 'Comment'}
        widgets = {
                'content': forms.Textarea(attrs={'placeholder': '  🙉 🙊 🙊 \nMake a comment about the post ', 'class': 'input-style', 'rows' :7, 'style':'resize: none; margin: 1rem 0; padding: .5rem 1rem;  border-color: #0D6EFD;' }),
            } 
