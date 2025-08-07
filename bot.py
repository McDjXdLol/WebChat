import datetime
import random
from typing import Optional, Callable
from files import Files


class Bot:
    def __init__(self):
        self.prefix: str = "!"
        self.replies: dict[str, str] = {
            "info": "I'm a web bot!",
        }

        self.commands: dict[str, tuple[Callable[..., Optional[str]], str]] = {
            "info": (self.cmd_info, "Send info about bot"),
            "help": (self.cmd_help, "Show this help menu"),
            "time": (self.cmd_time, "Show current time"),
            "echo": (self.cmd_echo, "Echo back your message"),
            "joke": (self.cmd_joke, "Tells a random joke"),
            "roll": (self.cmd_dice, "Rolls a dice"),
            "quote": (self.cmd_quote, "Tells a random quote"),
            "img": (self.cmd_image, "<URL> Displays an image from the provided URL in the chat.")
        }

        files = Files()
        self.jokes = files.read_jokes()
        self.quotes = files.read_quotes()

    def is_command(self, msg: str) -> bool:
        return msg.startswith(self.prefix)

    def cmd_image(self, msg: str, **kwargs) -> str:
        return f"<img src='{msg[len("!img "):].strip()}'>"

    def cmd_info(self, msg: str, **kwargs) -> str:
        return self.replies.get(msg[1:], "No info available.")

    def cmd_help(self, **kwargs) -> str:
        return "\n".join([f"!{name} - {desc}" for name, (_, desc) in self.commands.items()])

    @staticmethod
    def cmd_time(**kwargs) -> str:
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")

    def cmd_echo(self, msg: str, **kwargs) -> str:
        return msg[len(self.prefix + "echo"):].strip()

    def cmd_joke(self, **kwargs) -> str:
        return random.choice(self.jokes)

    def cmd_dice(self, **kwargs) -> str:
        return str(random.randint(1, 6))

    def cmd_quote(self, **kwargs) -> str:
        return random.choice(self.quotes)

    def get_reply(self, msg: str) -> Optional[str]:
        if not self.is_command(msg):
            return None

        command_line = msg[len(self.prefix):].strip()
        command_name = command_line.split()[0]

        command = self.commands.get(command_name)
        if command:
            func = command[0]
            return func(msg=msg)

        return None
