from .models import Player


def get_game(request):
    """
    Attempt to retrieve the current player from sessions. If no player is found,
    generate a new player.
    """

    # if it is a new player a new database entry for a player will be made
    is_cached = "game_data" in request.session
    if not is_cached:
        player = Player.objects.create(name="player")
        game_data = player.to_dict()
        request.session["game_data"] = game_data
    # If the user already has cached data check if there is a database entry, if not create one
    else:
        game_data = request.session["game_data"]
        if Player.objects.filter(id=game_data["id"]).exists():
            request.session["game_data"] = game_data
        else:
            player = Player.objects.create(name="player")
            game_data = player.to_dict()
            request.session["game_data"] = game_data
