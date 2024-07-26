import re
from rest_framework import serializers
from .models import Enquiry
from django.core.exceptions import ValidationError

class EnquirySerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(required=True, error_messages={'required': 'This field is required.'})
    company_name = serializers.CharField(required=True, error_messages={'required': 'This field is required.'})
    business_email = serializers.EmailField(required=True, error_messages={'required': 'This field is required.'})
    job_title = serializers.CharField(required=True, error_messages={'required': 'This field is required.'})
    contact = serializers.CharField(required=True, error_messages={'required': 'This field is required.'})
    looking_for = serializers.CharField(required=True, error_messages={'required': 'This field is required.'})
    service_request = serializers.CharField(required=True, error_messages={'required': 'This field is required.'})


    def validate_full_name(self, value):
        if not re.match(r'^[a-zA-Z]+(\s[a-zA-Z]+)?$', value.strip()):
            raise ValidationError("Please enter a valid Full name.")
        return value

    def validate_company_name(self, value):
        if not re.match(r'^[a-zA-Z\s\.,-]+$', value):
            raise ValidationError("Please enter a valid Company name.")
        return value

    def validate_buisness_email(self, value):
        # Check if the value consists of alphabets, numbers, and special characters only
        if not re.match(r'^[\w.-]+@[a-zA-Z\d]+\.[a-zA-Z]{2,4}$', value):
            raise ValidationError("Please enter a valid Buisness Email.")
        return value

    def validate_job_title(self, value):
        # Check if the value consists of alphabetic and numeric characters only
        if not re.match(r'^[a-zA-Z0-9\s]+$', value):
            raise ValidationError("Please enter a valid Job Title.")
        return value

    def validate_contact(self, value):
        # Check if the value consists of numeric characters only
        if not re.match(r'^\d+$', value):
            raise ValidationError("Please enter a valid Contact Number.")
        return value

    def validate_looking_for(self, value):
        # Check if the value consists of alphabets, numbers, and special characters only
        if not re.match(r'^[a-zA-Z0-9\s@#$%^&*()!-]+$', value):
            raise ValidationError("Only alphabets, numbers, and special characters are allowed.")
        return value

    class Meta:
        model = Enquiry
        fields = '__all__'