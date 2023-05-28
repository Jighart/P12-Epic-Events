from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import SALES, SUPPORT
from contracts.models import Contract
from contracts.permissions import ContractPermissions
from contracts.serializers import ContractSerializer


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ContractPermissions]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        "^client__first_name",
        "^client__last_name",
        "^client__email",
        "^client__company_name",
    ]
    filterset_fields = {
        "date_created": ["gte", "lte"],
        "payment_due": ["gte", "lte"],
        "amount": ["gte", "lte"],
        "status": ["exact"],
    }

    def get_queryset(self):
        if self.request.user.team == SUPPORT:
            return Contract.objects.filter(event__support_contact=self.request.user)
        elif self.request.user.team == SALES:
            return Contract.objects.filter(sales_contact=self.request.user)
        return Contract.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data["sales_contact"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer = ContractSerializer(data=request.data, instance=self.get_object())
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data["sales_contact"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
