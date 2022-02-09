import hidden
import lightbulb
import hikari

bot = lightbulb.BotApp(hidden.token, default_enabled_guilds=[935674596726808576])

@bot.command
@lightbulb.command("ping", "checks that the bot is alive")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("Pong!")

@bot.command
@lightbulb.command("hello", "says hello")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Hello {ctx.author.username}!")

@bot.command
@lightbulb.option("text", "text to repeat")
@lightbulb.command("echo", "repeats the given text")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.text)

@bot.command
@lightbulb.command("etest", "a callback to another bot")
@lightbulb.implements(lightbulb.SlashCommand)
async def etest(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title=ctx.author.username, description="IGN: Null",)  # creates profile embed
    embed.set_author(name="Name", url="https://www.google.com", icon=ctx.author.avatar_url)
    embed.add_field(name=f"Field1 Name", value="Field1 Value", inline=False)
    embed.add_field(name=f"Field2 Name", value="Field2 Value", inline=False)
    embed.set_footer(text="Footer Text", icon=ctx.author.avatar_url)
    await ctx.respond(embed=embed)
    await ctx.respond("test!")

bot.run()
