import speech_recognition as sr
import csv, os
from os import path
from pydub import AudioSegment

set_file = "./docs/hash.csv"
transcripts_path = "./transcripts/"
audio_set = {} 

if(not os.path.exists(transcripts_path)):
    os.mkdir(transcripts_path)

with open(file = set_file, mode = "r") as file:
    reader = csv.reader(file)
        
    for rows in reader:
        if(str(rows[3]) == "audio"):
            audio_set[str(rows[1])] = str(rows[0])

file.close()

for file in audio_set:
    # convert oga file to mp3
    sound_oga = AudioSegment.from_file(file)
    sound_mp3 = transcripts_path + audio_set[file] + ".mp3"
    sound_oga.export(sound_mp3, format="mp3")

    # convert mp3 file to wav                                                       
    sound = AudioSegment.from_mp3(sound_mp3)
    audio_name = transcripts_path + audio_set[file] + ".wav"
    sound.export(audio_name, format="wav")
    file_audio = sr.AudioFile(audio_name)
    
    # transcribe audio file
    r = sr.Recognizer()
    with file_audio as source:
        audio_text = r.record(source)
        text = r.recognize_google(audio_text,language='pt-BR') 

        text_file = open(transcripts_path + audio_set[file] + ".txt", "w")
        text_file.write(text)
        text_file.close()

