from rest_framework import serializers
from apps.vacancy.models import Vacancy


class VacancyFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ["title", "description", "salary"]
