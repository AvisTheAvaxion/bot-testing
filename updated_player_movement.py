import hikari
import hidden
w, h = 12, 12

player_x_pos = 6
player_y_pos = 6

ccw, cch = 3, 3

chunk_x_pos = 1
chunk_y_pos = 1

chunk_seed = [[0 for x in range(ccw)] for y in range(cch)]


def gen_seeds():
    a = 0
    for i in range(cch):
        for i1 in range(ccw):
            chunk_seed[i][i1] = a
            a = a + 1


gen_seeds()


current_chunk = [[0 for x in range(w)] for y in range(h)]


def gen_chunk(height, width, value):
    for i in range(height):
        for i1 in range(width):
            current_chunk[i][i1] = value


gen_chunk(12, 12, chunk_seed[chunk_y_pos][chunk_x_pos])

current_chunk[player_y_pos][player_x_pos] = 2


def print_array(height, width, arr):
    s = ""
    for i in range(height):
        for i1 in range(width):
            s = s + str(arr[i][i1])

        s = s + "\n"

    return s


def invalid_tile_check(x, y):
    a = current_chunk[y][x]
    invalid_tiles = [1, 2, 7, 3, 5]
    check = False
    for i in invalid_tiles:
        if i == a:
            check = True

    return check


current_chunk[4][6] = 1


