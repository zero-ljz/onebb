from django import forms

from .models import Collect, Comment, Follow, Like, Log, Message, Notification, Option, Permission, Post, Role, Tag
from accounts.models import User

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    mail = forms.EmailField()

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','content_html','tags'] # fields = '__all__' # exclude 和 fields 二选一
        

    # def __init__(self, *args, **kwargs):
    #     self.author = kwargs.pop('author')
    #     super(PostCreateForm, self).__init__(*args, **kwargs)

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if Post.objects.filter(user=self.user, title=title).exists():
    #         raise forms.ValidationError("你已经写了一本同名的书。")
    #     return title


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    #parent_comment_id = forms.IntegerField(widget=forms.HiddenInput, required=False)