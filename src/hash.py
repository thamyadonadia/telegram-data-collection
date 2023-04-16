def compare(message, file_name):
    if message.photo:
        print(message.media.photo.access_hash)
    else:
        print(message.media.document.access_hash)