def run():

    bot = hikari.GatewayBot(token=hidden.token)

    @bot.listen()
    async def show_array(event: hikari.GuildMessageCreateEvent) -> None:

        if event.is_bot or not event.content:
            return

        if event.message.content == "!show":
            await event.message.respond(print_array(12, 12, current_chunk))
            await event.message.respond("----------------------------")

            await event.message.respond(f"py: {player_y_pos}")
            await event.message.respond(f"px: {player_x_pos}")
            await event.message.respond(f"chunk y: {chunk_y_pos}")
            await event.message.respond(f"chunk x: {chunk_x_pos}")

    @bot.listen()
    async def kill(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        if event.message.content == "!kill":
            print("bot killed")
            quit()

    @bot.listen()
    async def up(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        if event.message.content == "!up":
            global player_y_pos
            global chunk_y_pos

            if player_y_pos > 0:
                current_chunk[player_y_pos][player_x_pos] = chunk_seed[chunk_y_pos][chunk_x_pos]
                player_y_pos = player_y_pos - 1
                if not invalid_tile_check(player_x_pos, player_y_pos):
                    current_chunk[player_y_pos][player_x_pos] = 2
                    await event.message.respond(print_array(12, 12, current_chunk))
                    await event.message.respond("----------------------------")

                else:
                    player_y_pos = player_y_pos + 1
                    await event.message.respond("Invalid Move! (Invalid Tile)")
                    current_chunk[player_y_pos][player_x_pos] = 2
                    await event.message.respond(print_array(12, 12, current_chunk))
                    await event.message.respond("----------------------------")

            else:
                if chunk_y_pos > 0:
                    chunk_y_pos = chunk_y_pos - 1
                    gen_chunk(12, 12, chunk_seed[chunk_y_pos][chunk_x_pos])
                    if not invalid_tile_check(player_x_pos, player_y_pos):
                        player_y_pos = 11

                        current_chunk[player_y_pos][player_x_pos] = 2
                        await event.message.respond(print_array(12, 12, current_chunk))
                        await event.message.respond("----------------------------")

                    else:
                        chunk_y_pos = chunk_y_pos + 1
                        gen_chunk(12, 12, chunk_seed[chunk_y_pos][chunk_x_pos])
                        await event.message.respond("Invalid move! (Invalid tile in other chunk)")
                        current_chunk[player_y_pos][player_x_pos] = 2
                        await event.message.respond(print_array(12, 12, current_chunk))
                        await event.message.respond("----------------------------")

                else:
                    await event.message.respond("Invalid move")

    @bot.listen()
    async def down(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        if event.message.content == "!down":
            global player_y_pos
            global chunk_y_pos
            if player_y_pos == h - 1:
                if chunk_y_pos < 2:
                    chunk_y_pos = chunk_y_pos + 1

                    gen_chunk(12, 12, chunk_seed[chunk_y_pos][chunk_x_pos])
                    if not invalid_tile_check(player_x_pos, 0):
                        player_y_pos = 0

                        current_chunk[player_y_pos][player_x_pos] = 2
                        await event.message.respond(print_array(12, 12, current_chunk))
                        await event.message.respond("----------------------------")

                    else:
                        chunk_y_pos = chunk_y_pos - 1
                        gen_chunk(12, 12, chunk_seed[chunk_y_pos][chunk_x_pos])
                        current_chunk[player_y_pos][player_x_pos] = 2
                        await event.message.respond(print_array(12, 12, current_chunk))
                        await event.message.respond("Invalid move! (invalid tile in another chunk")

                else:
                    await event.message.respond("Invalid move!")

            else:
                current_chunk[player_y_pos][player_x_pos] = chunk_seed[chunk_y_pos][chunk_x_pos]
                player_y_pos = player_y_pos + 1
                if not invalid_tile_check(player_x_pos, player_y_pos):
                    current_chunk[player_y_pos][player_x_pos] = 2
                    await event.message.respond(print_array(12, 12, current_chunk))
                    await event.message.respond("----------------------------")

                else:
                    player_y_pos = player_y_pos - 1
                    current_chunk[player_y_pos][player_x_pos] = 2
                    await event.message.respond(print_array(12, 12, current_chunk))
                    await event.message.respond("Invalid move! (invalid tile)")

    @bot.listen()
    async def left(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        if event.message.content == "!left":
            global player_x_pos
            global chunk_x_pos

            if player_x_pos > 0:
                current_chunk[player_y_pos][player_x_pos] = chunk_seed[chunk_y_pos][chunk_x_pos]
                player_x_pos = player_x_pos - 1
                if not invalid_tile_check(player_x_pos, player_y_pos):
                    current_chunk[player_y_pos][player_x_pos] = 2
                    await event.message.respond(print_array(12, 12, current_chunk))
                    await event.message.respond("----------------------------")

                else:
                    player_x_pos = player_x_pos + 1
                    await event.message.respond("Invalid Move! (Invalid Tile)")
                    current_chunk[player_y_pos][player_x_pos] = 2
                    await event.message.respond(print_array(12, 12, current_chunk))
                    await event.message.respond("----------------------------")

            else:
                if chunk_x_pos > 0:
                    chunk_x_pos = chunk_x_pos - 1
                    gen_chunk(12, 12, chunk_seed[chunk_y_pos][chunk_x_pos])
                    if not invalid_tile_check(player_x_pos, player_y_pos):
                        player_x_pos = 11

                        current_chunk[player_y_pos][player_x_pos] = 2
                        await event.message.respond(print_array(12, 12, current_chunk))
                        await event.message.respond("----------------------------")

                    else:
                        chunk_x_pos = chunk_x_pos + 1
                        gen_chunk(12, 12, chunk_seed[chunk_y_pos][chunk_x_pos])
                        await event.message.respond("Invalid move! (Invalid tile in other chunk)")
                        current_chunk[player_y_pos][player_x_pos] = 2
                        await event.message.respond(print_array(12, 12, current_chunk))
                        await event.message.respond("----------------------------")

                else:
                    await event.message.respond("Invalid move")

    @bot.listen()
    async def right(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        if event.message.content == "!right":
            global player_x_pos
            global chunk_x_pos
            if player_x_pos == h - 1:
                if chunk_x_pos < 2:
                    chunk_x_pos = chunk_x_pos + 1

                    gen_chunk(12, 12, chunk_seed[chunk_y_pos][chunk_x_pos])
                    if not invalid_tile_check(player_x_pos, 0):
                        player_x_pos = 0

                        current_chunk[player_y_pos][player_x_pos] = 2
                        await event.message.respond(print_array(12, 12, current_chunk))
                        await event.message.respond("----------------------------")

                    else:
                        chunk_x_pos = chunk_x_pos - 1
                        gen_chunk(12, 12, chunk_seed[chunk_y_pos][chunk_x_pos])
                        current_chunk[player_y_pos][player_x_pos] = 2
                        await event.message.respond(print_array(12, 12, current_chunk))
                        await event.message.respond("Invalid move! (invalid tile in another chunk")

                else:
                    await event.message.respond("Invalid move!")

            else:
                current_chunk[player_y_pos][player_x_pos] = chunk_seed[chunk_y_pos][chunk_x_pos]
                player_x_pos = player_x_pos + 1
                if not invalid_tile_check(player_x_pos, player_y_pos):
                    current_chunk[player_y_pos][player_x_pos] = 2
                    await event.message.respond(print_array(12, 12, current_chunk))
                    await event.message.respond("----------------------------")

                else:
                    player_x_pos = player_x_pos - 1
                    current_chunk[player_y_pos][player_x_pos] = 2
                    await event.message.respond(print_array(12, 12, current_chunk))
                    await event.message.respond("Invalid move! (invalid tile)")

    bot.run()


run()
