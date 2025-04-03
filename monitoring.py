import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from process_file import process_file


# The folder where misc files will be added
WATCH_FOLDER = "/MagicFolder/Inbox"


# Handle a newly added file
class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return  # skip directories
        filepath = event.src_path
        print(f"New file detected: {filepath}")
        process_file(filepath)  # call processing function

# Set up observer
observer = Observer()
observer.schedule(NewFileHandler(), path=WATCH_FOLDER, recursive=False)
observer.start()
print(f"Watching folder: {WATCH_FOLDER}")

# Main loop
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
