import os, calendar
from datetime import date

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
        os.rename(str(old_path), str(media_path)+"/"+str(message.id)+".jpg")
    if message.video:
        os.rename(str(old_path), str(media_path)+"/"+str(message.id)+".MP4")
    if message.voice:
        os.rename(str(old_path), str(media_path)+"/"+str(message.id)+".oga")
     
            
