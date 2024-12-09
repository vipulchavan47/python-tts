import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox  
from tkinter.ttk import Combobox, Style
import pyttsx3
import pytesseract
from PIL import Image

 
root = Tk()
root.title("Text to Speech")
root.geometry("900x500+100+100")
root.resizable(False, False)
root.configure(bg="#1A3B59")


engine = pyttsx3.init()


# Speak function to speak text
def speaknow():
    text = text_area.get(1.0, END).strip()
    if not text:
        messagebox.showwarning("No Text", "Please enter some text before speaking.")
        return

    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    selected_language = language_combobox.get()

    
    def setvoice():
        if (gender == 'David'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        elif(gender== 'Tony'):
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
        elif(gender== 'Meera'):
            engine.setProperty('voice', voices[5].id)
            engine.say(text)
            engine.runAndWait()
        elif(gender== 'Kalpana'):
            engine.setProperty('voice', voices[4].id)
            engine.say(text)
            engine.runAndWait()
        elif(gender== 'Hemant'):
            engine.setProperty('voice', voices[3].id)
            engine.say(text)
            engine.runAndWait()
        elif(gender== 'Sam'):
            engine.setProperty('voice', voices[2].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[6].id)
            engine.say(text)
            engine.runAndWait()
    
    if (speed == "Fast"):
        engine.setProperty('rate', 250)
    elif (speed == "Normal"):
        engine.setProperty('rate', 150)
    else:
        engine.setProperty('rate', 60)

    # Check if the text language matches the selected language
    if selected_language == 'English':
        if any(char.isalpha() and char.isupper() for char in text):
            # Text contains English characters
            setvoice()
        else:
            messagebox.showwarning("Language Mismatch", "The text in the text area is not in English. Please enter English text.")
            return
    elif selected_language == 'Hindi':
        if any(char.isalpha() and '\u0900' <= char <= '\u097F' for char in text):
            # Text contains Hindi characters
            setvoice()
        else:
            messagebox.showwarning("Language Mismatch", "The text in the text area is not in Hindi. Please enter Hindi text.")
            return
    elif selected_language == 'Marathi':
        if any(char.isalpha() and '\u0900' <= char <= '\u097F' for char in text):
            # Text contains Marathi characters
            setvoice()
        else:
            messagebox.showwarning("Language Mismatch", "The text in the text area is not in Marathi. Please enter Marathi text.")
            return
    else:
        # Handle unexpected languages
        messagebox.showwarning("Language Error", "Selected language is not supported for text-to-speech.")
        return




# Download function 
def download():
    text = text_area.get(1.0, END).strip()
    if not text:
        messagebox.showwarning("No Text", "Please enter some text before downloading.") 
        return
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')


    def setvoice():
        if (gender == 'David'):
            engine.setProperty('voice', voices[0].id)
            file_path = filedialog.asksaveasfilename(defaultextension=file_extension, filetypes=file_types)
            if file_path:
                engine.save_to_file(text, file_path)
                engine.runAndWait()
        elif(gender=='Tony'):
            engine.setProperty('voice', voices[1].id)
            file_path = filedialog.asksaveasfilename(defaultextension=file_extension, filetypes=file_types)
            if file_path:
                engine.save_to_file(text, file_path)
                engine.runAndWait()
        elif(gender=='Meera'):
            engine.setProperty('voice', voices[5].id)
            file_path = filedialog.asksaveasfilename(defaultextension=file_extension, filetypes=file_types)
            if file_path:
                engine.save_to_file(text, file_path)
                engine.runAndWait()
        elif(gender=='Kalpana'):
            engine.setProperty('voice', voices[4].id)
            file_path = filedialog.asksaveasfilename(defaultextension=file_extension, filetypes=file_types)
            if file_path:
                engine.save_to_file(text, file_path)
                engine.runAndWait()
        elif(gender=='Hemant'):
            engine.setProperty('voice', voices[3].id)
            file_path = filedialog.asksaveasfilename(defaultextension=file_extension, filetypes=file_types)
            if file_path:
                engine.save_to_file(text, file_path)
                engine.runAndWait()
        elif(gender=='Sam'):
            engine.setProperty('voice', voices[2].id)
            file_path = filedialog.asksaveasfilename(defaultextension=file_extension, filetypes=file_types)
            if file_path:
                engine.save_to_file(text, file_path)
                engine.runAndWait()
        else:
            engine.setProperty('voice', voices[6].id)
            file_path = filedialog.asksaveasfilename(defaultextension=file_extension, filetypes=file_types)
            if file_path:
                engine.save_to_file(text, file_path)
                engine.runAndWait()

    if (speed == "Fast"):
        engine.setProperty('rate', 250)
    elif (speed == "Normal"):
        engine.setProperty('rate', 150)
    else:
        engine.setProperty('rate', 60)

    setvoice()



def open_image():

  lang = language_combobox.get()
  file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])

  if file_path:
    img = Image.open(file_path)

    if lang == 'English':
      text = pytesseract.image_to_string(img)
    elif lang == 'Hindi':
      text = pytesseract.image_to_string(img, lang='hin')
    elif lang == 'Marathi':
      text = pytesseract.image_to_string(img, lang='mar')
    else:
      # Handle unexpected languages
      messagebox.showwarning("Language Error", "Selected language is not supported for extraction.")
      text = ""

    text_area.insert(END, text)

