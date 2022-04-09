from __future__ import annotations
from datetime import datetime

import sys

import logging
import os
from pathlib import Path

import hikari
import lightbulb
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import UTC

from XIII import __version__

log = open("log/log.txt", "a")

class Bot(lightbulb.BotApp):
    def __init__(self) -> None:
        self.scheduler = AsyncIOScheduler()
        self.scheduler.configure(timezone=UTC)

        with open("./secrets/token", mode="r", encoding="utf-8") as f:
            token = f.read()

        super().__init__(
            prefix="-",
            #insensitive_commands=True,
            token=token,
            intents=hikari.Intents.ALL,
        ),
    
    def run(self) -> None:
        self.event_manager.subscribe(hikari.StartingEvent, self.on_starting)
        self.event_manager.subscribe(hikari.StartedEvent, self.on_started)
        self.event_manager.subscribe(hikari.StoppingEvent, self.on_stopping)
        self.event_manager.subscribe(hikari.StoppedEvent, self.on_stopped)
        self.event_manager.subscribe(hikari.MessageCreateEvent, self.on_message_create)

        super().run(
            activity=hikari.Activity(
                name="with matches.",
                type=hikari.ActivityType.PLAYING
            ),
        )
    
    async def on_starting(self, event: hikari.StartingEvent) -> None:
        self.load_extensions_from("XIII/bot/extensions")
        logging.info(f"Extensions loaded")

    async def on_started(self, event: hikari.StartedEvent) -> None:
        self.scheduler.start()
        logging.info("BOT STARTED")
        timestamp = datetime.now()
        print(f"EVENT {timestamp}: Bot Started", file = log)

    async def on_stopping(self, event: hikari.StoppingEvent) -> None:
        pass
    
    async def on_stopped(self, event: hikari.StoppedEvent) -> None:
        self.scheduler.shutdown()
        timestamp = datetime.now()
        print(f"EVENT {timestamp}: Bot Stopped", file = log)
        log.close()

    async def on_message_create(self, event: hikari.MessageCreateEvent) -> None:
        if isinstance(event.message.channel_id, hikari.DMChannel):
            return

        logging.info(f"Message in {event.message.channel_id} by {event.message.author}: {event.message.content}")
        timestamp = datetime.now()
        print(f"MESSAGE {timestamp} in Channel {event.message.channel_id} from {event.message.author}: {event.message.content}", file = log)
