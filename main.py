from typing import Final
import os
from dotenv import load_dotenv 
from discord import Intents, Client, Message
from responses import get_response

#step_0: load token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#step_1: setup intents
intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)

#step_2: message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was not enabled because intents were probably not enabled properly')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

#step_3: handling the startup for our bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')

#step_4: handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#step_5: main entry point

def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
