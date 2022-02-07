import hikari
import random
import hidden

player_x_pos = 0
player_y_pos = 0

chunk_x_pos = 0
chunk_y_pos = 0

w, h = 3, 3
chunk_cont = [[0 for x in range(w)] for y in range(h)]

w, h = 12, 12
current_chunk = [[0 for x in range(w)] for y in range(h)]

chunk_border = "----------------------------"


# seed generation
def make_arr(h1, w1, arr, rand, v):
    f = 1
    for i in range(h1):
        for i1 in range(w1):
            if rand:
                arr[i][i1] = f
                f = f + 1

            else:
                arr[i][i1] = v


make_arr(3, 3, chunk_cont, True, None)


# Rendering engine
def print_array(h1, w1, matrix):
    s = ""
    for i in range(h1):
        for i1 in range(w1):
            s = s + str(matrix[i][i1])

        s = s + "\n"

    return s


# chunk generation from seed
def chunk_gen(h1, w1, v):
    for i in range(h1):
        for i1 in range(w1):
            current_chunk[i][i1] = v


chunk_gen(12, 12, 0)
current_chunk[0][0] = "p"


def run():
    bot = hikari.GatewayBot(token=hidden.token)

    @bot.listen()
    async def show_array(event: hikari.GuildMessageCreateEvent) -> None:

        if event.is_bot or not event.content:
            return

        if event.message.content == "!show":
            await event.message.respond(print_array(12, 12, current_chunk))
            await event.message.respond(chunk_border)\


    @bot.listen()
    async def up(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        if event.message.content == "!up":
            global current_chunk
            global chunk_y_pos
            global player_y_pos
            if player_y_pos > 0:
                current_chunk[player_y_pos][player_x_pos] = 0
                player_y_pos = player_y_pos - 1
                current_chunk[player_y_pos][player_x_pos] = "p"
                await event.message.respond(print_array(12, 12, current_chunk))

            else:
                if chunk_y_pos > 0:
                    chunk_y_pos = chunk_y_pos - 1
                    chunk_gen(12, 12, chunk_cont[chunk_y_pos, chunk_x_pos])

                else:
                    await event.message.respond("Invalid move")

    @bot.listen()
    async def down(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        if event.message.content == "!down":
            global chunk_y_pos
            global player_y_pos
            if player_y_pos == 11:
                if chunk_y_pos < 2:
                    chunk_y_pos = chunk_y_pos + 1
                    chunk_gen(12, 12, chunk_cont[chunk_y_pos, chunk_x_pos])

                else:
                    await event.message.respond("Invalid move")


            else:
                current_chunk[player_y_pos][player_x_pos] = 0
                player_y_pos = player_y_pos + 1
                current_chunk[player_y_pos][player_x_pos] = "p"
                await event.message.respond(print_array(12, 12, current_chunk))


    bot.run()

run()
