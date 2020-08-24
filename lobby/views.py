from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import redirect
from .models import Player
from .utils import get_game


class Lobby(DetailView):
    template_name = "lobby/index.html"

    def get(self, request, *args, **kwargs):
        get_game(request)
        game_data = request.session["game_data"]
        return render(request, self.template_name, {"player": game_data["id"]})

    def post(self, request):
        # update player name
        game_data = request.session["game_data"]
        name = self.request.POST.get("name")
        player = Player.objects.get(id=game_data.get("id"))
        player.name = name
        player.save(update_fields=["name"])
        game_data.update({"name": name})

        # Checks the players that need a match
        for p in Player.objects.filter(needs_match=True):
            # Makes sure player is not matched with self
            if p.id != game_data.get("id"):
                game_data.update({"needs_match": False})
                game_data.update({"opponent": p.id})
                p.needs_match = False
                p.opponent = player.id
                p.save(update_fields=["needs_match", "opponent"])
                player.needs_match = False
                player.opponent = p.id
                player.save(update_fields=["needs_match", "opponent"])

        request.session["game_data"] = game_data
        response = redirect("/room/")
        return response


class Room(DetailView):
    template_name = "room/index.html"

    def get(self, request, *args, **kwargs):
        """
        If the player has an opponent a view with the opponent info is returned.
        If no opponent the default is used.
        """

        game_data = request.session["game_data"]
        player = Player.objects.get(id=game_data.get("id"))
        game_data = player.to_dict()
        if game_data["opponent"] != 0:
            opponent = Player.objects.get(id=game_data["opponent"])
            game_data.update({"opponent": opponent.name})

        return render(request, self.template_name, game_data)
