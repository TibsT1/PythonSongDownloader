from pytube import YouTube
import subprocess
import os

def convert_video_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "128k",
        "-ar", "44100",
        "-y",
        output_file
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Conversion Successful")
    except subprocess.CalledProcessError as e:
        print("Conversion Failed")

url = input("Enter the URL of the video:\n")

my_video = YouTube(url)

my_video = my_video.streams.get_lowest_resolution()
my_video.download(filename="song.mp4")

output_file_name = my_video.title + ".mp3"

convert_video_to_mp3("song.mp4", output_file_name)
os.remove("song.mp4")