from django.shortcuts import render
from django.views.generic import DetailView
from .models import Card, Game


class Board(DetailView):
    template_name = "game_board/index.html"

    def get(self, request, *args, **kwargs):
        cards = Card.objects.all()
        context = {"cards": cards}
        game_data = request.session["game_data"]
        if not game_data["started"]:
            game_data.update({"started": True})
            playerID = game_data.get("id")
            opponentID = game_data.get("opponent")
            print("-----------------------")
            print(playerID, opponentID)
            Game.objects.create(player1=playerID, player2=opponentID)

        return render(request, self.template_name, context)
