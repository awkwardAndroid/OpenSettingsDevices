# This program is written by Jesse Valo
# This is "caveman code" and could be improved, but it works as intended.

from ctypes import *
from time import sleep

user = windll.user32

# This DELAY is used between key(press/release) events
DELAY = 0.01

# These keys are mapped on a finnish/swedish keyboard,
# so there is a great possibility that they wont work with your keyboard.
#
# I used a very simple program called "KeyboardStateView" to get the hex codes.
# You can google the program name or use this link https://www.nirsoft.net/utils/keyboard_state_view.html
# ------------------------------------------------------------------------

class Key:
    # Other Keys
    win = 0x5B # Windows key
    enter = 0x0D
    dash = 0xBD # dash/minus key(-)
    dot = 0xBE
    shift = 0x10

    # Character Keys (not in order)
    r = 0x52
    m = 0x4D
    s = 0x53
    e = 0x45
    t = 0x54
    i = 0x49
    n = 0x4E
    g = 0x47
    d = 0x44
    v = 0x56
    c = 0x43

# Hex codes placed in a list in an inteded order.
# This order will type out " ms-settings.devices " , and later the dot will be changed to colon(:) with the use of a shift key
hex_list = [Key.m, Key.s, Key.dash, Key.s, Key.e, Key.t, Key.t, Key.i, Key.n, Key.g, Key.s, Key.dot, Key.d, Key.e, Key.v, Key.i, Key.c, Key.e, Key.s, Key.enter]

# Press and release two keys
def pressTwoKeys(key1,key2):
    sleep(DELAY)
    user.keybd_event(key1,0,0,0)
    sleep(DELAY)
    user.keybd_event(key2,0,0,0)
    sleep(DELAY)
    user.keybd_event(key1,0,2,0)
    user.keybd_event(key2,0,2,0)
    sleep(DELAY)

# Press and release one key
def press(key):
    user.keybd_event(key,0,0,0)
    sleep(DELAY)
    user.keybd_event(key,0,2,0)
    sleep(DELAY)

def write(hex_list):
    for item in hex_list:
        if item == Key.dot:
            pressTwoKeys(Key.shift, item)
        else:
            press(item)


if __name__ == "__main__":
    print("!DONT PRESS ANYTHING!")
    sleep(1)
    # This opens run command window.
    pressTwoKeys(Key.win,Key.r)
    # This writes text to the command input and presses enter
    write(hex_list)