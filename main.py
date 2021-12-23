from card import readCard, loadTrusted
from door import doorOpen, doorClose
from light import lightOn, lightOff
from listen import listen
import commands as c
import threading, time

# --- presets ---

trustedIDPath = "IDs"
cardMatchLock = threading.Lock()
c._init()

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
            cardMatchLock.acquire()
            cardMatchFlag = True
            cardMatchLock.release()
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
            cardMatchLock.acquire()
            cardMatchFlag = False
            cardMatchLock.release()
            time.sleep(3)
            doorClose()
        time.sleep(0.1)

doorListenThread = threading.Thread(target=doorListen)
doorListenThread.setDaemon(True)

# ------------


# --- listen ---

listenThread = threading.Thread(target=listen)
listenThread.setDaemon(True)

# --------------


# --- voice control ---

def voiceControl():
    while True:
        commands = c.get_commands()
        # print(commands)
        if "开灯" in commands:
            lightOn()
            c.set_commands('')
        elif "关灯" in commands:
            lightOff()
            c.set_commands('')
        time.sleep(0.1)

voiceControlThread = threading.Thread(target=voiceControl)
voiceControlThread.setDaemon(True)

# ---------------


# --- main ---

cardDetectThread.start()
doorListenThread.start()
listenThread.start()
voiceControlThread.start()

while 1:
    time.sleep(0.1)

# ------------