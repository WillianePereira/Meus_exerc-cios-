from turtle import title
from pytube import YouTube
url=input("Digite a url para download")
video= YouTube(url) 
video.streams.get_lowest_resolution().download()

#video.streams.filter(only_audio=true).first().download(
    #output_path )