import dotenv, os 
import src.setup as setup
import src.hash as hash
from datetime import date
from telethon import TelegramClient

# searching and loading .env 
dotenv.load_dotenv(dotenv.find_dotenv())

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

# creating a session to collect the data
session_name = "anon" 
client = TelegramClient(session_name, api_id, api_hash)
event = input("Enter the name of the dataset: ")

async def main():
    # get the file that contains the chanel's or group's ids
    channels_file = input("Enter the name of the csv of channels: ")
    channel_set = setup.read_chanels(channels_file)

    # create a file to write the hash code
    hash_file_name = input("Enter the name of the hash file: ")
    hash_file = open(hash_file_name, "a")
    hash_set = hash.hash_start(hash_file_name)

    # retrieve start and end date of dataset
    start_date = input("Enter the start date [dd/mm/yy]: ")
    start_date = datetime.strptime(start_date, "%d/%m/%Y")

    end_date = input("Enter the end date [dd/mm/yy]: ")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")

    # creates a dicionary to save the amount found of each media
    amount = {} 
   
    # creates a directory to store the media from channels and groups  
    if(not os.path.exists(f"./media-{event}/")):
        os.mkdir(f"./media-{event}/")

    total = 0
    downloaded = 0
    # iterates through each channel to collect the media
    for channel in channel_set:
        entity = await client.get_entity(channel)    
        media_path = f"./media-{event}/" + str(channel)
                
        # creates a directory with the id of the channel to store the media 
        if(not os.path.exists(media_path)):
            os.mkdir(media_path)

        async for message in client.iter_messages(entity = entity, offset_date = end_date):
            if message.date < start_date: break

            if (message.photo or message.video or message.voice or message.audio) and (not message.web_preview): 
                total+=1

                if hash.new_media(hash_set, message):
                    media_path = f"./media-{event}/" + str(channel)
                    media_path = setup.organize_files(media_path, message)

                    path = await message.download_media(file = media_path)
                    dst = setup.rename_files(message, path, media_path)

                    hash.update_set(hash_set, message)
                    hash.write_hash(hash_file, message, dst)                
                    downloaded+=1

                    # convert an image to webp format     
                    #if message.photo: 
                    #    setup.convert_to_webp(dst) 
                    
                hash.update_amount(message, amount)    
                    
    amount_file = open(f"./{event}-amount.csv", "a")
    hash.write_amount(amount_file, amount, total, downloaded)
        
    amount_file.close()
    hash_file.close()

with client:
    client.loop.run_until_complete(main())

#await client.log_out()