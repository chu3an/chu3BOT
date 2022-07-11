from os import getenv

from dotenv import load_dotenv
from twitchio.ext import commands

load_dotenv()

TOKEN = getenv('TOKEN')
CLIENT_ID = getenv('CLIENT_ID')
CLIENT_SECRET = getenv('CLIENT_SECRET')
PREFIX = getenv('PREFIX')
CHANNEL = getenv('CHANNEL')


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=TOKEN, prefix=PREFIX,
                         initial_channels=[CHANNEL])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def test(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name} 尼豪 chu3anGood')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        print('[{channel}]{author}: {message}'.format(
            channel=message.channel.name,
            author=message.author.name,
            message=message.content
        ))
        print(message.author.is_broadcaster)
        
        # Print the contents of our message to console...
        # print(message.content)
        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...

        await self.handle_commands(message)


def main():
    bot = Bot()
    bot.run()


if __name__ == '__main__':
    main()
