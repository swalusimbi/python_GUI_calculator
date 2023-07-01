import tkinter as tk


def button_click(num):
    entry_text.insert(tk.END, str(num))


def button_clear():
    entry_text.delete("1.0", tk.END)


def button_clear_input():
    entry_text.delete("end-2c")


def button_add():
    first_num = entry_text.get("1.0", tk.END).strip()
    global f_num
    global operation
    operation = "addition"
    f_num = float(first_num)
    entry_text.insert(tk.END, " + ")


def button_subtract():
    first_num = entry_text.get("1.0", tk.END).strip()
    global f_num
    global operation
    operation = "subtraction"
    f_num = float(first_num)
    entry_text.insert(tk.END, " - ")


def button_multiply():
    first_num = entry_text.get("1.0", tk.END).strip()
    global f_num
    global operation
    operation = "multiplication"
    f_num = float(first_num)
    entry_text.insert(tk.END, " * ")


def button_divide():
    first_num = entry_text.get("1.0", tk.END).strip()
    global f_num
    global operation
    operation = "division"
    f_num = float(first_num)
    entry_text.insert(tk.END, " / ")


def button_equal():
    expression = entry_text.get("1.0", tk.END).strip()
    entry_text.delete("1.0", tk.END)

    try:
        result = eval(expression)
        entry_text.insert(tk.END, expression + "\n= " + str(result).rjust(28))
    except:
        entry_text.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Silver Walusimbi's Calculator")
root.configure(bg="light gray")

# Create a Text widget for input and output
entry_text = tk.Text(root, height=2, width=30, borderwidth=5)
entry_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
button_1 = tk.Button(root, text="1", padx=30, pady=20,
                     command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=30, pady=20,
                     command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=30, pady=20,
                     command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=30, pady=20,
                     command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=30, pady=20,
                     command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=30, pady=20,
                     command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=30, pady=20,
                     command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=30, pady=20,
                     command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=30, pady=20,
                     command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=30, pady=20,
                     command=lambda: button_click(0))

# Create operation buttons
button_add = tk.Button(root, text="+", padx=30, pady=20,
                       font=("Arial", 14), command=button_add)
button_subtract = tk.Button(
    root, text="-", padx=33, pady=20, font=("Arial", 14), command=button_subtract)
button_multiply = tk.Button(
    root, text="*", padx=30, pady=20, font=("Arial", 14), command=button_multiply)
button_divide = tk.Button(root, text="/", padx=33,
                          pady=20, font=("Arial", 14), command=button_divide)

# Create clear and equal buttons
button_clear = tk.Button(root, text="Clear All", padx=70,
                         pady=20, command=button_clear)
button_clear_input = tk.Button(
    root, text="Clear Input", padx=20, pady=20, command=button_clear_input)
button_equal = tk.Button(root, text="=", padx=30, pady=20,
                         font=("Arial", 14), command=button_equal)

# Place the buttons on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_clear_input.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

# Run the main event loop
root.mainloop()
