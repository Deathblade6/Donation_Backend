from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    phone = serializers.RegexField(regex=r'^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$',required=True,error_messages={'required':('Please enter phone number'), 'invalid':('Please enter number in correct format. Eg:7025266580')})
    first_name = serializers.CharField(max_length=30, label='First Name')
    last_name = serializers.CharField(max_length=30, label='Last Name')
    address = serializers.CharField(max_length=500,label="Address")

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.address = self.validated_data.get('address', '')
        user.phone = self.validated_data.get('phone', '')
        user.save(update_fields=['first_name','last_name','phone','address'])
        print("here")