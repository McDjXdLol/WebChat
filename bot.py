import datetime
import random
from typing import Optional, Callable

from files import Files


class Bot:
    def __init__(self):
        self.prefix: str = "!"
        self.replies: dict[str, str] = {
            "info": "This is a simple, no-frills chat app side project — check out /about page for more info and fun facts!",
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

    @staticmethod
    def cmd_image(msg: str, **kwargs) -> str:
        return f'<img id="modalImg" src="{msg[len("!img "):].strip()}" alt="Image"/>'

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

    @staticmethod
    def cmd_dice(**kwargs) -> str:
        return str(random.randint(1, 6))

    def cmd_quote(self, **kwargs) -> str:
        return random.choice(self.quotes)

    def get_reply(self, msg: str) -> Optional[str]:
        if msg.startswith('/about'):
            print("Next idiot!")
            return "Nah 🤦 I mean /about page. You can find it in the bottom of this page."

        if not self.is_command(msg):
            return None

        command_line = msg[len(self.prefix):].strip()
        command_name = command_line.split()[0]

        command = self.commands.get(command_name)
        if command:
            func = command[0]
            return func(msg=msg)

        return None
