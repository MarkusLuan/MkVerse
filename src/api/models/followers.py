from django.db import models

import uuid

class Followers (models.Model):
    id = models.BigAutoField(null=False, unique=True, primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, null=False, unique=True)
    dt_criacao = models.DateTimeField(auto_now_add=True, null=False)
    
    seguidor = models.ForeignKey(
        "api.User",
        null=False,
        related_name = "seguindo",
        on_delete=models.CASCADE
    )
    seguindo = models.ForeignKey(
        "api.User",
        null=False,
        related_name = "seguidor",
        on_delete=models.CASCADE
    )

    models.UniqueConstraint(name="uk_followers", fields=[seguidor, seguindo])