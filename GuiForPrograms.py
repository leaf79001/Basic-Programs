import os
import sys

import tkinter as tk
from tkinter import ttk

def get_files():
    # Get all files in the current directory ending with '.py'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    files = [file for file in os.listdir(current_dir) if file.endswith('.py')]
    return files

def run_file(event):
    # Get the file path of the selected file
    selection = event.widget.selection()
    if selection:
        file_path = os.path.join(current_dir, selection[0])
        # Run the selected file as a subprocess
        subprocess.Popen([sys.executable, file_path])

# Get all .py files in the current directory
files = get_files()

# Create a GUI using tkinter
root = tk.Tk()
root.title("Python Programs")

# Create a listbox to display the files
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
for file in files:
    listbox.insert(tk.END, file)
listbox.bind("<Double-Button-1>", run_file)
listbox.pack(fill=tk.BOTH, expand=True)

# Start the GUI event loop
root.mainloop()