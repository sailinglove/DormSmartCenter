from card import readCard, loadTrusted
from door import doorOpen, doorClose
import threading, time

# --- presets ---

trustedIDPath = "final/IDs"
threadLock = threading.Lock()

# ---------------

# --- global variables ---

cardDetactExit = False
cardMatchFlag = False

# ------------------------


# --- cardDetection ---

trustedIDs = loadTrusted(trustedIDPath)

def cardDetect():
    global cardDetactExit
    global cardMatchFlag
    while not cardDetactExit:
        cardID = readCard()
        if cardID in trustedIDs:
            threadLock.acquire()
            cardMatchFlag = True
            threadLock.release()
            time.sleep(3)
        time.sleep(0.1)

cardDetectThread = threading.Thread(target=cardDetect)
cardDetectThread.setDaemon(True)

# ---------------------


# --- door ---

def doorListen():
    global cardMatchFlag
    while 1:
        if cardMatchFlag:
            doorOpen()
            threadLock.acquire()
            cardMatchFlag = False
            threadLock.release()
            time.sleep(3)
            doorClose()
        time.sleep(0.1)

doorListenThread = threading.Thread(target=doorListen)
doorListenThread.setDaemon(True)

# ------------


# --- main ---

cardDetectThread.start()
doorListenThread.start()

while 1:
    time.sleep(0.1)

# ------------