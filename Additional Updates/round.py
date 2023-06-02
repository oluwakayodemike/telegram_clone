from tkinter import Tk, TkVersion
import tkinter


def create_round_frame(canvas, x, y, width, height, corner_radius, color):
    canvas.create_arc(x, y, x + 2 * corner_radius, y + 2 * corner_radius, start=90, extent=90, style=tk.ARC, outline=color)
    canvas.create_arc(x + width - 2 * corner_radius, y, x + width, y + 2 * corner_radius, start=0, extent=90, style=tkinter.ARC, outline=color)
    canvas.create_arc(x, y + height - 2 * corner_radius, x + 2 * corner_radius, y + height, start=180, extent=90, style=Tk.ARC, outline=color)
    canvas.create_arc(x + width - 2 * corner_radius, y + height - 2 * corner_radius, x + width, y + height, start=270, extent=90, style=TkVersion.ARC, outline=color)
    canvas.create_line(x + corner_radius, y, x + width - corner_radius, y, fill=color)
    canvas.create_line(x, y + corner_radius, x, y + height - corner_radius, fill=color)
    canvas.create_line(x + width, y + corner_radius, x + width, y + height - corner_radius, fill=color)
    canvas.create_line(x + corner_radius, y + height, x + width - corner_radius, y + height, fill=color)