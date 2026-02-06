import tkinter
from tkinter import PhotoImage
from PIL import ImageTk, Image
import customtkinter as ctk
import random


def getChord ():
    key_label.configure(state = "normal")  # sets wheel to open 
    key_label.delete("1.0", "end") # clears all previous content 

    wheels = ["1", "2", "3", "4", "5"]
    wheel =  wheels[random.randint(0, len(wheels)-1)]
    wheels = " ".join(wheels) # creates a string of wheels separated by spaces
    key_label .insert("end", wheels) # inserts the string of wheels into the textbox
    index = wheels.find(wheel) # finds the index of the selected wheel
    start_wheel = f"1.{index}"  #locates the start and end of wheel highlight 
    end_wheel = f"1.{index+ 1}" 
    key_label.tag_add("highlight", start_wheel, end_wheel)
    chord_label.configure(state = "normal")
    chord_label.delete("1.0", "end")

    if wheel == "1":
        w1 = ["B  ", "C#m", "D#m", "E  ", "F#  ", "G#m"]
        chord =  w1[random.randint(0, len(w1)-1)]
        w1 = "\n".join(w1)
        chord_label.insert("end", w1)
        index = w1.find(chord)
        start_chord = f"1.{index}"
        end_chord = f"1.{index+len(chord)}"
        chord_label.tag_add("highlight", start_chord, end_chord)
    elif wheel == "2":
        w2 = ["C   ", "DDm ", "Em ", "F   ", "G   ", "Am "]
        chord =  w2[random.randint(0, len(w2)-1)]
        w2 = "\n".join(w2)
        chord_label.insert("end", w2)
        index = w2.find(chord)
        start_chord = f"1.{index}"
        end_chord = f"1.{index+len(chord)}"
        chord_label.tag_add("highlight", start_chord, end_chord)
    elif wheel  == "3":
        w3 = ["D♭ ", "E♭m", "Fm ", "G♭ ", "A♭ ", "B♭m"]   
        chord =  w3[random.randint(0, len(w3)-1)]
        w3 = "\n".join(w3)
        chord_label.insert("end", w3)
        index = w3.find(chord)
        start_chord = f"1.{index}"
        end_chord = f"1.{index+len(chord)}"
        chord_label.tag_add("highlight", start_chord, end_chord)

    elif wheel == "4":
        w4 = ["D  ", "Em ", "F#m ", "G  ", "A  ", "Bm "]
        chord =  w4[random.randint(0, len(w4)-1)]
        w4 = "\n".join(w4)
        chord_label.insert("end", w4)
        index = w4.find(chord)
        start_chord = f"1.{index}"
        end_chord = f"1.{index+len(chord)}"
        chord_label.tag_add("highlight", start_chord, end_chord)
    else:
        w5 = ["E♭ ", "Fm ", "Gm ", "A♭ ", "B♭ ", "Cm "]
        chord =  w5[random.randint(0, len(w5)-1)]
        w5 = "\n".join(w5)
        chord_label.insert("end", w5)
        index = w5.find(chord)
        start_chord = f"1.{index}"
        end_chord = f"1.{index+len(chord)}"
        chord_label.tag_add("highlight", start_chord, end_chord)

    key_label.tag_add("highlight", start_wheel, end_wheel)
    chord_label.configure(state = "disabled")
    key_label.configure(state = "disabled")
  

# Set the default theme and color 
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


#Creates window and fonts
app = ctk.CTk()
app.geometry("1100x710")
app.title("Muscle Music (design 2)")
font_default= ctk.CTkFont(family="Times New Roman", size=35)
font_bold= ctk.CTkFont(family="Times New Roman", size=35, weight="bold")

#Key frame
key_frame = ctk.CTkFrame(app, width=400, height=100,fg_color="blue")
key_frame.pack(pady=10, padx=10)

#Chord frame
chord_frame = ctk.CTkFrame(app, width=700, height=300,fg_color="blue")
chord_frame.pack(pady=10, padx=10)

#Guitar frame
guitar_frame = ctk.CTkFrame(app, width=1000, height=300,fg_color="blue")
guitar_frame.pack(pady=10, padx=10)

#Key textbox  
key_label= ctk.CTkTextbox(key_frame, width=300, height=50, font=font_default, fg_color="red")
key_label.pack(pady = 10, padx = 10)
key_label.tag_config("highlight", foreground="yellow")
key_label.configure(state = "disabled")

#Right bracket photo
rbracket_path = "bracket_right.png"
rbracket = Image.open(rbracket_path)
tkrbracket = ctk.CTkImage(rbracket, size = (100, 300))
rbracketImage = ctk.CTkLabel(chord_frame, image=tkrbracket, text="")
rbracketImage.pack( side="right", pady=10, padx=100)

#chord textbox  
chord_label= ctk.CTkTextbox(chord_frame, width=100, height=300, font=font_default, fg_color="red")
chord_label.pack(side = "right", pady = 10, padx = 10)
chord_label.tag_config("highlight", foreground="yellow")
chord_label.configure(state = "disabled")

#Left bracket photo
lbracket_path = "bracket_left.png"
lbracket = Image.open(lbracket_path)
tklbracket = ctk.CTkImage(lbracket, size = (100, 300))
lbracketImage = ctk.CTkLabel(chord_frame, image=tklbracket, text="")
lbracketImage.pack( side="left", pady=10, padx=100)

# Adding Sound Button label 
sound = ctk.CTkButton (app, text="Play Sound", command = getChord)
sound.pack(pady=10, padx=10)

app.mainloop()