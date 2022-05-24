from pytube import YouTube
from time import sleep
from datetime import datetime

t1 = datetime.now()
link = input("pls enter video link: ") ##https://www.youtube.com/watch?v=vdouDiUU4fw
video = YouTube(link)

print(f"video title is: {video.title}")
_filename = input("pls enter the name of your mp3: ")
_filename = _filename + ".mp3"
print("-" * 49)

video.streams.get_by_itag(140).download(output_path="D:\Music", filename = _filename)

def done():
    t2 = datetime.now()
    print(f"done in {int((t2-t1).total_seconds())} Seconds")
    sleep(2)

video.register_on_complete_callback(done())

##_filename = input("pls enter the name of your mp3: ")
##for stream in video.streams:
##    print(stream)
