from django import forms
from user.models import User


class UserForm(forms.ModelForm):
    login_auth_str = forms.CharField(max_length=100,
                                     widget=forms.PasswordInput,
                                     label='口令')
    class Meta:
        model = User
        fields = '__all__'