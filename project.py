import customtkinter
import os
from PIL import Image



def face_reg():
     os.system("py firstpage.py")
def vic_asst():
     os.system("py personal.py")
def scrap():
     os.system("py price_comparison_engine.py")
def file_manager():
     os.system("py file.py")
def camera():
     os.system("py cam.py")
def calculator():
     os.system("py calculator.py")
def tictac():
     os.system("py tiktac.py")
def qr_code():
     os.system("py qr_code.py")

def brightness():
     os.system("py brightness.py")
def volume():
     os.system("py vol_con.py")

def chatbot():
     os.system("py app.py")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("MODERN GUI")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),size=(26, 26))
        self.face_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "FREG.png")),size=(26, 26))
        self.voice_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "mic.png")),size=(26, 26))
        self.price_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "scrap.png")),size=(26, 26))
        self.file_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "file.png")),size=(26, 26))
        self.cam_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "cam.png")),size=(26, 26))
        self.cal_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "cal.png")),size=(26, 26))
        self.tictac_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "open.png")),size=(26, 26))
        self.qrcode_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "qr.png")),size=(26, 26))
       # self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), #size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.cam_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "cam.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "cam.png")), size=(20, 20))

        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
       
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="MOBILE  ", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),

                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")


        self.brg_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Brightness",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("black", "black"),

                                                   image=self.cam_image, anchor="w", command=brightness )
        self.brg_button.grid(row=2, column=0, sticky="ew")

        self.chat_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="CHATBOT",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("black", "black"),

                                                   image=self.cam_image, anchor="w", command=chatbot )
        self.chat_button.grid(row=5, column=0, sticky="ew")





        self.vol_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Volume",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("black", "black"),

                                                   image=self.cam_image, anchor="w", command=volume )
        self.vol_button.grid(row=3, column=0, sticky="ew")


        

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        #self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="sathya", image=self.image_icon_image)
        #self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="FACE REG", image=self.face_image,command=face_reg) 
        self.home_frame_button_1.grid(row=0, column=0,padx=50, pady=30 ),
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="VOICE ", image=self.voice_image ,command=vic_asst, compound="left")
        self.home_frame_button_2.grid(row=0, column=1, padx=50, pady=30)
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="PRICE", image=self.price_image, command=scrap,compound="left")
        self.home_frame_button_1.grid(row=1, column=0, padx=50, pady=30)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="FILE ", image=self.file_image,command=file_manager, compound="left")
        self.home_frame_button_2.grid(row=1, column=1, padx=50, pady=30)
        
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="CAMERA", image=self.cam_image,command=camera) 
        self.home_frame_button_1.grid(row=2, column=0,padx=50, pady=30 ),
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CALCULATOR", image=self.cal_image ,command=calculator, compound="left")
        self.home_frame_button_2.grid(row=2, column=1, padx=50, pady=30)
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="TIC TAC TOE", image=self.tictac_image, command=tictac,compound="left")
        self.home_frame_button_1.grid(row=3, column=0, padx=50, pady=30)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="QRCODE", image=self.qrcode_image,command=qr_code, compound="left")
        self.home_frame_button_2.grid(row=3, column=1, padx=50, pady=30)

        # create third frame
  
        # select default frame
        self.select_frame_by_name("home")
 

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
       

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
    
        
    def home_button_event(self):
        self.select_frame_by_name("home")


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
 

    



if __name__ == "__main__":
    app = App()
    app.mainloop()

