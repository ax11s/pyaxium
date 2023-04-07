import tkinter
import tkinter.messagebox
import customtkinter
import threading

import time

        while True:
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
                