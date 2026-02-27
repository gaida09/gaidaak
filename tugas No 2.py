import tkinter as tk
from tkinter import messagebox
from datetime import datetime

BIAYA_PER_JAM = 2000

def hitung_biaya():
    try:
        masuk = entry_masuk.get()
        keluar = entry_keluar.get()

        format_waktu = "%H:%M"

        waktu_masuk = datetime.strptime(masuk, format_waktu)
        waktu_keluar = datetime.strptime(keluar, format_waktu)

        selisih = waktu_keluar - waktu_masuk
        jam = selisih.seconds / 3600

        total = jam * BIAYA_PER_JAM

        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, str(int(total)))

    except:
        messagebox.showerror("Error", "Format waktu harus HH:MM")

root = tk.Tk()
root.title("Aplikasi Parkir")
root.geometry("400x400")

tk.Label(root, text="No Plat Polisi").pack()
entry_plat = tk.Entry(root)
entry_plat.pack()

tk.Label(root, text="Waktu Masuk (HH:MM)").pack()
entry_masuk = tk.Entry(root)
entry_masuk.pack()

tk.Label(root, text="Waktu Keluar (HH:MM)").pack()
entry_keluar = tk.Entry(root)
entry_keluar.pack()

tk.Label(root, text="Biaya").pack()
entry_biaya = tk.Entry(root)
entry_biaya.pack()

tk.Button(root, text="Hitung Biaya", command=hitung_biaya).pack(pady=10)

tk.Label(root, text="Biaya Per Jam Rp 2.000", fg="red").pack(pady=20)

root.mainloop()