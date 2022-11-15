import dotenv
import os 
import datetime
import src.chanel_url as chanel_url
import src.chanels as chanels

from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import PhotoSize

# searching and loading .env 
dotenv.load_dotenv(dotenv.find_dotenv())

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

session_name = input("Enter the name of the session: ")
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    # get the file that contains the chanel's ou group's ids
    url_file = input("Enter the name of the file that contains the IDs: ")
    chanel_dict = chanels.read_chanels(url_file)

    # get the offset date -> messages previous to this date will be retrieved
    day, month, year = input("Enter the offset date: ").split("/")
    date = datetime.datetime(int(year), int(month), int(day))
    
    images_path = "./images/"

    for x in chanel_dict:
        chanel_id = chanel_dict[x]

        # creates a directory with the name of the chanel to store the images 
        if(os.path.exists(images_path+x) == False):
            os.mkdir(images_path+x)
        
        #TODO: PhotSize + 
        async for message in client.iter_messages(chanel_id, offset_date = date, filter=InputMessagesFilterPhotos):
            await message.download_media(images_path+x)

    # await client.log_out

with client:
    client.loop.run_until_complete(main())

#colocar as tarefas aqui
