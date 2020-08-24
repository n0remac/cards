from .models import Player


def get_game(request):
    """
    Attempt to retrieve the current player from sessions. If no player is found,
    generate a new player.
    """

    is_cached = "game_data" in request.session
    if not is_cached:
        player = Player.objects.create(name="player")
        game_data = player.to_dict()
        request.session["game_data"] = game_data
    else:
        game_data = request.session["game_data"]
        if Player.objects.filter(id=game_data["id"]).exists():
            request.session["game_data"] = game_data
        else:
            player = Player.objects.create(name="player")
            game_data = player.to_dict()
            request.session["game_data"] = game_data
