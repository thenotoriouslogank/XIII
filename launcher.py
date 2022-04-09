from XIII import __version__
from XIII.bot import Bot

import os

if os.name != "nt":
    import uvloop
    uvloop.install()

if __name__ == '__main__':
    bot = Bot()
    bot.run()