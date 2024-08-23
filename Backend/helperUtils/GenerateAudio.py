"""
Module Name: GenerateAudio.py
Author: Arun
"""
from gtts import gTTS
import os


def generate_audio(text, file_name="token_audio.mp3"):
    # Create a gTTS object with the given text and language
    tts = gTTS(text, lang='en')

    # Define the path to save the audio file
    file_path = os.path.join("static", "audio", file_name)

    # Save the generated speech to an MP3 file
    tts.save(file_path)

    # Return the file path of the saved audio
    return file_path
