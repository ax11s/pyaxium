import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.main = True
        self.utilities = False
        self.visual = False

        self.title("Pyaxium")
        self.geometry(f"{900}x{580}")


        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Pyaxium", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 20))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))

        if self.main:
                    self.frame = customtkinter.CTkFrame(master=self, width=740, height=80, corner_radius=8)
                    self.frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
                    self.label = customtkinter.CTkLabel(self.frame, text='Welcome to pyaxium!', font=('', 18, 'bold'))
                    self.label.place(relx=0.5, rely=0.12, anchor=tkinter.CENTER)
                    self.label2 = customtkinter.CTkLabel(self.frame, text="Welcome to the cheat suite for cs:go made by ax11! I hope you will have fun using this client.", font=('', 14, 'normal'))
                    self.label2.place(relx=0.5, rely=0.26, anchor=tkinter.CENTER)
                    self.label3 = customtkinter.CTkLabel(self.frame, text="Keep in mind that its a 'legit' client, made to be a help for you to win and not be used as a hvh cheat.", font=('', 14, 'normal'))
                    self.label3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()