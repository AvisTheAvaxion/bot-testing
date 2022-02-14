import hidden
import lightbulb
import hikari

guilds = [935674596726808576]

bot = lightbulb.BotApp(hidden.token, default_enabled_guilds=guilds, prefix="!", ignore_bots=True,
                       help_slash_command=True)


@bot.listen()
async def update_presence(event: hikari.StartedEvent) -> None:
    await bot.update_presence(status="dnd", activity=hikari.Activity(name="Forb play with himself",
                                                                     type=hikari.ActivityType.WATCHING))


@bot.command
@lightbulb.command("ping", "checks that the bot is alive")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("Pong!")


@bot.command
@lightbulb.command("hello", "says hello")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def hello(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Hello {ctx.author.username}!")


@bot.command
@lightbulb.option("text", "text to repeat")
@lightbulb.command("echo", "repeats the given text")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def echo(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.text)


@bot.command
@lightbulb.command("etest", "a callback to another bot")
@lightbulb.implements(lightbulb.SlashCommand)
async def etest(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title=ctx.author.username, description="IGN: Null", )  # creates profile embed
    embed.set_author(name="Name", url="https://www.google.com", icon=ctx.author.avatar_url)
    embed.add_field(name=f"Field1 Name", value="Field1 Value", inline=False)
    embed.add_field(name=f"Field2 Name", value="Field2 Value", inline=False)
    embed.set_footer(text="Footer Text", icon=ctx.author.avatar_url)
    await ctx.respond(embed=embed)
    await ctx.respond("test!")

makka_pakka_img = "https://m.media-amazon.com/images/M/MV5BMTUwOTQxOTE2OV5BMl5BanBnXkFtZTgwODQ4NDE0NzE" \
                  "@._V1_UY1200_CR752,0,630,1200_AL_.jpg "


@bot.command
@lightbulb.command("embed_test", "an embed test")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def etest2(ctx: lightbulb.context) -> None:
    embed = hikari.Embed(title="Embed Test", description="This is an embed test", color=0xFF0000)
    embed.set_author(name="Name", url=makka_pakka_img, icon=makka_pakka_img)
    embed.add_field(name="Username", value=ctx.author.username, inline=False)
    embed.add_field(name="Discriminator", value=ctx.author.discriminator, inline=False)
    embed.add_field(name="Avatar", value=ctx.author.avatar_url, inline=False)
    embed.set_footer(text="Footer Text", icon="https://m.media-amazon.com/images/M"
                                              "/MV5BMTUwOTQxOTE2OV5BMl5BanBnXkFtZTgwODQ4NDE0NzE@._V1_UY1200_CR752,0,"
                                              "630,1200_AL_.jpg")

    await ctx.respond(embed=embed)


bot.run()
