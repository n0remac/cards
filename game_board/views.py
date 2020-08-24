from django.shortcuts import render
from django.views.generic import DetailView
from .models import Card


class Board(DetailView):
    template_name = "game_board/index.html"

    def get(self, request, *args, **kwargs):
        cards = Card.objects.all()
        context = {"cards": cards}
        return render(request, self.template_name, context)
