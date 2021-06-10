from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password):
        user = CustomUser.objects.create(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    last_login = None    # disable unwanted field provided by AbstractBaseUser

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

