from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(width=False, height=False)
root.configure(background="#F0F1F5")


def BMI():
    h = float(height.get())
    w = float(weight.get())
    
    #Calculating BMI
    bmi = round(float((w / (h ** 2)) * 703), 1)
    
    label1.configure(text=bmi)
    
    #BMI Categories
    if bmi <= 18.5:
        label2.config(text="Underweight!")
        label3.config(text="You have a lower weight \nthan normal. Try to \ngain weight by eating \nhealthy foods.")
        
    elif bmi > 18.5 and bmi <= 24.9:
        label2.config(text="Normal!")
        label3.config(text="You have a normal weight.\nGood job!")
        
    elif bmi > 24.9 and bmi <= 29.9:
        label2.config(text="Overweight!")
        label3.config(text="You have a higher weight \nthan normal. Try to \nlose weight by exercising and \neating healthy foods.")
        
    else:
        label2.config(text="Obese!")
        label3.config(text="Your health is at risk. \nTry to lose weight by \nexercising and eating \nhealthy foods.")


#BMI Icon next to the title
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)


#Top Frame (Heading of the Application)
top = PhotoImage(file="Images/top.png")
top_image = Label(root, image=top, background="#F0F1F5")
top_image.place(x=-10, y=-10)


#Bottom Frame
Label(root, width=72, height=18, background="lightblue").pack(side=BOTTOM)


#Two Boxes in the Top Half of the Application
box = PhotoImage(file="Images/box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)


#Weight Scale Image
scale = PhotoImage(file="Images/scale.png")
Label(root, image=scale, bg="lightblue").place(x=15, y=310)


#####################Slider 1#####################
current_value = tk.DoubleVar()

def get_current_value():
    return "{: .2f}".format(current_value.get())
    
def slider_changed(event):
    Height.set(get_current_value())
    
    size = int(float(get_current_value()))
    img = (Image.open("Images/man.png"))
    resized_image = img.resize((50, 10+size))
    photo2 = ImageTk.PhotoImage(resized_image)
    manFigure.configure(image=photo2)
    manFigure.place(x=70, y=550-size)
    manFigure.image = photo2
               
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed, variable = current_value)
slider.place(x=80, y=250)

#Slider 1(slider color change)
style = ttk.Style()
style.configure("TScale",background = "white")


#####################Slider 2#####################
current_value2 = tk.DoubleVar()

def get_current_value2():
    return "{: .2f}".format(current_value2.get())
    
def slider_changed2(event):
    Weight.set(get_current_value2())
               
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale", command=slider_changed2, variable = current_value2)
slider2.place(x=300, y=250)

#Slider 2(slider color change)
style2 = ttk.Style()
style2.configure("TScale",background = "white")


#Text Entry Boxes
Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font=("Arial", 50), bg="#FFF", fg = "#000", bd=0, justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font=("Arial", 50), bg="#FFF", fg = "#000", bd=0, justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())


#Man Figure Image
manFigure = Label(root, bg = "lightblue")
manFigure.place(x=70, y=530)


Button(root,text="View Report", width=15, height=2, bg="#1F6E68", fg="white", command=BMI, font="aerial 10 bold").place(x=170, y=315)

label1 = Label(root, font=("aerial 40 bold"), bg="lightblue", fg="#fff")
label1.place(x=320, y=305)

#Labels Frame was created to help with the placement of the labels and center label 1 and 2 with respect to each other
labels_frame = Frame(root, bg="lightblue")
labels_frame.place(x=180, y=370)

label2 = Label(labels_frame, font=("aerial", 30, "bold"), bg="lightblue", fg="#3b3a3a")
label2.grid(row=0, column=0, pady=0)

label3 = Label(labels_frame, font=("aerial", 15), bg="lightblue")
label3.grid(row=1, column=0, pady=0)

label_inches = Label(root, text="Inches", font=("aerial 20 bold"), bg="white", fg="#3b3a3a")
label_inches.place(x=85, y=110)

label_pounds: Label = Label(root, text="Pounds", font=("aerial 20 bold"), bg="white", fg="#3b3a3a")
label_pounds.place(x=300, y=110)

root.mainloop()