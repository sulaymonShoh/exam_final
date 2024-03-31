from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.vacancy.models import Vacancy
from apps.vacancy.api_endpoints.Vacancy.VacancyFilter.serializers import (
    VacancyFilterSerializer,
)


class VacancyFilterAPIView(APIView):
    serializer_class = VacancyFilterSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Vacancy.objects.all()
        salary_from = self.request.query_params.get("salary_from")
        salary_to = self.request.query_params.get("salary_to")
        salary = self.request.query_params.get("salary")

        if salary_from is not None:
            queryset = queryset.filter(salary__gte=salary_from)
        if salary_to is not None:
            queryset = queryset.filter(salary__lte=salary_to)
        if salary is not None:
            queryset = queryset.filter(salary__exact=salary)

        return queryset
