from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
