from rest_framework import serializers
from .models import Friend, FriendRequest
from user.serializers import UserSeializer
from datetime import timedelta, datetime


class FriendRequestSerializer(serializers.ModelSerializer):
    """ FriendRequest serializer"""

    class Meta:
        model = FriendRequest
        fields = (
            'id',
            'sender',
            'receiver',
            'status',
            'created_at',
        )
        extra_kwargs = {
            'sender' : { 'read_only' : True },
            'receiver' : { 'write_only' : True },
            'status' : { 'read_only' : True },
            'created_at' : { 'read_only' : True },
        }

    def validate(self, attrs):
        sender = self.context.get('sender')
        current_created_at = datetime.now()
        one_minute_earlier = current_created_at - timedelta(minutes=1)
        check_request_count = FriendRequest.objects.filter(
            sender=sender,
            created_at__gte=one_minute_earlier,
            created_at__lt=current_created_at,
        ).count()
        if check_request_count >= 3:
            raise serializers.ValidationError('You\'ve sent too many friend requests in a short time. Please wait a bit before sending more.')
        return attrs

    def validate_receiver(self, attrs):
        sender = self.context.get('sender')
        if sender == attrs:
            raise serializers.ValidationError('Turns out, you can\'t be friends with yourself. Who would\'ve thought?')

        try:
            FriendRequest.objects.get(sender=sender, receiver=attrs)
            raise serializers.ValidationError('Your friend request has already been sent.')
        except FriendRequest.DoesNotExist:
            pass
        try:
            FriendRequest.objects.get(sender=attrs, receiver=sender)
            raise serializers.ValidationError('You\'ve got another friend request from this user. How unexpected!')
        except FriendRequest.DoesNotExist:
            return attrs

    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['sender'] = UserSeializer(instance.sender).data
        return data

    def create(self, validated_data):
        validated_data['created_at'] = datetime.now()
        return super().create(validated_data)


class FriendListSerializer(serializers.ModelSerializer):
    """ Friend List serializer """
    friend = serializers.SerializerMethodField()

    class Meta:
        model = Friend
        fields = [
            'id',
            'friend',
            'created_at'
        ]

    def get_friend(self, instance):
        user = self.context.get('user')
        # check logged in user with user_one and user_two and return the friend name
        if user == instance.user_one:
            return UserSeializer(instance.user_two).data
        return UserSeializer(instance.user_one).data