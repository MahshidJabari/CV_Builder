from typing import Callable
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from rest_framework_simplejwt.tokens import AccessToken


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True


class User(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=256, unique=False)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'id'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    @classmethod
    def create_deferred_user(cls, **kwargs) -> Callable[[], 'User']:
        """
        returns a function, which once called, will return a new User object
        this is used when creating new Customer or Admin profile using `get_or_create`
        """

        def create_user():
            return cls.objects.create(**kwargs)

        return create_user

    def get_tokens_for_user(self) -> str:
        return str(AccessToken.for_user(self))
