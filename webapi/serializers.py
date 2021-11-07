from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from webapi.models import Booking_DB
from rest_framework.response import Response
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError(("Email is already exist."),params = {'value':value})
class RegisterSerializer(serializers.ModelSerializer):
    # email=User.serializers(many=False, read_only=True)
    email = serializers.EmailField(validators=[validate_email])
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['email'], validated_data['password'])
        return user
# validated_data['username'],
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ('email', 'password','id')

        # read_only_fields = ['token']

class BookCallSerializer(serializers.ModelSerializer):
    # email=User.serializers(many=False, read_only=True)
    # email = serializers.EmailField(validators=[validate_email])
    class Meta:
        model = Booking_DB
        fields = ('booking_time',)
        # extra_kwargs = {'password': {'write_only': True}}

    #
    # def create(self, validated_data):
    #     user = Booking_DB.objects.create(validated_data['advisor'],validated_data['booking_id'],validated_data['booking_time'],)
    #     return user
    def create(self, validated_data):
        if Booking_DB.objects.create(**validated_data):
            user = Booking_DB.objects.create(**validated_data)
            return user
