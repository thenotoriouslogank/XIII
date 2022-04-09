import lightbulb
from XIII.bot import Bot

plugin = lightbulb.Plugin("shutdown")

@plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("shutdown", "Gracefully closes the bot.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def shutdown(ctx: lightbulb.Context) -> None:
    await ctx.respond("Goodbye!")
    await ctx.bot.close()

def load(bot: Bot) -> None:
    bot.add_plugin(plugin)

def unload(bot: Bot) -> None:
    bot.remove_plugin(plugin)