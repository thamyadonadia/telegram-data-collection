import dotenv
import os 
import datetime
import src.channel_url as channel_url
import src.channels as channels

from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterVideo

# searching and loading .env 
dotenv.load_dotenv(dotenv.find_dotenv())

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

session_name = input("Enter the name of the session: ")
print(session_name)
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    # get the file that contains the chanel's ou group's ids
    url_file = input("Enter the name of the file that contains the IDs: ")
    channel_dict = channels.read_chanels(url_file)

    # get the offset date -> messages previous to this date will be retrieved
    day, month, year = input("Enter the offset date: ").split("/")
    date = datetime.datetime(int(year), int(month), int(day))
    
    media_path = "./media/"

    for x in channel_dict:
        channel_id = channel_dict[x]
        
        # creates a directory with the name of the chanel to store the media 
        if(os.path.exists(media_path+x) == False):
            os.mkdir(media_path+x)
 
        async for message in client.iter_messages(channel_id, offset_date = date, filter=InputMessagesFilterPhotos):
            await message.download_media(media_path+x)

        async for message in client.iter_messages(channel_id, offset_date = date, filter=InputMessagesFilterVideo):
           await message.download_media(media_path+x)

        async for message in client.iter_messages(channel_id, offset_date = date, filter=InputMessagesFilterVoice):
            await message.download_media(media_path+x)


    # await client.log_out

with client:
    client.loop.run_until_complete(main())

