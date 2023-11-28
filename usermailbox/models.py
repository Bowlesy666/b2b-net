from django.db import models
from userprofile.models import UserProfile
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from booking.models import slug_save

# https://stackoverflow.com/questions/43696074/django-private-messaging-conversation-view
class ConversationModel(models.Model):
    sender_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="sent_conversations")
    receiver_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="received_conversations")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_archived = models.BooleanField(default=False)
    is_trash = models.BooleanField(default=False)
    conversation_subject = models.CharField(max_length=100, unique=True, null=True)

    class Meta:
        ordering = ["-updated_on"]

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_save(self)
        super(ConversationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


class MessageModel(models.Model):
    conversation = models.ForeignKey(ConversationModel, on_delete=models.CASCADE, related_name="messages")
    sender_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="sent_messages")
    receiver_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="received_messages")
    message_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
