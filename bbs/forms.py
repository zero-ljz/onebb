from django import forms

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

