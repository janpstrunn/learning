#!/usr/bin/env python3

import tkinter as tk
from tkinter import simpledialog
from datetime import datetime
import os

current_time = datetime.now().strftime("%H:%M")

root = tk.Tk()
root.withdraw() 

user_input = simpledialog.askstring("Time Tracker", "Name your task:")

if user_input:
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Inbox.md")
    with open(desktop_path, "a") as f:
        f.write(f"{current_time} {user_input}\n")
