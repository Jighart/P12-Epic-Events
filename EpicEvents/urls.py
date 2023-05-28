from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers

from users.views import UpdatePassword
from clients.views import ClientViewset
from contracts.views import ContractViewset
from events.views import EventViewset


client_router = routers.SimpleRouter()
client_router.register(r"clients/?", ClientViewset, basename="clients")

contract_router = routers.SimpleRouter()
contract_router.register(r"contract/?", ContractViewset, basename='contract')

event_router = routers.SimpleRouter()
event_router.register(r"events/?", EventViewset, basename='events')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/update-password/', UpdatePassword.as_view(), name='update_password'),
    path('api/api-auth/', include('rest_framework.urls')),

    path('api/', include(client_router.urls)),
    path('api/', include(contract_router.urls)),
    path('api/', include(event_router.urls)),
]
