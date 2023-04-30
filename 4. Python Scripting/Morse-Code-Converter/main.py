import json
import pyperclip
from tkinter import *
from PIL import Image, ImageTk


# ------------- function ----------- #
def to_morse(input):
    result = ""
    value = text_text.get("1.0", END).strip()
    with open("morse-code.json", "r") as file:
        message.set("")
        data = json.load(file)
        for letter in value:
            try:
                if letter == "\n":
                    result += "\n"
                else:
                    result += (data[letter.lower()]) + " "
            except KeyError:
                message.set('Please only use char "A-Z", "1-10", "?,," All other char will not be included in the morse-code!')
    morse_text.delete("1.0", END)
    morse_text.insert("1.0", result)


def to_word(codes):
    result = ""
    values = morse_text.get("1.0", END).strip()
    codes_list = values.split()
    with open("morse-code.json", "r") as file:
        data = json.load(file)
        for n in range(len(codes_list)):
            for key, value in data.items():
                if value == codes_list[n]:
                    result += key
    end_result = result.capitalize()
    text_text.delete("1.0", END)
    text_text.insert("1.0", end_result)

def copy(button):
    if button == "Button_1":
        values = text_text.get("1.0", END)
        pyperclip.copy(values)
    else:
        values = morse_text.get("1.0", END)
        pyperclip.copy(values)


# <--------------- UI ----------------- > #
# init window
window = Tk()
window.title("Morse Code Converter")
window.config(padx=50, pady=50)

# resize logo to fit
img = (Image.open("logo.png"))
resized_img = img.resize((100, 40), Image.LANCZOS)
new_image = ImageTk.PhotoImage(resized_img)

# creating the logo in the window
canvas = Canvas(width=150, height=80)
canvas.create_image(100, 50, image=new_image)
canvas.grid(column=1, row=0)

# message to display errors
message = StringVar()
error_message = Message(textvariable=message, width=500, fg="red")
error_message.grid(column=1, row=1, sticky="ew")

# allow user to type multiple lines into the box
text_label = Label(text="Text Input: ")
text_label.grid(column=0, row=2, sticky="ne")
text_text = Text(height=3, state=NORMAL)
text_text.grid(column=1, row=2)
text_text.bind("<KeyRelease>", to_morse)

# creating empty row
text_label = Label(text="")
text_label.grid(column=0, row=3)

# create second error message
message_2 = StringVar()
error_message_2 = Message(textvariable=message_2, width=500)
error_message_2.grid(column=1, row=3, sticky="ew")

morse_label = Label(text="Morse Input: ")
morse_label.grid(column=0, row=4, sticky="ne")
morse_text = Text(height=10, state=NORMAL)
morse_text.grid(column=1, row=4, sticky="we")
morse_text.bind("<KeyRelease>", to_word)

copy_button_1 = Button(text="Copy", command= lambda button="Button_1": copy(button))
copy_button_1.grid(column=2, row=2, sticky="n")

copy_button_2 = Button(text="Copy", command= lambda button="Button_2": copy(button))
copy_button_2.grid(column=2, row=4, sticky="n")

window.mainloop()
