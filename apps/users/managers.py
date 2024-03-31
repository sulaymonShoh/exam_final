from django.contrib.auth.models import UserManager
from django.db.models import Manager, QuerySet


class CustomManager(UserManager):
    def get_queryset(self):
        return QuerySet(self.model, using=self._db).filter(deleted_at__isnull=True)
