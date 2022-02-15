import hidden
import lightbulb
import hikari

makka_pakka_img = "https://breedingbetterdogs.com/paulcosta/sites/default/files/styles/extra_large/public/field/" \
                  "image/Windows-default-shortcut-icon.png?itok=zkh2swTd"

guilds = [935674596726808576]

bot = lightbulb.BotApp(hidden.token, default_enabled_guilds=guilds, prefix="!", ignore_bots=True,
                       help_slash_command=True)


@bot.listen()
async def update_presence(event: hikari.StartedEvent) -> None:
    await bot.update_presence(status="dnd", activity=hikari.Activity(name="a game",
                                                                     type=hikari.ActivityType.WATCHING))


@bot.command
@lightbulb.command("ping", "checks that the bot is alive")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("Pong!")


@bot.command
@lightbulb.command("read", "shows player info")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def info(ctx: lightbulb.context) -> None:
    try:
        path = "player_data/Users/" + str(ctx.author.id) + "/data.json"
        with open(path) as file:
            pdata = json.load(file)

    except FileNotFoundError:
        await ctx.respond("Player data not found.")


@bot.command
@lightbulb.command("write", "creates player data")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def create(ctx: lightbulb.context) -> None:
    path = "player_data\Users\\" + str(ctx.author.id) + "\data.json"
    # os.makedir(path)
    # path = path + "/json"
    file = open(path, "w")
    file.close()


@bot.command
@lightbulb.command("makka_pakka", "makka pakka")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def info(ctx: lightbulb.context) -> None:
    embed = hikari.Embed(title="Embed Test", description="This is an embed test", color=0xFF0000)
    embed.set_author(name="Name", url="https://www.google.com/", icon=makka_pakka_img)
    embed.add_field(name="Username", value=ctx.author.username, inline=False)
    embed.add_field(name="Discriminator", value=ctx.author.discriminator, inline=False)
    embed.add_field(name="Avatar", value=ctx.author.avatar_url, inline=False)
    embed.set_footer(text="Footer Text", icon="https://m.media-amazon.com/images/M"
                                              "/MV5BMTUwOTQxOTE2OV5BMl5BanBnXkFtZTgwODQ4NDE0NzE@._V1_UY1200_CR752,0,"
                                              "630,1200_AL_.jpg")

    await ctx.respond(embed=embed)


bot.run()
