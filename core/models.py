from ast import Del, Delete
from xml.dom import ValidationErr
from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from accounts.models import User

# Create your models here.
class Post(models.Model):
  posted_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, blank=True, default=None)
  title = models.CharField(max_length=50)
  description = models.TextField(max_length=10000)
  attachment = models.FileField(upload_to='attachments/', max_length=250, null=True, blank=True, default=None,
                                 validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xlsx', 'png', 'jpg', 'jpeg'])])
  date_posted = models.DateTimeField(auto_now_add=True)
  for_grade = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
  slug = models.SlugField(unique=True, blank=True, null=True)

  class Meta:
    ordering = ['-date_posted']

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    value = self.title
    self.slug = slugify(value, allow_unicode=True)

    return super().save(*args, **kwargs)