from rest_framework import serializers
from core.models import Contact
import phonenumbers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'type',
            'phone_number',
            'email',
            'image'
        ]

        read_only_fields = ['user']

    def validate_phone_number(self, phone_number, *args, **kwargs):
        # Validate Phone Number
        if phone_number is "":
            return phone_number
        else:
            try:
                cleaned_phone_number = phonenumbers.parse(phone_number, None)
                if phonenumbers.is_valid_number(cleaned_phone_number):
                    pass
                else:
                    raise serializers.ValidationError("Oops! Please enter correct phone number with Country Code")
            except phonenumbers.phonenumberutil.NumberParseException:
                raise serializers.ValidationError("Oops! Please enter correct phone number with Country Code")

            return phone_number

