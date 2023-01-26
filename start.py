import dotenv
import os 
import src.channels as channels

from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotoVideo
from telethon.tl.types import InputMessagesFilterVoice
#import telethon.utils as utils

# searching and loading .env 
dotenv.load_dotenv(dotenv.find_dotenv())

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

session_name = input("Enter the name of the session: ")
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    # get the file that contains the chanel's ou group's ids
    url_file = input("Enter the name of the file that contains the IDs: ")
    channel_dict = channels.read_chanels(url_file)
    
    # creates a directory to store the media from channels and groups  
    media_path = "./media/"
    if(os.path.exists(media_path) == False):
        os.mkdir(media_path)

    for x in channel_dict:
        channel_id = channel_dict[x]
        
        # creates a directory with the name of the chanel to store the media 
        if(os.path.exists(media_path+x) == False):
            os.mkdir(media_path+x)

        async for message in (client.iter_messages(channel_id, filter=InputMessagesFilterPhotoVideo)):
           await message.download_media(media_path+x)
        
        async for message in (client.iter_messages(channel_id, filter=InputMessagesFilterVoice)):
           await message.download_media(media_path+x)

        #async for message in (client.iter_messages(channel_id)):
        #    if (utils.is_audio(message) or utils.is_image(message) or utils.is_video(message)): 
        #        await message.download_media(media_path+x)
        
    # await client.log_out

with client:
    client.loop.run_until_complete(main())

