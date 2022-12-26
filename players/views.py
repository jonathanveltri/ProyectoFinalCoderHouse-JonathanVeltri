from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from players.models import Player
from players.forms import PlayerForm
from players.models import Comment
from players.forms import CommentForm

# Create your views here.
class PlayerListView(ListView):
    model = Player
    template_name = "players/players_list.html"
    paginate_by = 3


class PlayerCreateView(LoginRequiredMixin,CreateView):
    model = Player
    success_url = reverse_lazy("players:players-list")

    form_class = PlayerForm

    def form_valid(self, form):
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Player.objects.filter(
            name=data["name"], last_name=data["last_name"],).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El jugador {data['name']} {data['last_name']} ya se encuentra en la base de datos",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Jugador {data['name']} {data['last_name']} incluido exitosamente!",
            )
            return super().form_valid(form)
        
class PlayerDetailView(DetailView):
    model = Player
    template_name = "players/player_detail.html"
    fields = ["name", "last_name", "team", "number", "position"]

    def get(self, request, pk):
        player = Player.objects.get(id=pk)
        comments = Comment.objects.filter(player=player).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "player": player,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)
    
class PlayerUpdateView(LoginRequiredMixin,UpdateView):
    model = Player
    fields = ["name", "last_name", "team", "number", "position"]

    def get_success_url(self):
        player_id = self.kwargs["pk"]
        return reverse_lazy("players:player-detail", kwargs={"pk": player_id})

class PlayerDeleteView(LoginRequiredMixin,DeleteView):
    model = Player
    success_url = reverse_lazy("players:players-list")

class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        player = get_object_or_404(Player, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, player=player
        )
        comment.save()
        return redirect(reverse("players:player-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        player = self.object.player
        return reverse("players:player-detail", kwargs={"pk": player.id})