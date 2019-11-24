from django.db import models
from .base import BaseModel


class Follower(BaseModel):
    user_id = models.CharField(max_length=30)
    follower_id = models.CharField(max_length=30)
    subscription_date = models.DateTimeField()
    subscription_flag = models.BooleanField()

    @staticmethod
    def create_follower(created_at, updated_at, user_id, follower_id, subscription_date, subscription_flag):
        return Follower.objects.create(
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
            follower_id=follower_id,
            subscription_date=subscription_date,
            subscription_flag=subscription_flag,
        )