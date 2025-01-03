from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileMovedEvent
import time
import sqlite3

class MyHandler(FileSystemEventHandler):
    def __init__(self, file_types):
        self.file_types = file_types

    def should_watch(self, file_path): 
        # Check if the file has one of the specified extensions
        return file_path.endswith(tuple(self.file_types))

    def on_modified(self, event):
        if not event.is_directory and self.should_watch(event.src_path):
            conn = sqlite3.connect("files.db")
            c = conn.cursor()
            c.execute(f"UPDATE files SET isModded = 1 WHERE Path = '{event.src_path}'")
            print(f"{event.src_path} UPDATED")
            conn.commit()
            conn.close()
            

    def on_created(self, event):
        if not event.is_directory and self.should_watch(event.src_path):
            conn = sqlite3.connect("files.db")
            c = conn.cursor()
            c.execute(f"INSERT INTO files (Name, Path, isModded, Embedding) VALUES (?, ?, ?, ?)", (event.src_path.rsplit("/",1)[1], event.src_path, 0, "Null"))
            print(f"{event.src_path} CREATED")
            conn.commit()
            conn.close()

    def on_deleted(self, event):
        if not event.is_directory and self.should_watch(event.src_path):
            conn = sqlite3.connect("files.db")
            c = conn.cursor()
            c.execute(f"DELETE FROM files WHERE Path = '{event.src_path}'")
            print(f"{event.src_path} DELETED")
            conn.commit()
            conn.close()
            

    def on_moved(self, event):
        if isinstance(event, FileMovedEvent) and self.should_watch(event.dest_path):
            conn = sqlite3.connect("files.db")
            c = conn.cursor()
            c.execute(f"UPDATE files SET Path = '{event.dest_path}' WHERE Path = '{event.src_path}'")
            print(f"{event.src_path} MOVED {event.dest_path}")
            conn.commit()
            conn.close()

if __name__ == "__main__":
    path_to_watch = "/Users/lukewharton/"  # Replace with the path you want to monitor
    file_types_to_watch = (".txt", ".log", ".md", ".rtf", ".doc", ".docx", ".odt", ".wps", ".pdf", ".jpg", ".jpeg", ".png", ".ppt", ".pptx", ".odp", ".key", ".epub", ".mobi", ".axw3")

    
    event_handler = MyHandler(file_types_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)

    try:
        print(f"Monitoring changes in {path_to_watch} for {file_types_to_watch}...")
        observer.start()
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        print("Stopping observer...")
        observer.stop()

    observer.join()

