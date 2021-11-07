from django import forms
from webapi.models import Advisors_DB,Booking_DB
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username',  'password',]
        # fields = ['first_name', 'last_name', 'username', 'password']


# class UserLoginForm(forms.ModelForm):
#     def clean_esal(self):
#         inputsal=self.cleaned_data['esal']
#         if inputsal<5000:
#             raise forms.validationError('The minimum salary should be 5000')
#         return inputsal
#
#
#     class Meta:
#         model=Employee
#         fields='__all__'
