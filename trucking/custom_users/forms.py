import requests
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django import forms


class UserEditForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('name', 'address', 'email', 'bank_account', 'unp', 'contract_1', 'contract_2')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm text-center',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control form-control-sm text-center',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-sm text-center',
                'readonly': True,
            }),
            'bank_account': forms.TextInput(attrs={
                'class': 'form-control form-control-sm text-center',
            }),
            'unp': forms.TextInput(attrs={
                'class': 'form-control form-control-sm text-center',
            }),
            'contract_1': forms.FileInput(attrs={
                'class': 'form-control form-control-sm',
                'accept': '.pdf, .docx, .doc, .odf',
            }),
            'contract_2': forms.FileInput(attrs={
                'class': 'form-control form-control-sm',
                'accept': '.pdf, .docx, .doc, .odf',
            }),
        }