# 365 Days of Code - Termux Edition

Hey, I'm Gourav. Learning programming + automation with Termux on my Vivo Y15s.

**Goal**: 1 program per day for 365 days.

**How I'm learning**: I'm a complete beginner who started with just `cd pwd ls`. I'm using Meta AI to explain concepts, debug errors, and plan projects. AI writes the first draft, I run it, break it, fix it, and understand it. No copy-paste without learning.

### Requirements
'''bash
pkg install python termux-api
termux-setup-storage

### Day 1: **storage.py**
Checks total/used/free storage on my phone using `df` and Termux.

**Run it**:
python storage.py

### Day 2: **battery.py**
Checks battery percentage, health, status, and temperature using `termux-battery-status`.
Gives you warnings when charge gets low.

**Run it**:
pyrhon battery.py

###Day 3: **wifi.py**

Checks WiFi connection info using termux-wifi-connectioninfo. Shows SSID, IP, signal strength in dBm, and rates connection as Amazing/good/bad/worst. Sends notification with current status.

**Run it**:
 python wifi.py
