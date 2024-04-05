from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = (
            "username",
            "email",
            "name",
        )

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 为用户名字段添加初始的 CSS 类
        self.fields['username'].widget.attrs['class'] = 'form-control'
        
        # 为密码字段添加初始的 CSS 类
        self.fields['password'].widget.attrs['class'] = 'form-control'

        # 为用户名字段添加 placeholder 属性
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        
        # 为密码字段添加 placeholder 属性
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your password'