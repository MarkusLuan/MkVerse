from django.db import models

import uuid

class Likes (models.Model):
    id = models.BigAutoField(null=False, unique=True, primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, null=False, unique=True)
    dt_criacao = models.DateTimeField(auto_now_add=True, null=False)
    user = models.OneToOneField("api.User", models.CASCADE, null=False)
    feed = models.OneToOneField("api.Feed", models.CASCADE, null=False)
