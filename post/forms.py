from .models import  Post, Category
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'post_pic', 'status')
        labels = {'post_pic': 'Image'}
        widgets = {
                'title': forms.TextInput(attrs={'placeholder': '🥚 Enter post title',  'style':'margin:  1rem 0; padding: .5rem 1rem;  border-color: #0D6EFD;'}),
                'content': forms.Textarea(attrs={'placeholder': '🐣 → 🐓 → 🍗 \n Enter post content', 'class': 'input-style', 'rows' :7, 'style':'margin: 1rem 0; padding: .5rem 1rem;  border-color: #0D6EFD;' }),
                'status': forms.Select(attrs={'style':'margin: 1rem 0; padding: .5rem;  border-color: #0D6EFD;'}),
                'post_pic': forms.ClearableFileInput(attrs={ 'style':'margin-top: 1rem 0; padding: .5rem 0;  border-color: #0D6EFD;' }),
            } 


class PostCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
                'category': forms.Select(attrs={'style' : 'padding: .5rem 1rem; border-color: #0D6EFD; width: 16rem'}),
            } 
