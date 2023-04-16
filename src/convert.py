from pathlib import Path
from PIL import Image

def convert_to_webp(source, path):
    destination = source.with_suffix(".webp")
    try: 
        with Image.open(source) as im:
            im.save(destination, path= path, format="webp")
    except OSError:
        print("cannot convert", source)
