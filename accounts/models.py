from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from .manager import UserManager

# Create your models here.

class User(AbstractUser):
  email = models.EmailField(unique=True)
  grade = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], null=True, blank=True)

  objects = UserManager()

  REQUIRED_FIELDS = []
