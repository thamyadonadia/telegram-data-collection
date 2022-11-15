import csv

def read_chanels(file_name):
    with open(file=file_name, mode = "r") as file:
        reader = csv.reader(file)
        channel_dict = {rows[0]:int(rows[1]) for rows in reader}
    return channel_dict

