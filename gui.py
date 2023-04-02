import tkinter
import tkinter.messagebox
import customtkinter
import threading
import bhop
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
        
        def checkmenu():
                if self.main:
                            self.frame = customtkinter.CTkFrame(master=self, width=740, height=80, corner_radius=8)
                            self.frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
                            self.label = customtkinter.CTkLabel(self.frame, text='Welcome to pyaxium!', font=('', 18, 'bold'))
                            self.label.place(relx=0.5, rely=0.12, anchor=tkinter.CENTER)
                            self.label2 = customtkinter.CTkLabel(self.frame, text="Welcome to the cheat suite for cs:go made by ax11! I hope you will have fun using this client.", font=('', 14, 'normal'))
                            self.label2.place(relx=0.5, rely=0.26, anchor=tkinter.CENTER)
                            self.label3 = customtkinter.CTkLabel(self.frame, text="Keep in mind that its a 'legit' client, made to be a help for you to win and not be used as a hvh cheat.", font=('', 14, 'normal'))
                            self.label3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
                elif self.stats:
                            self.framestat = customtkinter.CTkFrame(master=self, width=740, height=20, corner_radius=8)
                            self.framestat.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
                            self.progressbar = customtkinter.CTkProgressBar(master=self.framestat,
                                                                    width=660,
                                                                    height=20,
                                                                    border_width=5)
                            self.progressbar.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
                            self.progressbar.set(10)
                
                time.sleep(0.00001)
                checkmenu()

        thread = threading.Thread(target=checkmenu)
        thread.start()



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