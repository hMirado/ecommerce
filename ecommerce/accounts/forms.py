from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120, required=True)
    password = forms.CharField( widget=forms.PasswordInput(), max_length=120, required=True)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Are you sure you are registered? We cannot find in this user.")
        return username

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Invalid Password")
        elif user is None:
            pass
        else:
            return password

