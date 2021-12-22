import os
import time

def loadTrusted(path: str):
    with open(path, 'r') as f:
        return f.readlines()

def readCard():
    bashOut = os.popen("nfc-list").read().split("\n")
    for i in bashOut:
        if "UID" in i:
            ID = i.lstrip("       UID (NFCID1): ").rstrip(" ")
    try:
        return ID
    except:
        return None

if __name__ == '__main__':
    while 1:
        print(readCard())
        time.sleep(0.5)