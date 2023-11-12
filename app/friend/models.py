from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model


class FriendRequest(models.Model):
    Friend_Request_Status = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]
    sender = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='friend_requests_sender'
    )
    receiver = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='friend_requests_receiver'
    )
    status = models.CharField(max_length=20, choices=Friend_Request_Status)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.receiver.get_full_name()}'

class Friend(models.Model):
    user_one = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user1_friends'
    )
    user_two = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user2_friends'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_one', 'user_two')

    def save(self, *args, **kwargs):
        if self.user_one_id > self.user_two_id:
            self.user_one, self.user_two = self.user_two, self.user_one
        super().save(*args, **kwargs)