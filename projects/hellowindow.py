import tkinter as tk

### THIS PROJECT PRINTS HELLO WINDOW ON A APPLICATION WINDOW SO WE GET TO PRINT OUT MESSAGE NOT TO THE TERMINAL BUT TO A BAD-ASS GUI

# This code below will create a window using tkinter library which is a GUI toolkit. (https://docs.python.org/3/library/tkinter.html)
window = tk.Tk()

# This code below will define the title of the window. 
window.title("Hello Window")

# This code below will determine the screen size
window.geometry("800x400")

# This code below will print given text in the window
message = tk.Label(window, text="Hello Window!")

# This code below will determine the location of the text
message.pack(padx=20, pady=100)

# This code below will keep the window running
window.mainloop()
