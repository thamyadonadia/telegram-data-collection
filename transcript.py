import speech_recognition as sr
import csv, os
from pydub import AudioSegment

event = input("Enter the name of the dataset: ")
set_file = input("Enter the name of the hash file: ")
transcripts_path = f"./transcripts-{event}/"
audio_set = {} 

if(not os.path.exists(transcripts_path)):
    os.mkdir(transcripts_path)

with open(file = set_file, mode = "r") as file:
    reader = csv.reader(file)
        
    for rows in reader:
        if(str(rows[2]) == "audio"): # or str(rows[2]) == "video"
            audio_set[str(rows[1])] = str(rows[0])

file.close()

for file in audio_set:

    if not os.path.exists(f"{file}.txt"):
        # convert audio/voice file to .wav
        sound_oga = AudioSegment.from_file(file)
        audio_name = transcripts_path + audio_set[file] + ".wav"
        sound_oga.export(audio_name, format="wav")
        file_audio = sr.AudioFile(audio_name)
        
        # transcribe audio file
        r = sr.Recognizer()
        with file_audio as source:
            audio_text = r.record(source)
            text = r.recognize_google(audio_text, language='pt-BR') 
            text_file = open(transcripts_path + audio_set[file] + ".txt", "w")
            text_file.write(text)
            text_file.close()

