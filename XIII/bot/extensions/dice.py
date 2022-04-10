import lightbulb
from XIII.bot import Bot

plugin = lightbulb.Plugin("roll", "Rolls dice.")

@plugin.command
@lightbulb.command("roll", "Rolls arbitrary dice.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def roll(ctx: lightbulb.Context, dice: str) -> None:
    rawRoll=dice.split("d")
    print(rawRoll[1])
    print(rawRoll[2])

def load(bot: Bot) -> None:
    bot.add_plugin(plugin)

def unload(bot: Bot) -> None:
    bot.remove_plugin(plugin)