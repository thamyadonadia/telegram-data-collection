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
        hash_file.write(str(message.media.photo.access_hash) + "," + dst + "\n")
    else:
        hash_file.write(str(message.media.document.access_hash) + "," + dst + "\n")

def update_set(hash_set, message):
    if message.photo:
        hash_code = str(message.media.photo.access_hash)
        hash_set.add(hash_code)
    else:
        hash_code = str(message.media.document.access_hash)
        hash_set.add(hash_code)
    
    return hash_set

def new_media(hash_set, message):
    if message.photo:
        hash_code = str(message.media.photo.access_hash)
    
        if hash_code in hash_set:
            return False
    else:
        hash_code = str(message.media.document.access_hash)
        if hash_code in hash_set:
            return False
    
    return True