from django.urls import path

from federations import views

app_name = "federations"

urlpatterns = [
    path("federations", views.federations, name="federations-list"),
    path("federation/add", views.create_federation, name="federation-add"),
    path("federation/<int:pk>/detail/", views.federation_detail, name="federation-detail"),
    path("federation/<int:pk>/update/", views.federation_update, name="federation-update"),
    path("federation/<int:pk>/delete/", views.federation_delete, name="federation-delete"),
]