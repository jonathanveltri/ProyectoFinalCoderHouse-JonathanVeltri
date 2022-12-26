from django.urls import path

from teams import views

app_name = "teams"

urlpatterns = [
    path("teams", views.teams, name="teams-list"),
    path("team/add", views.create_team, name="team-add"),
]