from django.shortcuts import render
from django.contrib import messages
from teams.models import Team
from teams.forms import TeamForm


# Create your views here.
def teams(request):
    teams = Team.objects.all()

    context_dict = {"teams": teams}

    return render(
        request = request,
        context = context_dict,
        template_name="teams/teams_list.html",
    )

def create_team(request):
    if request.method == "POST":
        team_form = TeamForm(request.POST)
        if team_form.is_valid():
            data = team_form.cleaned_data
            actual_objects = Team.objects.filter(
                name=data["name"], federation=data["federation"], country=data["country"], city=data["city"], fundation_date=data["fundation_date"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El equipo {data['name']} ya existe",
                )
            else:
                team = Team(name=data["name"], federation=data["federation"], country=data["country"], city=data["city"], fundation_date=data["fundation_date"])
                team.save()
                messages.success(
                    request,
                    f"Equipo {data['name']}  incluido exitosamente!",
                )

            teams = Team.objects.all()

            context_dict = {"teams": teams}

            return render(
                request=request,
                context=context_dict,
                template_name="teams/teams_list.html",
            )

    team_form = TeamForm(request.POST)
    context_dict = {"form": team_form}
    return render(
        request=request,
        context=context_dict,
        template_name="teams/teams_form.html",
    )
