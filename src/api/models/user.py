from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.models import TokenUser

import uuid

class UserManager (BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not (email or password):
            raise ValueError("Email ou senha não informados")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(null=False, unique=True, primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, null=False, unique=True)
    dt_criacao = models.DateTimeField(auto_now_add=True, null=False)
    dt_nascimento = models.DateField(null=False)
    nick = models.TextField(null=False, unique=True, max_length=20)
    nome = models.TextField(null=False, max_length=200)
    email = models.EmailField(null=False, unique=True)
    bio = models.TextField(null=True, max_length=250)
    
    objects = UserManager()
    
    USERNAME_FIELD = "nick"
    user_permissions = [TokenUser]
    groups = [TokenUser]
    REQUIRED_FIELDS = [dt_nascimento, nick, nome, email]

    def __str__(self):
        return self.nome