#!/usr/bin/env python3

import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
import os
from odf.opendocument import OpenDocumentSpreadsheet, load
from odf.table import Table, TableRow, TableCell
from odf.text import P

def get_note():
    root = tk.Tk()
    root.withdraw() 
    user_input = simpledialog.askstring("Time Tracker", "Name your task:")
    return user_input

current_time = datetime.now().strftime("%H:%M")

user_input = get_note()

if user_input:
    ods_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "TimeTracking.ods")
    if not os.path.exists(ods_file_path):
        ods = OpenDocumentSpreadsheet()
        table = Table(name="Time Tracking")
        ods.spreadsheet.addElement(table)
        header_row = TableRow()
        for header in ["Time", "Task", "Total (Minutes)"]:
            cell = TableCell()
            cell.addElement(P(text=header))
            header_row.addElement(cell)
        table.addElement(header_row)
        ods.save(ods_file_path)
    else:
        ods = load(ods_file_path)
    table = ods.spreadsheet.getElementsByType(Table)[0]
    rows = table.getElementsByType(TableRow)[1:]
    last_time = None
    if rows:
        last_row = rows[-1]
        last_time_text = last_row.getElementsByType(TableCell)[0].getElementsByType(P)[0].firstChild
        if last_time_text:
            last_time = datetime.strptime(last_time_text.data, "%H:%M")
    time_difference = ""
    if last_time:
        time_difference = (datetime.strptime(current_time, "%H:%M") - last_time).total_seconds() // 60
    for entry in [current_time, user_input, str(time_difference) if last_time else ""]:
        cell = TableCell()
        cell.addElement(P(text=entry))
        new_row.addElement(cell)
    table.addElement(new_row)
    ods.save(ods_file_path)
    messagebox.showinfo("Success", "Done!")
else:
    messagebox.showwarning("Oh no!", "Seems like you got an error!")
