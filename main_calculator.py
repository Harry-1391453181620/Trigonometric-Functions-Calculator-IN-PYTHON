import tkinter as tk
from tkinter import messagebox
from definitions import *

functions = [
        "", "Sine Function: sin","Cosine Function: cos","Tangent Function: tan","Cotangent Function: cot","Secant Function: sec","Cosecant Function: csc","Arcsine Function: asin","Arccosine Function: acos","Arctangent Function: atan","Arccotangent Function: acot","Arcsecant Function: asec","Arccosecant Function: acsc","Versed Sine Function: versin","Coversed Sine Function: coversin","Haversine Function: haversin","Hacoversed Sine Function: hacoversin","Exsecant Function: exsec","Excosecnt Function: excsc",
    ]

def show_welcome():
    root = tk.Tk()
    root.title("Welcome Page")
    root.geometry("400x300")
    root.configure(bg="black")

    label = tk.Label(root, text="Welcome to Trigonometric Functions Calculator", fg="white", bg="black", font=("Helvetica", 12))
    label.pack(pady=50)

    label2 = tk.Label(root, text="Please choose which function to calculate: ", fg="white", bg="black", font=("Helvetica", 10))
    label2.pack()

    for i, func in enumerate(functions[1:]):
        button = tk.Button(root, text=func, fg="white", bg="gray",
                           command=lambda func_idx=i + 1: select_function(root, func_idx), width=30, font=("Helvetica", 10))
        button.pack(pady=1)

    root.mainloop()

def select_function(parent, func_choice):
    root = tk.Tk()
    root.title("Trigonometric Functions Calculator")
    root.geometry("400x300")
    root.configure(bg="black")

    label = tk.Label(root, text=f"You chose: {get_function_name(func_choice)}", fg="white", bg="black", font=("Helvetica", 12))
    label.pack(pady=20)

    label2 = tk.Label(root, text="Please choose the way of calculate: ", fg="white", bg="black", font=("Helvetica", 10))
    label2.pack()

    button1 = tk.Button(root, text="Please enter the ratio of sides and calculate angle values", fg="white", bg="grey",
                        command=lambda: calculate_mode(parent, func_choice, 1), width=50)
    button1.pack(pady=5)

    button2 = tk.Button(root, text="Please enter the angle values and calculate ratio of sides", fg="white", bg="grey",
                        command=lambda: calculate_mode(parent, func_choice, 2), width=50)
    button2.pack(pady=5)

    back_button = tk.Button(root, text="Return", fg="white", bg="grey", command=lambda: show_welcome(), width=10)
    back_button.pack(pady=10)

    root.mainloop()

def get_function_name(func_choice):
    return functions[func_choice]

def calculate_mode(parent, func_choice, mode_choice):
    root = tk.Tk()
    root.title("Calculating space")
    root.geometry("400x300")
    root.configure(bg="black")

    if mode_choice == 1:
        label = tk.Label(root, text="Please input the values: ", fg="white", bg="black", font=("Helvetica", 10))
        label.pack(pady=10)

        entry = tk.Entry(root)
        entry.pack(pady=5)

        calculate_button = tk.Button(root, text="Calculate", fg="white", bg="grey",
                                                                         command=lambda: calculate(root, func_choice, mode_choice, entry.get()), width=30)
        calculate_button.pack(pady=10)

    else:
        label = tk.Label(root, text="please input the value of angle: ", fg="white", bg="black", font="Helvetica, 10")
        label.pack(pady=10)

        entry = tk.Entry(root)
        entry.pack(pady=5)

        calculate_button = tk.Button(root, text="Calculate", fg="white", bg="grey",
                                                                         command=lambda: calculate(root, func_choice, mode_choice, entry.get()), width=30)
        calculate_button.pack(pady=10)

    back_button = tk.Button(root, text="Return", fg="white", bg="grey",
                            command=lambda: show_welcome(), width=10)
    back_button.pack(pady=10)

    root.mainloop()

def calculate(parent, func_choice, mode_choice, value):
    try:
        value = float(value)
        if mode_choice == 1:
            if func_choice == 1:
                result = sin_func(value)
            elif func_choice == 2:
                result = cos_func(value)
            elif func_choice == 3:
                result = tan_func(value)
            elif func_choice == 4:
                result = cot_func(value)
            elif func_choice == 5:
                result = sec_func(value)
            elif func_choice == 6:
                result = csc_func(value)
            elif func_choice == 7:
                result = arcsin_func(value)
            elif func_choice == 8:
                result = arccos_func(value)
            elif func_choice == 9:
                result = arctan_func(value)
            elif func_choice == 10:
                result = arctan_func(value)
            elif func_choice == 11:
                result = arcsec_func(value)
            elif func_choice == 12:
                result = arccsc_func(value)
            elif func_choice == 13:
                result = versin_func(value)
            elif func_choice == 14:
                result = coversin_func(value)
            elif func_choice == 15:
                result = haversin_func(value)
            elif func_choice == 16:
                result = hacoversin_func(value)
            elif func_choice == 17:
                result = exsec_func(value)
            elif func_choice == 18:
                result = excsc_func(value)
            else:
                messagebox.showerror("Error","This kind of function is not available in this app or it is not available to use the ratio of sides to calculate the value of angle.")
                return
        else:
            if func_choice <= 6:
                if func_choice == 1:
                    result = sin_func(value)
                elif func_choice == 2:
                    result = cos_func(value)
                elif func_choice == 3:
                    result = tan_func(value)
                elif func_choice == 4:
                    result = cot_func(value)
                elif func_choice == 5:
                    result = sec_func(value)
                elif func_choice == 6:
                    result = csc_func(value)
                elif func_choice == 7:
                    result = arcsin_func(value)
                elif func_choice == 8:
                    result = arccos_func(value)
                elif func_choice == 9:
                    result = arctan_func(value)
                elif func_choice == 10:
                    result = arctan_func(value)
                elif func_choice == 11:
                    result = arcsec_func(value)
                elif func_choice == 12:
                    result = arccsc_func(value)
                elif func_choice == 13:
                    result = versin_func(value)
                elif func_choice == 14:
                    result = coversin_func(value)
                elif func_choice == 15:
                    result = haversin_func(value)
                elif func_choice == 16:
                    result = hacoversin_func(value)
                elif func_choice == 17:
                    result = exsec_func(value)
                elif func_choice == 18:
                    result = excsc_func(value)
            else:
                messagebox.showerror("Error", "This kind of function is not available in this app or it is not available to use the value of angle to calculate the ratio of sides.")
                return

        print(f"The result is:{result}")
        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error","Unavailable input, please try again with another number.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
if __name__ == "__main__":
    show_welcome()
