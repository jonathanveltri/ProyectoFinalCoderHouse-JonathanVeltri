from django.forms.models import model_to_dict
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from federations.models import Federation
from federations.forms import FederationForm


# Create your views here.
def federations(request):
    federations = Federation.objects.all()

    context_dict = {"federations": federations}

    return render(
        request = request,
        context = context_dict,
        template_name="federations/federations_list.html",
    )

@login_required
def create_federation(request):
    if request.method == "POST":
        federation_form = FederationForm(request.POST, request.FILES)
        if federation_form.is_valid() and len(request.FILES) != 0:
            image = request.FILES["image"]
            data = federation_form.cleaned_data
            actual_objects = Federation.objects.filter(
                name=data["name"], initials=data["initials"], official_website=data["official_website"]
            ).count()
            if actual_objects:
                messages.error(
                    request,
                    f"La federación {data['name']} - {data['initials']} ya existe",
                )
            else:
                federation = Federation(name=data["name"], initials=data["initials"], official_website=data["official_website"], image=image, owner=request.user)
                federation.save()
                messages.success(
                    request,
                    f"Federación {data['name']} - {data['initials']} incluida exitosamente!",
                )

            federations = Federation.objects.all()

            context_dict = {"federations": federations}

            return render(
                request=request,
                context=context_dict,
                template_name="federations/federations_list.html",
            )

    federation_form = FederationForm(request.POST)
    context_dict = {"form": federation_form}
    return render(
        request=request,
        context=context_dict,
        template_name="federations/federations_form.html",
    )

def federation_detail(request, pk: int):
    return render(
        request=request,
        context={"federation": Federation.objects.get(pk=pk)},
        template_name="federations/federation_detail.html",
    )

@login_required
def federation_update(request, pk: int):
    federation = Federation.objects.get(pk=pk)

    if request.method == "POST":
        federation_form = FederationForm(request.POST, request.FILES)
        if federation_form.is_valid():
            data = federation_form.cleaned_data
            federation.name = data["name"]
            federation.initials = data["initials"]
            federation.official_website = data["official_website"]
            federation.image = data["image"]
            federation.save()

            return render(
                request=request,
                context={"federation": federation},
                template_name="federations/federation_detail.html",
            )

    federation_form = FederationForm(model_to_dict(federation))
    context_dict = {
        "federation": federation,
        "form": federation_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="federations/federations_form.html",
    )

@login_required
def federation_delete(request, pk: int):
    federation = Federation.objects.get(pk=pk)
    if request.method == "POST":
        federation.delete()

        federations = Federation.objects.all()
        context_dict = {"federations": federations}
        return render(
            request=request,
            context=context_dict,
            template_name="federations/federations_list.html",
        )

    context_dict = {
        "federation": federation,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="federations/federation_confirm_delete.html",
    )