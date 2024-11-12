import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nSo love me like you do", 0.10),
        ("La-la-love me like you do", 0.10),
        ("love me like you do", 0.10),
        ("La-la-love me like you do", 0.10),
        ("Touch me like you do", 0.10),
        ("Ta-ta-touch me like you do", 0.15),
        ("\nWhat are you waiting for?", 0.17),
        ("Fading in,fading out", 0.12),
        ("On the edge of paradise", 0.11),
        ("Every inch of your skin is a holy grail", 0.11),
        ("I've got to find", 0.15),
        ("Only you can set my heart", 0.14),
    ]
    delays = [0.3, 1.7, 3.0, 4.5, 6.0, 9.5, 13.9, 14.9, 15.7, 17.0, 18.5, 22.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()