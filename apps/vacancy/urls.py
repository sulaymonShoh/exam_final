from django.urls import path
from apps.vacancy.api_endpoints.Vacancy.VacancyFilter.views import VacancyFilterAPIView

urlpatterns = [
    path("", VacancyFilterAPIView.as_view(), name="vacancy-filter"),
]
