from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from apps.users.managers import CustomManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True, default=None)

    def hard_delete(self, using=None, keep_parents=False):
        super().delete(using=using, keep_parents=keep_parents)

    def delete(self):
        if self.deleted_at is None:
            self.deleted_at = timezone.now()
            self.save()
        else:
            # bir objectga 2 marta delete sorov kelsa hard delete bajarailadi
            self.hard_delete()

    def restore(self):
        self.deleted_at = None
        self.save()

    def get_deleted_at(self):
        return self.deleted_at or None

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    class Meta:
        abstract = True


class CustomUser(BaseModel, AbstractUser):
    objects = CustomManager()  # soft deleted userlarni handle qilish uchun manager
