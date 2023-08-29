from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description', 'funding_goal', 'allowed_donors', 'category', 'image', 'video']


        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['title'].widget.attrs['class'] = 'input'
            self.fields['title'].widget.attrs['placeholder'] = 'Title'
            self.fields['description'].widget.attrs['class'] = 'input'
            self.fields['description'].widget.attrs['placeholder'] = 'Description'
            self.fields['funding_goal'].widget.attrs['class'] = 'input'
            self.fields['funding_goal'].widget.attrs['placeholder'] = 'Funding Goal'
            self.fields['allowed_donors'].widget.attrs['class'] = 'input'
            self.fields['allowed_donors'].widget.attrs['placeholder'] = 'Allowed Donors'
            self.fields['category'].widget.attrs['class'] = 'select'
            self.fields['image'].widget.attrs['class'] = 'input-file'
            self.fields['video'].widget.attrs['class'] = 'input-file'


