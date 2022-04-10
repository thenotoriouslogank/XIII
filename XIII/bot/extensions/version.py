import lightbulb
from XIII.bot import Bot
from XIII import __version__

plugin = lightbulb.Plugin("version")

@plugin.command
@lightbulb.command("version", "Returns bot version information.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def version(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"{__version__}")

def load(bot: Bot) -> None:
    bot.add_plugin(plugin)

def unload(bot: Bot) -> None:
    bot.remove_plugin(plugin)