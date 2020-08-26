from .models import Player


def get_game(request):
    """
    Attempt to retrieve the current player from sessions. If no player is found,
    generate a new player.
    """

    # if it is a new player a new database entry for a player will be made
    is_cached = "player_data" in request.session
    if not is_cached:
        player = Player.objects.create(name="player")
        player_data = player.to_dict()
        request.session["player_data"] = player_data
    # If the user already has cached data check if there is a database entry, if not create one
    else:
        player_data = request.session["player_data"]
        if Player.objects.filter(id=player_data["id"]).exists():
            request.session["player_data"] = player_data
        else:
            player = Player.objects.create(name="player")
            player_data = player.to_dict()
            request.session["player_data"] = player_data
