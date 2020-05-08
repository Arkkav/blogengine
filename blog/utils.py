from django.shortcuts import render, get_object_or_404
from .models import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):  # process GET requests, no needs in "if else"...
        obj = get_object_or_404(self.model, slug__iexact=slug)  # class indeed + condition
        return render(request, self.template, context={self.model.__name__.lower(): obj})