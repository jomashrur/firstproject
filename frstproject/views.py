
from django.shortcuts import render
from .forms import shakForm

# creating a home view


def home_view(request):
    context = {}
    form = shakForm(request.POST or None)
    context['form'] = form
    return render(request, "home.html", context)
