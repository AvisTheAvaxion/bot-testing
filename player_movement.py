import hikari
import hidden
w, h = 12, 12

matrix = [[0 for x in range(w)] for y in range(h)]


def make_arr():
    for i in range(h):
        for i1 in range(w):
            matrix[i][i1] = 0


make_arr()

player_x_pos = 0
player_y_pos = 0
matrix[player_y_pos][player_x_pos] = 2


def print_array():
    s = ""
    for i in range(h):
        for i1 in range(w):
            s = s + str(matrix[i][i1])

        s = s + "\n"

    return s


def run():

    bot = hikari.GatewayBot(token=hidden.token)

    @bot.listen()
    async def show_array(event: hikari.GuildMessageCreateEvent) -> None:

        if event.is_bot or not event.content:
            return

        if event.message.content == "!show":
            await event.message.respond(print_array())
            await event.message.respond("----------------------------")

    @bot.listen()
    async def up(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        if event.message.content == "!up":
            global player_y_pos
            if player_y_pos > 0:
                matrix[player_y_pos][player_x_pos] = 0
                player_y_pos = player_y_pos - 1
                matrix[player_y_pos][player_x_pos] = 2
                await event.message.respond(print_array())
                await event.message.respond("----------------------------")

            else:
                await event.message.respond("Invalid move")

    @bot.listen()
    async def down(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        if event.message.content == "!down":
            global player_y_pos
            if player_y_pos == h - 1:
                await event.message.respond("Invalid move!")

            else:
                matrix[player_y_pos][player_x_pos] = 0
                player_y_pos = player_y_pos + 1
                matrix[player_y_pos][player_x_pos] = 2
                await event.message.respond(print_array())
                await event.message.respond("----------------------------")

    @bot.listen()
    async def left(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        if event.message.content == "!left":
            global player_x_pos
            if player_x_pos > 0:
                matrix[player_y_pos][player_x_pos] = 0
                player_x_pos = player_x_pos - 1
                matrix[player_y_pos][player_x_pos] = 2
                await event.message.respond(print_array())
                await event.message.respond("----------------------------")

            else:
                await event.message.respond("Invalid Move")

    @bot.listen()
    async def right(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        if event.message.content == "!right":
            global player_x_pos
            if player_x_pos == w - 1:
                await event.message.respond("Invalid move!")

            else:
                matrix[player_y_pos][player_x_pos] = 0
                player_x_pos = player_x_pos + 1
                matrix[player_y_pos][player_x_pos] = 2
                await event.message.respond(print_array())
                await event.message.respond("----------------------------")




    bot.run()


run()
