from pytube import YouTube
import subprocess
import os
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.2.0')

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def converter(self):
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
                self.url_label.text = str("Conversion Successful")
            except subprocess.CalledProcessError as e:
                self.url_label.text = str("Conversion Failed")

        my_video = YouTube(self.url_label.text)

        my_video = my_video.streams.get_lowest_resolution()
        my_video.download(filename="song.mp4")

        output_file_name = my_video.title + ".mp3"

        convert_video_to_mp3("song.mp4", output_file_name)
        os.remove("song.mp4")

class YTdownloader(App):
    def build(self):
        return MyRoot()

ytdl = YTdownloader()
ytdl.run()