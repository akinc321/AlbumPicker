from pytube import YouTube
import os


# create video object
yt = YouTube(str(input("Enter video URL: \n>> ")))

# extract only audio
audio = yt.streams.filter(only_audio=True).first()

# save to desktop video file
destination = str(os.path.expanduser(r"~\Desktop"))+r"\Videos"

# download the file
out_file = audio.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)

# final success printout
print(yt.title + " has been downloaded to " + destination + ".")