from pytube import YouTube
from moviepy.editor import *

# Download the video using pytube
print("Introduzca la URL que quiere convertir")
url = input()
youtube = YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download()  # replace with your desired download directory

titulo = video.title
titulo = titulo.replace(":", "")

# Convert the downloaded video to mp3 and wav using moviepy
video_clip = VideoFileClip(titulo + ".mp4")  # replace with your downloaded video file name
audio = video_clip.audio


while True:
    print("Elige extensión: 1 - mp3 | 2 - wav | 3 - flac")
    ext = int(input())

    if ext == 1:
        audio.write_audiofile(titulo + ".mp3")  # mp3 file name
        break
    elif ext == 2:
        audio.write_audiofile(titulo + ".wav")  # wav file name
        break
    elif ext == 3:
        audio.write_audiofile(titulo + ".flac") # flac file name
        break
    else:
        print("Error, número incorrecto")