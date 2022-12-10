from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from base.models import (User)

class SetPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        # fields = ['new_password1', 'new_password2']
        fields = '__all__'

