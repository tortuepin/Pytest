import os
import sys
import signal
import time
import threading

pid = os.fork()

if pid == 0:
    i = 1
    while True:
        print(i)
        time.sleep(2)
        i += 1
    sys.exit()
else:
    while True:
        c = sys.stdin.read(1)
        if c == ' ':
            os.kill( pid, signal.SIGTERM)
            sys.exit()



