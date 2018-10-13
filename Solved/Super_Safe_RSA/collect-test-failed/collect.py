#!/usr/bin/env python3
import socket
from queue import Queue
from threading import Thread, Lock
import time

THREADS = 100

lock = Lock()

def write_file(txt):
    global lock
    with lock:
        with open("out.txt", "a") as f:
            f.write(txt)


def process(q):
    while True:
        print("Doing", q.get())
        while True:
            try:
                s = socket.socket()
                s.connect(('2018shell2.picoctf.com', 3609))

                data = s.recv(4096).decode().strip()
                if data:
                    write_file(data.replace(":", " =") + "\n\n")
                    q.task_done()
                    break
            except:
                time.sleep(1)


def start_threads():
    queue = Queue(maxsize=0)

    for i in range(THREADS):
        worker = Thread(target=process, args=(queue,))
        worker.setDaemon(True)
        worker.start()

    for i in range(65600):
        queue.put(i)
    queue.join()


if __name__ == '__main__':
    start_threads()
