from django.shortcuts import render
from .models import Participants
from .forms import RegisterForm


def index_view(request):
    return render(request, "index.html", {})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RegisterForm()  # to clear the page
    context = {
        'form': form,
    }
    return render(request, "registration.html", context)


def speakers_list_view(request):
    queryset = Participants.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, "speakers_list.html", context)



