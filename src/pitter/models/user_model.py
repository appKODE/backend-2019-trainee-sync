from django.db import models
from .base import default_uuid_id
from .base import BaseModel


class User(BaseModel):
    id = models.CharField(default=default_uuid_id, primary_key=True, editable=False, max_length=256)
    login = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    profile_name = models.CharField(max_length=32)
    email_address = models.CharField(max_length=128)
    email_notifications_mode = models.BooleanField()

    def to_dict(self) -> dict:
        return dict(
            id=self.id,
            login=self.login,
            password=self.password,
            profile_name=self.profile_name,
            email_address=self.email_address,
            email_notifications_mode=self.email_notifications_mode,
        )

    @staticmethod
    def create_user(id, login, password, profile_name, email_address, email_notifications_mode):
        return User.objects.create(
            id=id,
            login=login,
            password=password,
            profile_name=profile_name,
            email_address=email_address,
            email_notifications_mode=email_notifications_mode,
        )

