import tkinter
import tkinter.messagebox
import customtkinter
import threading

import time

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue") 



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.main = True
        self.statistics = False
        self.aim = False
        self.utilities = False
        self.visual = False

        self.title("Pyaxium")
        self.geometry(f"{900}x{580}")


        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Pyaxium", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 20))
        
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Stats", command=self.stats)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)


        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Aiming", command=self.aiming)
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Visuals", command=self.visuals)
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Utilities", command=self.Utilities)
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))
        





    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def stats(self):
        self.main = False
        self.stats = True
        self.aim = False
        self.utilities = False
        self.visual = False
        print("stats")

    def aiming(self):
        self.main = False
        self.stats = False
        self.aiming = True
        self.utilities = False
        self.visual = False
        print("aiming")

    def visuals(self):
        self.main = False
        self.stats = False
        self.aiming = False
        self.utilities = False
        self.visual = True
        print("visuals")


    def Utilities(self):
        self.main = False
        self.stats = False
        self.aiming = False
        self.utilities = True
        self.visual = False
        print("Utilities")

    def Bhop(self):
        thread = threading.Thread(target=bhop.bunny)
        thread.start()

if __name__ == "__main__":
    app = App()
    app.mainloop()