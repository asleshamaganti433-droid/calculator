from tkinter import *

# Global expression string
expression = ""

# Function to update the expression
def press(key):
    global expression
    expression += str(key)
    display.set(expression)

# Function to evaluate result
def equal():
    global expression
    try:
        result = str(eval(expression))
        display.set(result)
        expression = ""
    except:
        display.set("Error")
        expression = ""

# Clear everything
def clear():
    global expression
    expression = ""
    display.set("")

# Create main window
root = Tk()
root.title("Simple Calculator")
root.geometry("300x350")

display = StringVar()
expression = ""

# Entry field for display
entry = Entry(root, textvariable=display, font=("Arial", 18), bd=5, insertwidth=2, justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, pady=10)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for btn_text in buttons:
    button = Button(root, text=btn_text, font=("Arial", 14), width=5, height=2,
                    command=lambda t=btn_text: press(t) if t != "=" else equal())
    button.grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
clear_button = Button(root, text="C", font=("Arial", 14), width=5, height=2, command=clear)
clear_button.grid(row=row, column=1, padx=2, pady=2)

root.mainloop()
