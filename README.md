# wobblemouse

A little script to wobble the mouse around occasionally, preventing my status in Teams (probably would work with Slack, IDK) from reverting to "Away", even though I'm _right here_, reading a doc, watching a video, whatever...

Originally concieved during the Work From Home phase of the COVID-19 pandemic, it remains a useful part of my toolset, preventing Teams making it look like I'm a slacker... 😉

Although my notes trace the genesis of this thing back to October 2020, I somehow never created a repo on GitHub for it. This is (finally) correcting that omission.

It uses the excellent [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) to just jog the mouse a few pixels every few (randomized) minutes.

Thanks to [PEP-668](https://peps.python.org/pep-0668/), PyAutoGUI and whatever else it needs must be installed in a venv. I use a shell script (MacOS, usually) to activate the venv and launch the script. See/use requirements.txt for the details for pip. 00_wobblemouse.sh is the script I use, called with an [XMenu](https://apps.apple.com/us/app/xmenu/id419332741?mt=12) Custom menu-bar dropdown.
