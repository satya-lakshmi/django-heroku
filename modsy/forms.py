from django import forms
from django.contrib.auth.models import User
from . models import project
from . models import room
from . models import goal
from . models import design
from . models import furniture
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email
            raise forms.ValidationError('This email address is already in use.')
class UserRequirementForm(forms.ModelForm):
    class Meta:
        model = project
        fields=('room','goal','design','furniture')
        error_messages = {
            'room': {
                'required': "Please select any of the room in the first step",
            },
            'goal': {
                'required': "Please select any of the goals in the second step",
            },
            'design': {
                'required': "Please select any of the design in the forth step",
            },
            'furniture': {
                'required': "Please select any of the furniture in the third step",
            },
        }
class EditProfileForm(UserChangeForm):
    template_name='edit_profile'

    class Meta:
        model = User
        fields = ('username','email','password',)