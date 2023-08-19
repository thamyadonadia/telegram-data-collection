import os, calendar, csv
from datetime import date
from PIL import Image
from pathlib import Path

def read_chanels(file_name):
    with open(file=file_name, mode = "r") as file:
        reader = csv.reader(file)
        channel_dict = {rows[0]:int(rows[1]) for rows in reader}
    return channel_dict

def organize_files(media_path, message):
    # creates a directory with the name of the chanel to store the media    
    date = message.date
    month = calendar.month_abbr[date.month] 
    media_path += "/" + month.lower() 
            
    if(not os.path.exists(media_path)):
        os.mkdir(media_path)
    
    return media_path

def rename_files(message, old_path, media_path):
    if message.photo:
        dst = str(media_path)+"/"+str(message.id)+".jpg"
        os.rename(str(old_path), dst)
    
    elif message.video:
        dst = str(media_path)+"/"+str(message.id)+".MP4"
        os.rename(str(old_path), dst)

    elif message.voice or message.audio:
        dst = str(media_path)+"/"+str(message.id)+".oga"
        os.rename(str(old_path), dst)
    
    return dst

def convert_to_webp(source):
    try: 
        path = Path(source)
        destination_path = path.with_suffix(".webp")
        image =Image.open(source)
        image.save(destination_path, format="WebP", quality=80)
    except IOError:
        print(f"An error occurred while opening or saving the image: {source}") 
        
