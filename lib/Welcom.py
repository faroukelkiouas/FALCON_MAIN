# /etc/init.d/sample.py
### BEGIN INIT INFO
# Provides:          welcom.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO



import pyttsx3 # Text to Speech Library
engine = pyttsx3.init() # object creation
import pygame
import time
#Speech Variables:
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',10.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[2].id)   #changing index, changes voices. 1 for female
time.sleep(2)
pygame.mixer.init()
pygame.mixer.music.load('/home/pi/FAalcon/lib/entrance.mp3')
pygame.mixer.music.play()
time.sleep(2)
engine.say("Hello everybody")
engine.say("seems there is something to be done today!")
engine.runAndWait()
engine.stop()
