from django import forms
from .models import Member
from django.core.validators import RegexValidator

FRUIT_CHOICES= [
    (False, "Regular - Can't delete members"),
    (True, 'Can delete members'),
]

class MemberForm(forms.ModelForm):
    first_name = forms.CharField(required = True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Phone number'}),
        validators=[
            RegexValidator(
                regex="^\d{10}?$",
                message='Enter 10 digit phone number',
                code='invalid_phone_number'
            ),
    ],
    )
    role = forms.ChoiceField(label='Role', required = True, initial=False, choices=FRUIT_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'phone', 'role']
