import tkinter as tk
from tkinter import messagebox


def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        simple_interest = (principal * rate * time) / 100
        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        label_si_result.config(text=f"Simple Interest: {simple_interest:.2f}")
        label_ci_result.config(text=f"Compound Interest: {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


def clear_fields():
    entry_principal.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    label_si_result.config(text="Simple Interest: 0.00")
    label_ci_result.config(text="Compound Interest: 0.00")


root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x280")
root.resizable(False, False)

tk.Label(root, text="Principal Amount ($):").grid(row=0, column=0, padx=15, pady=10, sticky="w")
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=15, pady=10)

tk.Label(root, text="Rate of Interest (%):").grid(row=1, column=0, padx=15, pady=10, sticky="w")
entry_rate = tk.Entry(root)
entry_rate.grid(row=1, column=1, padx=15, pady=10)

tk.Label(root, text="Time Period (Years):").grid(row=2, column=0, padx=15, pady=10, sticky="w")
entry_time = tk.Entry(root)
entry_time.grid(row=2, column=1, padx=15, pady=10)

btn_calculate = tk.Button(root, text="Calculate", command=calculate_interest, width=12)
btn_calculate.grid(row=3, column=0, padx=15, pady=15)

btn_clear = tk.Button(root, text="Clear", command=clear_fields, width=12)
btn_clear.grid(row=3, column=1, padx=15, pady=15)

label_si_result = tk.Label(root, text="Simple Interest: 0.00", font=("Arial", 10, "bold"))
label_si_result.grid(row=4, column=0, columnspan=2, pady=5)

label_ci_result = tk.Label(root, text="Compound Interest: 0.00", font=("Arial", 10, "bold"))
label_ci_result.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
