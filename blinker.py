import tkinter as tk

class Blinker(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.circle_radius = 7
        self.circle_color = "red"
        self.visible = True
        self.toggle_circle()

    def toggle_circle(self):
        if self.visible:
            self.draw_circle()
        else:
            self.delete("all")
        self.visible = not self.visible
        self.after(500, self.toggle_circle)  # Toggle every 500 milliseconds

    def draw_circle(self):
        # Calculate circle coordinates
        x0 = self.winfo_width() // 2 - self.circle_radius
        y0 = self.winfo_height() // 2 - self.circle_radius
        x1 = self.winfo_width() // 2 + self.circle_radius
        y1 = self.winfo_height() // 2 + self.circle_radius
        
        # Draw or delete the circle based on visibility
        if self.visible:
            self.create_oval(x0, y0, x1, y1, fill=self.circle_color)
        else:
            self.delete("all")
    def configure(self, color):
        self.circle_color = color
        


