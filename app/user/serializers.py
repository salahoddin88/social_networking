"""
    Serializers for the user API View
"""
from rest_framework import serializers
from django.contrib.auth import (
    get_user_model,
    password_validation
)


class UserRegistrationSerializer(serializers.ModelSerializer):
    """ User registration serializer """

    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )
    confirm_password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password'
        ]

    def validate_password(self, password):
        try:
            password_validation.validate_password(password)
        except serializers.ValidationError as error:
            raise serializers.ValidationError(str(error))
        return password

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({
                'password': "Passwords do not match."
            })
        return data

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserSeializer(serializers.ModelSerializer):
    """ User details serializer """
    name = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email',
            'name',
            'phone',
            'profile_picture',
            'last_login',
        )

    def get_name(self, instance):
        return instance.get_full_name()

    def get_profile_picture(self, instance):
        if instance.profile_picture:
            return instance.profile_picture.url
        return 'example/dummy_profile_pic.png'
