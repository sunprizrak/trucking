from django import forms
from .models import PreliminaryClaim, ShippingClaim
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class PreliminaryClaimForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, required=True)

    class Meta:
        model = PreliminaryClaim
        fields = '__all__'
        widgets = {
            'shipping_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'gross_weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'min': 0,
            }),
            'count_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'min': 0,
            }),
            'type_seats': forms.Select(attrs={
                'class': 'form-select',
                'required': True,
            }),
            'length_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'min': 0,
            }),
            'width_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'min': 0,
            }),
            'height_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'min': 0,
            }),
            'fly': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
            }),
            'train': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
            }),
            'ship': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
            }),
            'auto': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
            }),
            'point_departure': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'destination': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True,
                'placeholder': 'дд.мм.гггг',
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True,
                'placeholder': 'дд.мм.гггг',
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'messenger': forms.Select(attrs={
                'class': 'form-select',
            }),
            'messenger_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'contact_person': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
        }


class ShippingClaimForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, required=True)

    class Meta:
        model = ShippingClaim
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'shipping_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'gross_weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'min': 0,
            }),
            'count_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'min': 0,
            }),
            'type_seats': forms.Select(attrs={
                'class': 'form-select',
                'required': True,
            }),
            'length_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'min': 0,
            }),
            'width_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'min': 0,
            }),
            'height_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'min': 0,
            }),
            'point_departure': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'destination': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'code': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1111111111,
                'max': 9999999999,
                'required': True,
            }),
            'cargo_features': forms.RadioSelect(attrs={
                'class': 'form-check-input',
                'type': 'radio',
                'required': True,
            }),
            'cargo_insurance': forms.RadioSelect(attrs={
                'class': 'form-check-input',
                'type': 'radio',
                'required': True,
            }),
            'date_loading': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True,
                'placeholder': 'дд.мм.гггг',
            }),
            'transport': forms.Select(attrs={
                'class': 'form-select',
                'required': True,
            }),
            'person_loading': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'per_load_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'per_load_msg': forms.Select(attrs={
                'class': 'form-select',
            }),
            'per_load_msg_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'person_unloading': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'per_unload_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'per_unload_msg': forms.Select(attrs={
                'class': 'form-select',
            }),
            'per_unload_msg_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }
