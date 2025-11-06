# Countdown Timer (PyQt5)

A beautiful and minimal **countdown timer** built with **PyQt5**, featuring a **dark neon theme**.  
You can set a custom time, start, pause/resume, or reset the timer — and an alarm sound plays when time runs out.

---

## Overview

The UI is designed using **Qt Designer** (`countdown-timer-fixed.ui`) and includes:

- A digital time display (`QLabel`)
- Time selector (`QTimeEdit`)
- Three buttons: **Start**, **Stop / Resume**, and **Reset**
- Smooth color transitions depending on the timer state

---

## Features

✅ Countdown timer with second precision  
✅ Pause and resume functionality  
✅ Reset to the original selected time  
✅ Plays an alarm sound when time reaches zero  
✅ Automatically resets after alarm  
✅ Dynamic background colors 

---

## Requirements

Make sure you have **Python 3.8+** and **PyQt5** installed.

### Install dependencies:
```bash
pip install PyQt5

---

Sound Notes: The file Alarm-Clock.mp3 must be located in the same directory as countdown_timer.py.
