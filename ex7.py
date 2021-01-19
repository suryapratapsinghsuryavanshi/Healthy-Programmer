"""
Healthy Programmer -
9am-5pm
water - water.mp3  (3.5 liters) - Drank - log
eyes - eyes.mp3 - every 30 min - EyDone - log
physical activity - physical.mp3 every - 45 min ExDone - log

Rule
- solve time conflict.
- play audio using pygame module.
"""
from pygame import mixer
import time
mixer.init()
mixer.music.set_volume(0.5)


def stamp():
    return time.asctime(time.localtime())


def water():
    mixer.music.load("water.mp3")
    mixer.music.play(20)
    q = input("Write Drank :- ")
    if q == "Drank":
        mixer.music.pause()
        file = open("water.txt", "a")
        file.write(f"[ {stamp()} ] - Drink Water.\n")
        file.close()
    else:
        water()


def eyes():
    mixer.music.load("eyes.mp3")
    mixer.music.play(20)
    q = input("Write EyDone :- ")
    if q == "EyDone":
        mixer.music.pause()
        file = open("eyes.txt", "a")
        file.write(f"[ {stamp()} ] - Eyes Ex Done.\n")
        file.close()
    else:
        eyes()


def physical():
    mixer.music.load("physical.mp3")
    mixer.music.play(20)
    q = input("Write ExDone :- ")
    if q == "ExDone":
        mixer.music.pause()
        file = open("physical.txt", "a")
        file.write(f"[ {stamp()} ] - Physical Ex Done.\n")
        file.close()
    else:
        physical()


if __name__ == '__main__':
    while True:
        time.sleep(22 * 60)  # 18/8 = 2.25 = each 20 min after
        water()
        time.sleep(8*60)    # 22 + 8 = 30 min
        eyes()
        time.sleep(10*60)   # 30 + 10 = 40 min
        physical()
