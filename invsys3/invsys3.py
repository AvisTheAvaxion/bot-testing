import json
import os
import hidden
from invSys3 import inventory
from invSys3 import json_stuff
from invSys3 import conveince
import lightbulb
import hikari


guilds = [935674596726808576, 911743102501421117]

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
@lightbulb.command("kill", "kills the bot")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def kill(ctx: lightbulb.Context) -> None:
    await ctx.respond("dieing")
    await bot.close()


@bot.command
@lightbulb.command("create", "creates base data")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def create(ctx: lightbulb.Context) -> None:
    os.makedirs("invSys3/Users/" + str(ctx.author.id) + "/")

    path = conveince.get_user_data_path(ctx.author.id, "inv.json")
    inventory.create_inventory(path)

    await ctx.respond("Inventory created!")


@bot.command
@lightbulb.command("inventory", "shows your inventory")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def show_inv(ctx: lightbulb.Context) -> None:
    inv = inventory.Inventory(conveince.get_user_data_path(ctx.author.id, "inv.json"))
    await ctx.respond(f"Inventory:\nItems: {inv.item_list}\nResource: {inv.resource_list}")

    embed = hikari.Embed(title="Inventory", description="Your items")
    for resource in inv.resource_list:
        embed.add_field(name=f"{resource.name}: {resource.amount}", value=resource.description, inline=False)

    for item in inv.item_list:
        pass

    await ctx.respond(embed=embed)


@bot.command
@lightbulb.option("name", "name")
@lightbulb.option("desc", "desc")
@lightbulb.option("amount", "amount")
@lightbulb.command("add_resource", "adds a resource")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def add_item(ctx: lightbulb.Context) -> None:
    inv = inventory.Inventory(conveince.get_user_data_path(ctx.author.id, "inv.json"))
    inv.add_resource(ctx.options.name, ctx.options.desc, ctx.options.amount)
    await ctx.respond("added! (hopefully)")



def run():
    bot.run()
