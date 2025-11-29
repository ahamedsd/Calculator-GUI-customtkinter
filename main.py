import customtkinter as ctk

# Functions
def press(num):
    entry_var.set(entry_var.get() + str(num))

def clear():
    entry_var.set("")

def equal():
    try:
        entry_var.set(str(eval(entry_var.get())))
    except:
        entry_var.set("Error")

# Window setup
root = ctk.CTk()
root.title("Calculator")  # Window title
root.geometry("350x500")

# Entry field
entry_var = ctk.StringVar()
display = ctk.CTkEntry(root, textvariable=entry_var, font=("Arial", 30), justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20, ipady=10)

# Buttons layout
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['C','0','=','+']
]

for i, row in enumerate(buttons):
    for j, b in enumerate(row):
        if b == "=":
            action = equal
        elif b == "C":
            action = clear
        else:
            action = lambda x=b: press(x)
        
        btn = ctk.CTkButton(root, text=b, command=action, fg_color="black", text_color="white",
                             font=("Arial", 20), corner_radius=20)
        btn.grid(row=i+1, column=j, sticky="nsew", padx=5, pady=5)

# Make rows and columns expand equally
total_rows = len(buttons) + 1  # +1 for entry
for i in range(total_rows):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
