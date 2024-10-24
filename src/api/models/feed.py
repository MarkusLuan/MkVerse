from django.db import models

import uuid

class Feed (models.Model):
    id = models.BigAutoField(null=False, unique=True, primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, null=False, unique=True)
    dt_criacao = models.DateTimeField(auto_now_add=True, null=False)
    texto = models.TextField(null=False)
    uuid_imagem = models.UUIDField(null=True, unique=True)
    user = models.OneToOneField("api.User", models.CASCADE, null=False)
