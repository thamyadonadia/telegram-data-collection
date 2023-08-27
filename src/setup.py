import os, calendar, csv
from datetime import date
from PIL import Image
from pathlib import Path

def read_chanels(file_name):
    channel_set = set()
    with open(file = file_name, mode = "r") as file:
        reader = csv.reader(file)
    
        for rows in reader:
            channel_set.add(int(rows[1]))

    file.close()
    return channel_set

def organize_files(media_path, message):
    # creates a directory with the month of the message    
    date = message.date
    month = calendar.month_abbr[date.month] 
    media_path += "/" + month.lower() 
            
    if(not os.path.exists(media_path)):
        os.mkdir(media_path)
    
    return media_path

def rename_files(message, old_path, media_path):
    if message.photo:
        dst = str(media_path)+"/"+str(message.media.photo.access_hash)+".jpg"
        os.rename(str(old_path), dst)
    
    elif message.video:
        dst = str(media_path)+"/"+str(message.media.document.access_hash)+".MP4"
        os.rename(str(old_path), dst)

    elif message.voice or message.audio:
        dst = str(media_path)+"/"+str(message.media.document.access_hash)+".oga"
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
        
