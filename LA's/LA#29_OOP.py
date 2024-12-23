print("SUMAYLO-BSIT2B-LA29")

import tkinter as tk

window = tk.Tk()
name = "Rivaii Heichou"
section = "BSIT 2B"
window.title(f"OOP LA28 {name}")
window.geometry("500x500")
window.configure(bg="black")
how = tk.Label(window, text=f"OOP LA29 {name} {section}")
how.grid(row=000, column=000, padx=250, pady=250)

window.mainloop()