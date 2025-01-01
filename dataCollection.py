import os
import sqlite3


INCLUDE = (".txt", ".log", ".md", ".rtf", ".doc", ".docx", ".odt", ".wps", ".pdf", ".jpg", ".jpeg", ".png", ".ppt", ".pptx", ".odp", ".key", ".epub", ".mobi", ".axw3")


def findAllFiles(path='/Users/lukewharton/') -> list[str]:

    file_list = []
    for root, _, files in os.walk(path, topdown=True):
        files[:] = [f for f in files if f.endswith(INCLUDE)]

        for file in files:
            name = file
            path = os.path.join(root, file)
            ismod = 0
            embed = "Null"
            file_list.append((name, path, ismod, embed))
        
        

    return file_list



def firstLoadDB():
    conn = sqlite3.connect("files.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS files (Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Path TEXT, isModded TINYINT, Embedding TEXT)")

    files = findAllFiles()

    c.executemany("INSERT INTO files (Name, Path, isModded, Embedding) VALUES (?, ?, ?, ?)", files)
    conn.commit()
    conn.close()


def getChanges():
    conn = sqlite3.connect("files.db")
    c = conn.cursor()
    c.execute("SELECT Name, Path FROM files WHERE isModded = 1")
    res = c.fetchall()
    conn.close()
    return res


def getCurrent(query: str):
    conn = sqlite3.connect("files.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM files WHERE Name LIKE '{query}%'")
    res = c.fetchall()
    conn.close()
    return res

if __name__ == "__main__":
    firstLoadDB()
