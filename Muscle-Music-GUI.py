import tkinter
from tkinter import PhotoImage
from PIL import ImageTk, Image
import customtkinter
import random
chord = ""

def getNote ():
    global chord
    wheels = ["1", "2", "3", "4", "5"]
    wheels =  wheels[random.randint(0, len(wheels)-1)]
    wheelLabel.configure(text = "Wheel: " + wheels)
    if wheels == "1":
        w1 = ["B","C#m", "D#m", "E", "F#", "G#m"]
        chord =  w1[random.randint(0, len(w1)-1)]

    elif wheels == "2":
        w2 = ["C", "Dm", "Em", "F", "G", "Am"]
        chord =  w2[random.randint(0, len(w2)-1)]

    elif wheels == "3":
        w3 = ["D♭", "E♭m", "Fm", "G♭", "A♭", "B♭m"]   
        chord =  w3[random.randint(0, len(w3)-1)]

    elif wheels == "4":
        w4 = ["D", "Em", "F#m", "G", "A", "Bm"]
        chord =  w4[random.randint(0, len(w4)-1)]
    else:
        w5 = ["E♭", "Fm", "Gm", "A♭", "B♭", "Cm"]
        chord =  w5[random.randint(0, len(w5)-1)]
    chordLabel.configure(text = chord)


# Set the default theme and color 
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

3

#Creates window and font
app = customtkinter.CTk()
app.geometry("1100x710")
app.title("Muscle Music")
font1 = customtkinter.CTkFont(family="Times New Roman", size=20)
font2 = customtkinter.CTkFont(family="Times New Roman", size=35)

# Adding Title label 
title = customtkinter.CTkLabel(app, text="Muscle Music", font=font1)
title.pack(pady=10, padx=10)

# Adding Sound Button label 
sound = customtkinter.CTkButton (app, text="Play Sound", command = getNote)
sound.pack(pady=10, padx=10)


# add the photo
guitar_path = "guitar.png"
guitar = Image.open(guitar_path)
tkguitar = customtkinter.CTkImage(guitar, size = (500, 500))
guitarImage = customtkinter.CTkLabel(app, image=tkguitar, text="")
guitarImage.pack(side = customtkinter.LEFT, pady=10, padx=100)



# Adding Wheel label 
wheelLabel = customtkinter.CTkLabel(app, text="Wheel: none", font=font2)
wheelLabel.pack(side = customtkinter.LEFT, pady= 10, padx=10)

# Adding Note label 
chordLabel= customtkinter.CTkLabel(app, text="none", font=font2)
chordLabel.pack( side = customtkinter.LEFT, pady= 10, padx=50)



app.mainloop()