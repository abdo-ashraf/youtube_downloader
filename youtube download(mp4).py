from pytube import YouTube
from time import sleep
from datetime import datetime

t1 = datetime.now()
link = input("pls enter video link: ")
video = YouTube(link)

print(f"video title is: {video.title}")
boolname = input("want to change filename?(yes/no) ").lower()
if boolname in ["y","yes"]:
    _filename = input("pls enter the name of your mp4: ")
    _filename = _filename + ".mp4"
else:
    _filename = None
print("-" * 49)
print("# NOTE 144p only 6 fps but 360p and 720p 25 fps #")
print("-" * 49)
itag = int(input("choose your quality( 17 -> 144p, 18 -> 360p, 22 ->720p): "))
if itag not in [17,18,22]:
    print("wrong itag")
    itag = int(input("17 -> 144p, 18 -> 360p, 22 ->720p: "))

video.streams.get_by_itag(itag).download(output_path = "D:\Videos", filename = _filename)

def done():
    t2 = datetime.now()
    print(f"done in {int((t2-t1).total_seconds())} Seconds")
    sleep(2)

video.register_on_complete_callback(done())
