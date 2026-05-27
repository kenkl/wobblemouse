#!/usr/bin/env python3
# A little ditty to wobble the mouse around a little to simulate activity.

import pyautogui
from time import sleep, strftime
from datetime import datetime
import random

wobbles = 1

while True:
    now = datetime.now().strftime('%H:%M:%S')
    waitTime = random.randint(100,200)
    print('Wobble the mouse at %s (%s wobbles so far) - ' % (now, str(wobbles)), end = '')
    pyautogui.moveRel(10, 10, duration=0.1)
    sleep(1)
    pyautogui.moveRel(-10, -10, duration=0.1)
    print('Next in %s seconds' % (str(waitTime)))
    sleep(waitTime)
    wobbles += 1

