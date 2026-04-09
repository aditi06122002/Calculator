import tkinter as tk

# Function to update expression
def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Function to clear input
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(True , True)

expression = ""
equation = tk.StringVar()

# Display box
entry = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                        command=equalpress)
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                        command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                        command=lambda t=text: press(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run app
root.mainloop()