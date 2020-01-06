from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse(
        "Hello, world. You're at the app index."
    )

# Create your views here.
