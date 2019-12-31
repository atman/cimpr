from django import forms
from core.models import Contact
import phonenumbers


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'user',
            'first_name',
            'last_name',
            'type',
            'phone_number',
            'email',
            'image',
        ]

    def clean_phone_number(self, *args, **kwargs):
        # Validate Phone Number
        print("Inside Phone Number Clean...")
        phone_number = self.cleaned_data.get('phone_number', None)
        if phone_number is "":
            return phone_number
        else:
            try:
                cleaned_phone_number = phonenumbers.parse(phone_number, None)
                if phonenumbers.is_valid_number(cleaned_phone_number):
                    pass
                else:
                    raise forms.ValidationError("Oops! Please enter correct phone number with Country Code")
            except phonenumbers.phonenumberutil.NumberParseException:
                raise forms.ValidationError("Oops! Please enter correct phone number with Country Code")

            return phone_number



