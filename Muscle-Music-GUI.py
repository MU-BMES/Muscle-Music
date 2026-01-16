import tkinter
from tkinter import PhotoImage
from PIL import ImageTk, Image
import customtkinter as ctk
import random

#generate random wheel and selects a chord from the wheel putting it in the highlighted tag
def getChord ():
    wheelLabel.configure(state = "normal")  # sets wheel to open 
    wheelLabel.delete("1.0", "end") # clears all previous content 

    wheels = ["1", "2", "3", "4", "5"]
    wheel =  wheels[random.randint(0, len(wheels)-1)]
    wheels = " ".join(wheels) # creates a string of wheels separated by spaces
    wheelLabel .insert("end", wheels) # inserts the string of wheels into the textbox
    index = wheels.find(wheel) # finds the index of the selected wheel
    start_wheel = f"1.{index}"  #locates the start and end of wheel highlight 
    end_wheel = f"1.{index+ 1}" 
    wheelLabel.tag_add("highlight", start_wheel, end_wheel)

    chordLabel.configure(state = "normal")
    chordLabel.delete("1.0", "end")

    if wheel == "1":
        w1 = ["B  ", "C#m", "D#m", "E  ", "F#  ", "G#m"]
        chord =  w1[random.randint(0, len(w1)-1)]
        w1 = " ".join(w1)
        chordLabel.insert("end", w1)
        index = w1.find(chord)
        start_chord = f"1.{index}"
        end_chord = f"1.{index+len(chord)}"
        chordLabel.tag_add("highlight", start_chord, end_chord)

    elif wheel == "2":
        w2 = ["C   ", "DDm ", "Em ", "F   ", "G   ", "Am "]
        chord =  w2[random.randint(0, len(w2)-1)]
        w2 = " ".join(w2)
        chordLabel.insert("end", w2)
        index = w2.find(chord)
        start_chord = f"1.{index}"
        end_chord = f"1.{index+len(chord)}"
        chordLabel.tag_add("highlight", start_chord, end_chord)

    elif wheel  == "3":
        w3 = ["D♭ ", "E♭m", "Fm ", "G♭ ", "A♭ ", "B♭m"]   
        chord =  w3[random.randint(0, len(w3)-1)]
        w3 = " ".join(w3)
        chordLabel.insert("end", w3)
        index = w3.find(chord)
        start_chord = f"1.{index}"
        end_chord = f"1.{index+len(chord)}"
        chordLabel.tag_add("highlight", start_chord, end_chord)

    elif wheel == "4":
        w4 = ["D  ", "Em ", "F#m ", "G  ", "A  ", "Bm "]
        chord =  w4[random.randint(0, len(w4)-1)]
        w4 = " ".join(w4)
        chordLabel.insert("end", w4)
        index = w4.find(chord)
        start_chord = f"1.{index}"
        end_chord = f"1.{index+len(chord)}"
        chordLabel.tag_add("highlight", start_chord, end_chord)

    else:
        w5 = ["E♭ ", "Fm ", "Gm ", "A♭ ", "B♭ ", "Cm "]
        chord =  w5[random.randint(0, len(w5)-1)]
        w5 = " ".join(w5)
        chordLabel.insert("end", w5)
        index = w5.find(chord)
        start_chord = f"1.{index}"
        end_chord = f"1.{index+len(chord)}"
        chordLabel.tag_add("highlight", start_chord, end_chord)

    wheelLabel.tag_add("highlight", start_wheel, end_wheel)
    chordLabel.configure(state = "disabled")
    wheelLabel.configure(state = "disabled")
  
# Set the default theme and color 
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

#Creates window and font
app = ctk.CTk()
app.geometry("1100x710")
app.title("Muscle Music")
font_default= ctk.CTkFont(family="Times New Roman", size=35)
font_bold= ctk.CTkFont(family="Times New Roman", size=35, weight="bold")

# Adding Sound Button label 
sound = ctk.CTkButton (app, text="Play Sound", command = getChord)
sound.pack(pady=10, padx=10)

#Guitar frame
guitarFrame = ctk.CTkFrame(app, width=100, height=100,fg_color="transparent")
guitarFrame.pack(side = ctk.LEFT,pady=10, padx=10)

# add the photo
guitar_path = "guitar.png"
guitar = Image.open(guitar_path)
tkguitar = ctk.CTkImage(guitar, size = (500, 500))
guitarImage = ctk.CTkLabel(guitarFrame, image=tkguitar, text="")
guitarImage.pack( pady=10, padx=100)

# Adding Note label 
chordLabel= ctk.CTkTextbox(guitarFrame, width=500, height=50, font=font_default, fg_color="transparent")
chordLabel.pack(pady=10, padx=10)
chordLabel.tag_config("highlight", foreground="yellow")
chordLabel.configure(state = "disabled")

# Adding Wheel frame
wheelFrame = ctk.CTkFrame(app, width=100, height=100, fg_color="transparent")
wheelFrame.pack(side = ctk.LEFT, pady=10, padx=10)

# Adding Weel Title
wheelTitle = ctk.CTkLabel(wheelFrame, text="Wheel", font=font_bold)
wheelTitle.pack(pady=10, padx=(10,200))

# Adding Wheel label 
wheelLabel = ctk.CTkTextbox(wheelFrame, width=300, height=50, font=font_default, fg_color="transparent")
wheelLabel.pack(pady= (0,200))
wheelLabel.tag_config("highlight", foreground="yellow")
wheelLabel.configure(state = "disabled")

# Adding Live input label 
liveInputLabel = ctk.CTkLabel(wheelFrame, text="Live Input", font=font_bold)
liveInputLabel.pack(pady=(10,200))

app.mainloop()