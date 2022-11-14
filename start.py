import dotenv
import os 
import src.chanel_url as chanel_url

from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import PhotoSize

# searching and loading .env 
dotenv.load_dotenv(dotenv.find_dotenv())

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

session_name = input("Enter the name of the ession: ")
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    url = input("Enter the URL of the chanel: ")
    chanel_id = chanel_url.url_treatment(url)
    file_path = "./images"
    
    #TODO: colocar um .txt com os links pra ele ler e coletar de cada canal no .txt
    #TODO: mexer com venv e entender o PhotoSize
    async for message in client.iter_messages(chanel_id, filter=InputMessagesFilterPhotos):
       #await message.download_media(file_path, thumb = PhotoSize(type = "webp", w = 300, h = 300, size = 0))
        await message.download_media(file_path)

    # await client.log_out

with client:
    client.loop.run_until_complete(main())
    
