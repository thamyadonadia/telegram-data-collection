import dotenv
import os 

from telethon import TelegramClient

# procurando e carregando .env na mesma pasta
dotenv.load_dotenv(dotenv.find_dotenv())

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('@AfonsoSalvador', 'oiiiiiiiiiiiiiiiiii'))