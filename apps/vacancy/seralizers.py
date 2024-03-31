from rest_framework.serializers import ModelSerializer

from apps.vacancy.models import Vacancy


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('title', 'description', 'salary')
