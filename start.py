import dotenv, os 
import src.channels as channels
import src.setup as setup
import src.hash as hash

from telethon import TelegramClient

# searching and loading .env 
dotenv.load_dotenv(dotenv.find_dotenv())

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

session_name = "20jan"
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    # get the file that contains the chanel's ou group's ids
    channels_file = "./in/channels.csv"
    channel_dict = channels.read_chanels(channels_file)
    hash_set = hash.hash_start("./docs/hash.csv")
    hash_file = open("./docs/hash.csv", "a")
    
    # creates a directory to store the media from channels and groups  
    if(not os.path.exists("./media/")):
        os.mkdir("./media/")

    for x in channel_dict:
        channel_id = channel_dict[x]
        media_path = "./media/" + str(channel_id)
                
        # creates a directory with the name of the chanel to store the media 
        if(not os.path.exists(media_path)):
            os.mkdir(media_path)

        async for message in client.iter_messages(channel_id):
            
            if (message.photo or message.video or message.voice or message.audio) and (not message.web_preview): 
                
                if hash.new_media(hash_set, message):
                    media_path = "./media/" + str(channel_id)
                    media_path = setup.organize_files(media_path, message)
                    path = await message.download_media(media_path)
                    dst = setup.rename_files(message, path, media_path)
                    hash.write_hash(hash_file, message, dst)
                    hash_set = hash.update_set(hash_set, message)               
    
    hash_file.close()

with client:
    client.loop.run_until_complete(main())

    # await client.log_out