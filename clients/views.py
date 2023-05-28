from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import SALES, SUPPORT
from clients.models import Client
from clients.permissions import ClientPermissions
from clients.serializers import ClientSerializer


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, ClientPermissions]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["^first_name", "^last_name", "^email", "^company_name"]
    filterset_fields = ["status"]

    def get_queryset(self):
        if self.request.user.team == SUPPORT:
            return Client.objects.filter(
                contract__event__support_contact=self.request.user
            ).distinct()
        elif self.request.user.team == SALES:
            prospects = Client.objects.filter(status=False)
            own_clients = Client.objects.filter(sales_contact=self.request.user)
            return prospects | own_clients
        return Client.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data["status"] is True:
                serializer.validated_data["sales_contact"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        client = self.get_object()
        serializer = ClientSerializer(data=request.data, instance=client)
        if serializer.is_valid(raise_exception=True):
            if client.status is True and serializer.validated_data["status"] is False:
                raise ValidationError({"detail": "Cannot change status of converted client."})
            elif serializer.validated_data["status"] is True:
                serializer.validated_data["sales_contact"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
