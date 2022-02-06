import hikari
import hidden


def run():
    bot = hikari.GatewayBot(token=hidden.token)

    @bot.listen()
    async def show_array(event: hikari.GuildMessageCreateEvent) -> None:

        if event.is_bot or not event.content:
            return

        if event.message.content == "!test":
            await event.message.respond("CatLol: <:catlul:939679225714180127>")
            await event.message.respond(":CatPog: <:catpog:939679298426642453>")
            await event.message.respond(":CatLove: <:catlove:939679349068681226>")
            await event.message.respond("CatLost: <:catlost:939679266117943336>")

    bot.run()
