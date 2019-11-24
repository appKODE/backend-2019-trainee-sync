from django.db import models
from .base import default_uuid_id
from .base import BaseModel


class Pitt(BaseModel):
    id = models.CharField(default=default_uuid_id, primary_key=True, editable=False, max_length=256)
    user_id = models.CharField(max_length=256)
    audio_path = models.CharField(max_length=3000)
    audio_decoded = models.CharField(max_length=1000)

    @staticmethod
    def create_pitt(id, user_id, audio_path, audio_decoded):
        return Pitt.objects.create(
            id=id,
            user_id=user_id,
            audio_path=audio_path,
            audio_decoded=audio_decoded,
        )