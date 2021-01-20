import tkinter
import functions
from tkinter import messagebox
from tkinter import Button, Tk

FONT = ("Verdana", 10, "normal")
MAIN_PADX = 20
MAIN_PADY = 20
MAIN_WIDTH = 1400
MAIN_HEIGHT = 720
BUTTON_WIDTH = 20
BUTTON_HEIGHT = 1


main_window = Tk()
main_window.title(string="Misha the Helper")
main_window.config(padx=MAIN_PADX, pady=MAIN_PADY, width=MAIN_WIDTH, height=MAIN_HEIGHT)

# Adding button with Incident number
incident_number = Button()
incident_number.config(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=FONT, text="Pick Incident",
                       highlightthickness=0, command=functions.set_inc)
incident_number.grid(column=0, row=0)

# Adding button with current State of incident
incident_state = Button()
incident_state.config(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=FONT, text="Initial",
                      highlightthickness=0, command=functions.set_inc)
incident_state.grid(column=2, row=0)



main_window.mainloop()
