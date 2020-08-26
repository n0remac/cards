from django.shortcuts import render
from django.views.generic import DetailView
from .models import Game


class Board(DetailView):
    template_name = "game_board/index.html"

    def get(self, request, *args, **kwargs):
        player_data = request.session["player_data"]
        if not player_data["started"]:
            self.setup_game(request, player_data)
        else:
            self.run_game(request, player_data)

        request.session["player_data"] = player_data
        return render(request, self.template_name, player_data)

    def setup_game(self, request, player_data):
        player_data.update({"started": True})
        playerID = player_data.get("id")
        opponentID = player_data.get("opponent")
        games = Game.objects.all()
        new_game = True
        for game in games:
            if (game.player1 == opponentID and game.player2 == playerID) or (
                game.player1 == playerID and game.player2 == opponentID
            ):
                player_data.update({"game_id": game.id})
                new_game = False
                break
        if new_game:
            game = Game.objects.create(
                player1=playerID, player2=opponentID, whos_turn=playerID
            )
            player_data.update({"game_id": game.id})

    def run_game(self, request, player_data):
        pass
