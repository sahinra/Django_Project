from django import forms
from .models import Participants


class RegisterForm(forms.ModelForm):
    firstName = forms.CharField(required=True,
                                widget=forms.TextInput(
                                    attrs={
                                        'pattern': '[A-Za-z ]+',
                                    }
                                ),
                                error_messages={
                                    'required': 'Please enter your name!',
                                    'pattern': 'Please enter only letters!'
                                },
                                ),
    lastName = forms.CharField(required=True,
                               widget=forms.TextInput(
                                    attrs={
                                        'pattern': '[A-Za-z ]+',
                                    }
                               ),
                               error_messages={
                                    'required': 'Please enter your last name!',
                                    'pattern': 'Please enter only letters!'
                               },
                               )
    title = forms.CharField(required=False)

    class Meta:
        model = Participants
        fields = [
            'firstName',
            'lastName',
            'title',
        ]

