# Setting up Main Window
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk


class restaurantManagementApp:
    def __init__(self,root):
        self.root=root
        self.menu_items = {
            "Fries": 2,
            "Pizza": 4.5,
            "Burgur": 3,
            "Drinks": 1,
            "Icecream": 1.5,
            "Cheese Burgur": 3.5,
        }
        self.setup_background(root)
        frame=ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(frame,text="Restaurant Order Management", font=("Arial", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)
        self.menu_labels={}
        self.menu_quantity = {}
        for i,(item, price) in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(frame,text=f"{item} Meal({price})",font=("Arial", 20)).grid(row=i,column=0, padx=10, pady=5)
            self.menu_labels[item]=label
            quantityEntry=ttk.Entry(frame, width=5)
            quantityEntry.grid(row=i,column=1,padx=10, pady=5)
            self.menu_quantity[item]=quantityEntry
        counterbtn = Button(master=window, text="Place Order", fg="white", bg="Black", command=errormessage)
        counterbtn.place(x=400, y=550)  

    def setup_background(self,root):
        bgwidth, bgheight=800,600
        canvas=tk.Canvas(root,width=bgwidth, height=bgheight)
        image = Image.open(
            "C:/Users/Lenovo/OneDrive/Documents/Codingal/Python/TKINTER/restaurantApp.jpg"
        )
        # Resize the image using resize() method
        image = image.resize((1000, 700))
        image_tk = ImageTk.PhotoImage(image)
        label = Label(window, image=image_tk, bg="light blue")
        canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        canvas.image=image_tk
        label.place(x=0,y=0)
        # Adding Image and Labels in the Main Window


def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(
        bg="light grey",
    )
    top.geometry("650x400+50+50")
    global entrybox
    global l1Entry
    global l2Entry
    global l3Entry
    labelTop1 = Label(top, text="Enter total amount:", bg="light grey")
    entrybox = Entry(top)
    labelTop2 = Label(
        top, text="Here are the number of notes for each denomination:", bg="light grey"
    )
    l1 = Label(top, text="2000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")
    l1Entry = Entry(top)
    l2Entry = Entry(top)
    l3Entry = Entry(top)
    btn = Button(top, text="Calculate", command=counter, bg="brown", fg="white")
    labelTop1.place(x=140, y=170)
    labelTop2.place(x=140, y=100)
    entrybox.place(x=210, y=120)
    btn.place(x=240, y=145)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    l1Entry.place(x=270, y=200)
    l2Entry.place(x=270, y=230)
    l3Entry.place(x=270, y=260)
    top.mainloop()


def errormessage():
    messages = messagebox.showerror(
        "Error!", "Please order atleast one item!"
    )
    if messages == "ok":
        topwin()


def counter():
    try:
        global amount
        amount = int(entrybox.get())
        note2000 = amount // 2000
        amount %= 2000
        note500 = amount // 500
        amount %= 500
        note100 = amount // 100
        amount %= 100
        l1Entry.delete(0, END)
        l2Entry.delete(0, END)
        l3Entry.delete(0, END)
        l1Entry.insert(END, str(note2000))
        l2Entry.insert(END, str(note500))
        l3Entry.insert(END, str(note100))
    except:
        messagebox.showerror("Error!", "Please enter a valid number.")


if __name__=="__main__":
    window = Tk()
    app=restaurantManagementApp(window)
    window.title("Restaurant App")
    window.geometry("800x600")
    window.mainloop()
