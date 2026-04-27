from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Route


def index(request):
    routes = Route.objects.select_related("origin", "destination").all()
    return render(request, "routes/index.html", {"routes": routes})


def detail(request, route_id):
    route = get_object_or_404(Route, pk=route_id)
    passengers = route.passengers.all()
    already_booked = request.user.is_authenticated and route.passengers.filter(pk=request.user.pk).exists()
    return render(request, "routes/detail.html", {
        "route": route,
        "passengers": passengers,
        "already_booked": already_booked,
    })


@login_required
def book(request, route_id):
    if request.method == "POST":
        route = get_object_or_404(Route, pk=route_id)
        route.passengers.add(request.user)
    return HttpResponseRedirect(reverse("detail", args=(route_id,)))


@login_required
def unbook(request, route_id):
    if request.method == "POST":
        route = get_object_or_404(Route, pk=route_id)
        route.passengers.remove(request.user)
    return HttpResponseRedirect(reverse("detail", args=(route_id,)))


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})