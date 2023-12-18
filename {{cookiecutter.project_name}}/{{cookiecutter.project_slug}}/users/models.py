from django.db import models
from {{cookiecutter.project_slug}}.common.models import BaseModel

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin



class User(BaseModel, AbstractUser, PermissionsMixin):


    def __str__(self):
        return self.email



