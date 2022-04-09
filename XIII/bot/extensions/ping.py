import lightbulb
from XIII.bot import Bot

plugin = lightbulb.Plugin("ping")

@plugin.command
@lightbulb.command("ping", "Checks bot latency.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"**Latency**: {ctx.bot.heartbeat_latency * 1_000:,.0f} ms.")

def load(bot: Bot) -> None:
    bot.add_plugin(plugin)

def unload(bot: Bot) -> None:
    bot.remove_plugin(plugin)