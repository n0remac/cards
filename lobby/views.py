from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import redirect
from .models import Player
from .utils import get_game


class Lobby(DetailView):
    template_name = "lobby/index.html"

    def get(self, request, *args, **kwargs):
        get_game(request)
        player_data = request.session["player_data"]
        return render(request, self.template_name, {"player": player_data["id"]})

    def post(self, request):
        # update player name
        player_data = request.session["player_data"]
        name = self.request.POST.get("name")
        player = Player.objects.get(id=player_data.get("id"))
        player.needs_match = True
        player.name = name
        player.save(update_fields=["name", "needs_match"])
        player_data.update({"name": name})

        # Checks the players that need a match
        for p in Player.objects.filter(needs_match=True):
            # Makes sure player is not matched with self
            if p.id != player_data.get("id"):
                player_data.update({"needs_match": False})
                player_data.update({"opponent": p.id})
                p.needs_match = False
                p.opponent = player.id
                p.save(update_fields=["needs_match", "opponent"])
                player.needs_match = False
                player.opponent = p.id
                player.save(update_fields=["needs_match", "opponent"])

        request.session["player_data"] = player_data
        response = redirect("/room/")
        return response


class Room(DetailView):
    template_name = "room/index.html"

    def get(self, request, *args, **kwargs):
        """
        If the player has an opponent a view with the opponent info is returned.
        If no opponent the default is used.
        """

        player_data = request.session["player_data"]
        player = Player.objects.get(id=player_data.get("id"))
        player_data = player.to_dict()
        if player_data["opponent"] != 0:
            opponent = Player.objects.get(id=player_data["opponent"])
            player_data.update({"opponent": opponent.id})
            player_data.update({"game_id": 0})
            player_data.update({"started": False})
            request.session["player_data"] = player_data
            return redirect("/game/")
        return render(request, self.template_name, player_data)
