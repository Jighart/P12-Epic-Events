from django.urls import path

from clients import views

app_name = "clients"
urlpatterns = [
    path("", views.ClientList.as_view(), name="list"),
    path("<int:pk>/", views.ClientDetail.as_view(), name="detail"),
]