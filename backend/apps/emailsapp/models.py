from django.db import models


class Email(models.Model):
    email = models.EmailField(blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(blank=True, null=False, default=False)
