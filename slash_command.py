import hidden
import lightbulb

bot = lightbulb.BotApp(hidden.token)


@bot.command
@lightbulb.command("ping", "checks that the bot is alive")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("Pong!")

bot.run()