import os
import shutil
from tkinter import *
from tkinter import filedialog
import json


# Get the file path length
def get_file_path_length():
    length = file_path.get()
    return len(length)


def sort_files():
    # retrieve file path
    filepath = file_path.get()
    # retrieve items in file path
    files = os.listdir(filepath)
    with open('extension_categories.json', 'r') as data:
        p_data = json.load(data)
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            for key, value in p_data.items():
                if file_extension in value:
                    try:
                        new_filepath = filepath + "/" + key
                        os.mkdir(new_filepath)
                    except FileExistsError:
                        pass
                    shutil.move(filepath+"/"+file, new_filepath+"/"+file)
                    break

                else:
                    pass

# Create and configure window settings
window = Tk()
window.title("File Organizer")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)
window.grid_columnconfigure(2, weight=1)

# Create label for to indicate selection of File Path
file_path_label = Label(window, text="File Path:")
file_path_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

# Create label for to indicate selected File Path
file_path = StringVar()
directory_label = Label(window, textvariable=file_path, wraplength=get_file_path_length())
directory_label.config()
directory_label.grid(column=1, row=0, padx=10, pady=10, sticky="wes")

# Create button for selection of File Path
browse_button = Button(window, text="Browse", command=lambda: file_path.set(filedialog.askdirectory(mustexist=True)))
browse_button.grid(column=2, row=0, padx=10, pady=10, sticky="e")

# Create a button to start organizing
organize_button = Button(window, text="Organize", command=lambda: sort_files())
organize_button.grid(column=1, row=1, padx=10, pady=10)

window.mainloop()
