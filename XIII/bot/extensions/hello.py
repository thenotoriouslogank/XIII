import lightbulb
import random
from XIII.bot import Bot

plugin = lightbulb.Plugin("hello")

@plugin.command
@lightbulb.command("hello", "Just sayin' hi.", aliases=("hi", "hey", "howdy"))
@lightbulb.implements(lightbulb.PrefixCommand)
async def hello(ctx: lightbulb.Context) -> None:
    greeting = random.choice(("Hello", "Hi", "Howdy", "Sup, bitch?"))
    await ctx.respond(f"{greeting} {ctx.member.mention}!", user_mentions=True)
def load(bot: Bot) -> None:
    bot.add_plugin(plugin)

def unload(bot: Bot) -> None:
    bot.remove_plugin(plugin)