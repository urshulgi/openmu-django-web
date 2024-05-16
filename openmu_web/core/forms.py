from django import forms


class LoginForm(forms.Form):
    template_name = "login_form_snippet.html"
    user = forms.CharField(min_length=4, max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
