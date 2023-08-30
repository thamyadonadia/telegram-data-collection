import csv

def hash_start(file_name):
    hash_set = set()

    with open(file = file_name, mode = "r") as file:
        reader = csv.reader(file)
        
        for rows in reader:
            hash_set.add(str(rows[0]))

    file.close()
    return hash_set

def write_hash(hash_file, message, dst):
    if message.photo:
        hash_file.write(str(message.media.photo.access_hash) + "," + dst + "," + "photo\n")

    elif message.document.mime_type: 
        if ".mp4" in str(message.file.name): 
            hash_file.write(str(message.document.access_hash) + "," + dst + "," + "gif\n")
        
        elif ".webp" in str(message.file.name): 
            hash_file.write(str(message.document.access_hash) + "," + dst + "," + "sticker\n")

    elif message.video:
        hash_file.write(str(message.media.document.access_hash) + "," + dst + "," + "video\n")

    elif message.voice or message.audio:
        hash_file.write(str(message.media.document.access_hash) + "," + dst + "," + "audio\n")

    
def update_set(hash_set, message):
    if message.photo:
        hash_code = str(message.media.photo.access_hash)
        hash_set.add(hash_code)

    elif message.document.mime_type: 
        hash_code = str(message.document.access_hash)
        hash_set.add(hash_code) 

    else:
        hash_code = str(message.media.document.access_hash)
        hash_set.add(hash_code)

    
def new_media(hash_set, message):
    if message.photo:
        hash_code = str(message.media.photo.access_hash)
        if hash_code in hash_set:
            return False  
         
    elif message.document.mime_type: 
        hash_code = str(message.document.access_hash)
        if hash_code in hash_set:
            return False  

    else:
        hash_code = str(message.media.document.access_hash)
        if hash_code in hash_set:
            return False
    
    return True

def update_amount(message, amount):
    if message.photo: 
        hash_code = str(message.media.photo.access_hash)
        if hash_code in amount: 
            amount[hash_code] += 1
        else: 
            amount[hash_code] = 1

    elif message.document.mime_type: 
        hash_code = str(message.document.access_hash)
        if hash_code in amount: 
            amount[hash_code] += 1
        else: 
            amount[hash_code] = 1

    else: 
        hash_code = str(message.media.document.access_hash)
        if hash_code in amount: 
            amount[hash_code] += 1
        else: 
            amount[hash_code] = 1

def write_amount(amount_file, amount, total, downloaded): 
    for hash_code in amount: 
        amount_file.write(str(hash_code) + "," + str(amount[hash_code]) + "\n")
    
    amount_file.write(f"Total: {total}, Downloaded: {downloaded}")


