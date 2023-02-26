from tkinter import *
import customtkinter
from PIL import Image , ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("BUtton")
root.iconbitmap('')#file
root.geometry("500x500")

add_image = ImageTk.PhotoImage(Image.open("C:\Users\nandha kumar\Downloads\CustomTkinter-master\CustomTkinter-master\examples\test_images\home_dark.png").resize(20,20))
button_1 =customtkinter.CTkButton(master=root,Image=add_image)
button_1.pack(pady=20,padx=20)
root.mainloop()