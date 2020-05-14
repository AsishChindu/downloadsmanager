from watchdog.observers import Observer
from watchdog.events import  FileSystemEventHandler

import os 
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            
            path = folder_to_track + "/" + filename
            
            if not os.path.isdir(path):

                imagesExt = ["jpeg","jpg","png","svg"]
                documentsExt = ["pdf","doc","docx","xls","xlsx","ppt","pptx","txt","ods"]
                audiosExt = ["mp3","wav","wma","aac","flac"]
                videosExt = ["mkv","mp4","webm","mpeg","vob","avi","mov"]

                extension = filename[filename.rindex(".")+1:].lower()

                if imagesExt.count(extension):
                    directory = "Images"
                elif videosExt.count(extension):
                    directory = "Videos"
                elif audiosExt.count(extension):
                    directory = "Audios"
                elif documentsExt.count(extension):
                    directory = "Documents"
                else:
                    directory = "Others"

                path = os.path.join(folder_to_track, directory)

                isdir = os.path.isdir(path)
                if not isdir:
                    os.mkdir(path)

                src = folder_to_track + "/" + filename
                new_destination = path + "/" + filename
                os.rename(src, new_destination)

folder_to_track = "/home/asish/Music/Test"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    
observer.join()