from django.urls import path

from players import views

app_name = "players"

urlpatterns = [
#    path("players", views.players, name="players-list"),
#    path("player/add", views.create_player, name="player-add"),

    path("player/add/", views.PlayerCreateView.as_view(), name="player-add"),
    path("players/", views.PlayerListView.as_view(), name="players-list"),
    path("player/<int:pk>/detail/", views.PlayerDetailView.as_view(), name="player-detail"),
    path("player/<int:pk>/update/", views.PlayerUpdateView.as_view(), name="player-update"),
    path("player/<int:pk>/delete/", views.PlayerDeleteView.as_view(), name="player-delete"),

    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]