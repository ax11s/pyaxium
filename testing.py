import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.last_button_pressed = None
        
        self.create_widgets()
        
    def create_widgets(self):
        self.render_button1 = tk.Button(self)
        self.render_button1["text"] = "Render thing 1"
        self.render_button1["command"] = self.render_thing1
        self.render_button1.pack(side="left")
        
        self.render_button2 = tk.Button(self)
        self.render_button2["text"] = "Render thing 2"
        self.render_button2["command"] = self.render_thing2
        self.render_button2.pack(side="left")
        
        self.render_canvas = tk.Canvas(self, width=300, height=300)
        self.render_canvas.pack()
        
    def render_thing1(self):
        self.last_button_pressed = "thing1"
        self.render_canvas.delete("all") # clear the canvas
        self.render_canvas.create_rectangle(50, 50, 250, 250, fill="blue") # draw a blue rectangle
        
    def render_thing2(self):
        self.last_button_pressed = "thing2"
        self.render_canvas.delete("all") # clear the canvas
        self.render_canvas.create_oval(50, 50, 250, 250, fill="red") # draw a red oval
        
    def update(self):
        if self.last_button_pressed == "thing1":
            # do something if thing1 was last pressed
            pass
        elif self.last_button_pressed == "thing2":
            # do something if thing2 was last pressed
            pass
        
        self.after(100, self.update) # update every 100ms
        
root = tk.Tk()
app = Application(master=root)
app.update()
app.mainloop()