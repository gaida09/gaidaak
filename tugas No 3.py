import tkinter as tk
from tkinter import messagebox

def simpan_data():
    data = f"""
Nama: {entry_nama.get()}
Tanggal Lahir: {entry_tgl.get()}
Asal Sekolah: {entry_sekolah.get()}
NISN: {entry_nisn.get()}
Nama Ayah: {entry_ayah.get()}
Nama Ibu: {entry_ibu.get()}
No HP: {entry_hp.get()}
Alamat: {text_alamat.get("1.0", tk.END)}
"""
    messagebox.showinfo("Data Tersimpan", "Data siswa berhasil disimpan!")
    print(data)

def hapus_data():
    entry_nama.delete(0, tk.END)
    entry_tgl.delete(0, tk.END)
    entry_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_hp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

root = tk.Tk()
root.title("DATA SISWA BARU")
root.geometry("500x600")
root.configure(bg="#dff6f5")

judul = tk.Label(root, text="DATA SISWA BARU",
                 font=("Arial", 18, "bold"),
                 bg="#a8dadc")
judul.pack(fill="x", pady=10)

frame = tk.Frame(root, bg="#dff6f5")
frame.pack(pady=10)

def buat_label_entry(teks):
    tk.Label(frame, text=teks, bg="#dff6f5").pack(anchor="w")
    entry = tk.Entry(frame, width=50)
    entry.pack(pady=5)
    return entry

entry_nama = buat_label_entry("Nama Lengkap")
entry_tgl = buat_label_entry("Tanggal Lahir")
entry_sekolah = buat_label_entry("Asal Sekolah")
entry_nisn = buat_label_entry("NISN")
entry_ayah = buat_label_entry("Nama Ayah")
entry_ibu = buat_label_entry("Nama Ibu")
entry_hp = buat_label_entry("Nomor Telepon / HP")

tk.Label(frame, text="Alamat", bg="#dff6f5").pack(anchor="w")
text_alamat = tk.Text(frame, width=50, height=5)
text_alamat.pack(pady=5)

frame_button = tk.Frame(root, bg="#dff6f5")
frame_button.pack(pady=20)

tk.Button(frame_button, text="Hapus", bg="orange",
          command=hapus_data, width=10).pack(side="left", padx=10)

tk.Button(frame_button, text="Simpan", bg="orange",
          command=simpan_data, width=10).pack(side="left", padx=10)

root.mainloop()