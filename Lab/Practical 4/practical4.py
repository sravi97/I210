from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #canvas
        self.canvas = Canvas(self, height = 310, width = 500)
        self.canvas.grid(row = 1, column = 0, rowspan = 6)
        self.x, self.y = 20, 20
        
        #labels
        Label(self, text = "Roman Numeral Canvas").grid(row = 0, column = 0, columnspan = 30)
        Label(self, text = "Number:").grid(row = 1, column = 1, sticky = E)
        Label(self, text = "Line Width:").grid(row = 2, column = 1, sticky = W)
        Label(self, text = "Line Color:").grid(row = 3, column = 1, sticky = W)

        #entry
        self.number = Entry(self, width = 17)
        self.number.grid(row = 1, column = 2, columnspan = 2, sticky = W)

        #checkboxes
        self.numbers = BooleanVar()
        Checkbutton(self, text = "Numbers", variable = self.numbers).grid(row = 1, column = 4, sticky = E)
        
        #radio buttons
        self.ln_width = StringVar()
        self.ln_width.set("one")
        Radiobutton(self, text = "1", value = "one", variable = self.ln_width).grid(row = 2, column = 2)
        Radiobutton(self, text = "3", value = "three", variable = self.ln_width).grid(row = 2, column = 3)
        Radiobutton(self, text = "5", value = "five", variable = self.ln_width).grid(row = 2, column = 4)

        self.ln_color = StringVar()
        self.ln_color.set("black")
        Radiobutton(self, text = "Black", value = "black", variable = self.ln_color).grid(row = 3, column = 2)
        Radiobutton(self, text = "Red", value = "red", variable = self.ln_color).grid(row = 3, column = 3)
        Radiobutton(self, text = "Blue", value = "blue", variable = self.ln_color).grid(row = 3, column = 4)
        
        #buttons
        self.roman = PhotoImage(file = "roman.gif")
        Button(self, image = self.roman, command = self.numerals).grid(row = 4, column = 2, rowspan = 3)

        self.face = PhotoImage(file = "random.gif")
        Button(self, image = self.face, command = self.random).grid(row = 4, column = 4, rowspan = 3, sticky = E)

    def numerals(self):
        for char in self.number.get():
            #drawing the roman numerals
            #didn't have enough time to figure out all the coordinates, but I was creating lines to draw the letters
            #since the length and width of every letter was given, I calculated the coordinates
            if char == "M":
                self.canvas.create_line(20, 20, 26, 20)
                self.canvas.create_line(23, 20, 23, -20)
                self.canvas.create_line(23, -20, 30, 0)

            if char == "D":
            if char == "C":
            if char == "L":
            if char == "X":
            if char == "V":
            if char == "I":

#changing color and size

        if self.ln_width == "one"
            self.canvas.create_line(width = 1)

        if self.ln_width == "three"
            self.canvas.create_line(width = 3)

        if self.ln_width == "five":
            self.canvas.create_line(width = 5)

        if self.ln_color == "black"
            self.canvas.create_line(fill = black)

        if self.ln_color == "red"
            self.canvas.create_line(fill = red)

        if self.ln_color == "blue"
            self.canvas.create_line(fill = blue)

    def random(self):
        

        

            
            
        
# main
root = Tk()
root.title("Roman Numerals")
root.geometry("900x350")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
