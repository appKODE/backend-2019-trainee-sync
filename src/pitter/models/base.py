import uuid

from django.db import models


def default_uuid_id() -> str:
    return str(uuid.uuid4()).replace('-', '')


class BaseModel(models.Model):
    id = models.CharField(default=default_uuid_id, primary_key=True, editable=False, max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    id = models.CharField(default=default_uuid_id, primary_key=True, editable=False, max_length=256)
    login = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    profile_name = models.CharField(max_length=32)
    email_address = models.CharField(max_length=128)
    email_notifications_mode = models.BooleanField()


class Pitt(BaseModel):
    id = models.CharField(default=default_uuid_id, primary_key=True, editable=False, max_length=256)
    user_id = models.CharField(max_length=256)
    add_date = models.DateTimeField()
    audio_path = models.CharField(max_length=3000)
    audio_decoded = models.CharField(max_length=1000)


class Follower(BaseModel):
    user_id = models.CharField(max_length=30)
    follower_id = models.CharField(max_length=30)
    subscription_date = models.DateTimeField()
    subscription_flag = models.BooleanField()

