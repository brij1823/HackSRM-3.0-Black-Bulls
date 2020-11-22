from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.core.files.storage import default_storage


#Custom Libs
import os
from moviepy.editor import *
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS 
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.editor as mpe
import pytube
from pytube import YouTube
# Create your views here.

r = sr.Recognizer()
translator = Translator()
hindi_text = ""
class Home(TemplateView):
    template_name = 'home.html'


    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
      recognize_google(audio_listened,language="fr-FR")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                #text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                text+="."
                inter_text = translator.translate(text,dest = 'hi')
                print(inter_text.text)
                hindi_text+=inter_text.text
                whole_text += text
    # return the text for all chunks detected
    return hindi_text