# File types for saving
file_types = [('MP3 Files', '*.mp3'), ('WAV Files', '*.wav'), ('OGG Files', '*.ogg')]
file_extension = file_types[0][1][1:]  # Default file extension is MP3

# Icon
image_icon = PhotoImage(file="speak.png")
root.iconphoto(False, image_icon)

# Top frame
Top_frame = Frame(root, bg="#FFFFFF", width=900, height=100)
Top_frame.place(x=0, y=0)
Logo = PhotoImage(file="speaker_logo.png")
Label(Top_frame, image=Logo, bg="#FFFFFF").place(x=10, y=5)
Label(Top_frame, text="TEXT TO SPEECH", font="Arial 20 bold", bg="#FFFFFF", fg="#1A3B59").place(x=100, y=30)

# Text area
text_area = Text(root, font="Roboto 16", bg="#EFF4F4", relief=GROOVE, wrap=WORD, borderwidth=2, padx=10, pady=10)
text_area.place(x=10, y=150, width=500, height=250)

# Rounded corners for the text area
radius = 20
text_area.config(highlightbackground="#BFBFBF", highlightthickness=1, highlightcolor="#BFBFBF")
text_area.bind("<Enter>", lambda e: text_area.config(highlightbackground="#1A3B59", highlightthickness=2))
text_area.bind("<Leave>", lambda e: text_area.config(highlightbackground="#BFBFBF", highlightthickness=1))


# Custom style for dropdown boxes
style = Style()
style.theme_create("CustomStyle", settings={
    "TCombobox": {
        "configure": {
            "padding": 5,
            "background": "#F5F5F5",
            "foreground": "#333333",
            "fieldbackground": "#F5F5F5",
            "bordercolor": "#BFBFBF",
            "selectbackground": "#1A3B59",
            "selectforeground": "#FFFFFF",
            "rowcolors": "#1A3B59",
            "borderwidth": 1, 
            "relief": "solid",  
            "border-radius": 5  
        }
    },
    "TMenubutton": {
        "configure": {"padding": 5}
    },
    "TButton": {  
        "configure": {
            "borderwidth": 1, 
            "relief": "solid",  
            "border-radius": 5  
        }
    }
})
style.theme_use("CustomStyle")


# Label for speed
Label(root, text="SPEED", font="Arial 14 bold", bg="#1A3B59", fg="#FFFFFF").place(x=580,y=255)
# Speed combobox
speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="Arial 12", state="readonly", width=10)
speed_combobox.place(x=550,y=285)
speed_combobox.set('Normal')


# Label for Language
Label(root, text="LANG", font="Arial 14 bold", bg="#1A3B59", fg="#FFFFFF").place(x=580, y=160)
# Language combobox
language_combobox = Combobox(root, values=['English', 'Marathi','Hindi'], font="Arial 12", state="readonly", width=10)
language_combobox.place(x=550, y=200)
language_combobox.set('English')

# Label for Voices
Label(root, text="VOICE", font="Arial 14 bold", bg="#1A3B59", fg="#FFFFFF").place(x=760,y=160)

# Set default language and voice
default_language = 'English'
default_voice = 'David'

# Function to update voices based on selected language
def update_voices(*args):
    lang = language_combobox.get()
    if lang == 'English':
        gender_combobox['values'] = ['David', 'Tony','Meera','Sam','Zara']
        gender_combobox.set('David')
    else:
        gender_combobox['values'] = ['Kalpana','Hemant']
        gender_combobox.set('Hemant')

# Bind event handler to language_combobox
language_combobox.bind("<<ComboboxSelected>>", update_voices)

# Set default language and voice
language_combobox.set(default_language)
gender_combobox = Combobox(root, font="Arial 12", state="readonly", width=10) 
# Define gender_combobox here
gender_combobox.place(x=730,y=200)
gender_combobox.set(default_voice)  # Set default voice
update_voices()  # Update voices initially

# Upload Image Button
imageicon3 = PhotoImage(file="image.png")
image_btn = Button(root, text="Add\nImage", compound=LEFT, image=imageicon3, width=120, font="arial 13 bold", command=open_image)
image_btn.place(x=730, y=260)  

# Speak Button
imageicon = PhotoImage(file="speaking.png")
btn = Button(root, text="Speak", compound=LEFT, image=imageicon, width=120, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=360)  

# Save Button
imageicon2 = PhotoImage(file="save-file.png")
save = Button(root, text="Save", compound=LEFT, image=imageicon2, width=120, bg="#EFF4F4", font="arial 14 bold", command=download)
save.place(x=730, y=360) 



root.mainloop()
