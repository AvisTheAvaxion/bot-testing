
class Player:
    pfp = None
    discriminator = None
    name = None
    id = None


def parse(player_info):
    new_player = Player()
    new_player.pfp = player_info["Pfp"]
    new_player.discriminator = player_info["Discriminator"]
    new_player.name = player_info["Author"]
    new_player.id = player_info["Id"]
    return new_player