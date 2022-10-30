# OpenSettingsDevices
---
A program to open the settings panel Bluetooth &amp; Devices <br>
Why? why not? I just wanted to try if it were possible and was feeling lazy and now I have a one click access to open it.

## How it works

This script uses default python libraries so you only need a basic installation of python3.
It uses ctypes to access keyboard events.
```
from ctypes import *
```

The program needs hex codes to know what keys to work with and after a bit of googling and trying to figure out the right codes, I got frustrated and downloaded a program to get the hex codes directly. The program I used is called "KeyboardStateView". Just google the program name or use this link https://www.nirsoft.net/utils/keyboard_state_view.html
Also what made my search a bit harder is that I have a finnish/swedish keyboard. So if you have a different keyboard layout, you need to change some keys.
(the character keys should be the same)
```
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
```

So after mapping the right codes to variables with the corresponding characters, the program uses the two keys to open the run command window
(Windows key and r key)
```
  pressTwoKeys(Key.win,Key.r)
```

And then it gets keys from a list to press them in a correct order
```
hex_list = [Key.m, Key.s, Key.dash, Key.s, Key.e, Key.t, Key.t, Key.i, Key.n, Key.g, Key.s, Key.dot, Key.d, Key.e, Key.v, Key.i, Key.c, Key.e, Key.s, Key.enter]
```
This will type out " ms-settings.devices "
And in the loop what uses the list to type out the keys, it waits for the dot and then uses the pressTwo function to press two keys ( shift + dot(.) ) to turn it into a colon.
```
def write(hex_list):
    for item in hex_list:
        if item == Key.dot:
            pressTwoKeys(Key.shift, item)
        else:
            press(item)
```

And thats basically it!


----
## How to install 
