import tkinter as tk
from tkinter import messagebox

def hitung_total():
    try:
        harga = float(entry_harga.get())
        qty = float(entry_qty.get())
        total = harga * qty
        label_total.config(text=f"Total: Rp {total:,.2f}")
    except:
        messagebox.showerror("Error", "Masukkan angka yang benar!")

root = tk.Tk()
root.title("Program Kasir")
root.geometry("300x250")

tk.Label(root, text="Harga").pack(pady=5)
entry_harga = tk.Entry(root)
entry_harga.pack()

tk.Label(root, text="Kuantitas").pack(pady=5)
entry_qty = tk.Entry(root)
entry_qty.pack()

tk.Button(root, text="Hitung Total", command=hitung_total).pack(pady=10)

label_total = tk.Label(root, text="Total: Rp 0.00")
label_total.pack(pady=10)

root.mainloop()