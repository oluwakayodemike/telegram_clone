import tkinter as tk
from tkinter import font

def create_round_frame(canvas, x, y, width, height, corner_radius, color):
    canvas.create_arc(x, y, x + 2 * corner_radius, y + 2 * corner_radius, start=90, extent=90, style=tk.ARC, outline=color)
    canvas.create_arc(x + width - 2 * corner_radius, y, x + width, y + 2 * corner_radius, start=0, extent=90, style=tk.ARC, outline=color)
    canvas.create_arc(x, y + height - 2 * corner_radius, x + 2 * corner_radius, y + height, start=180, extent=90, style=tk.ARC, outline=color)
    canvas.create_arc(x + width - 2 * corner_radius, y + height - 2 * corner_radius, x + width, y + height, start=270, extent=90, style=tk.ARC, outline=color)
    canvas.create_line(x + corner_radius, y, x + width - corner_radius, y, fill=color)
    canvas.create_line(x, y + corner_radius, x, y + height - corner_radius, fill=color)
    canvas.create_line(x + width, y + corner_radius, x + width, y + height - corner_radius, fill=color)
    canvas.create_line(x + corner_radius, y + height, x + width - corner_radius, y + height, fill=color)

root = tk.Tk()


# Customization options for the canvas
canvas_width = 400  # width adjustment
canvas_height = 200  # height adjustment
root.geometry(f"{canvas_width}x{canvas_height}")

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)  # Use the adjusted canvas dimensions
canvas.pack(pady=20)

# Customization options for the round frame
x = 50
y = 50

# all these properties are to be adjusted only for the round frame
width = 300  
height = 30     
corner_radius = 14
color = "#A9A9A9"  # Set the color to light blue (hex code: #ADD8E6)

# Create the round frame using the custom Canvas widget
create_round_frame(canvas, x, y, width, height, corner_radius, color)

entry_font = font.Font(family="Arial", size=10)  # Change the font family and weight

entry_x = x + corner_radius + 5  # Adjust the x position of the text box
entry_y = y + 5  # Adjust the y position of the text box
entry_width = width + 2 * (corner_radius := -17)  # Adjust the width of the text box
entry_height = height - 10  # Adjust the height of the text box

entry = tk.Text(canvas, width=entry_width, height=entry_height, bd=0, bg="white", font=entry_font, fg="black")  # Set the background color and font of the text box
entry.place(x=entry_x, y=entry_y, width=entry_width, height=entry_height)  # Adjust the positioning and dimensions of the text box

root.mainloop()

# to get the one for the search, change the corner radius to 20