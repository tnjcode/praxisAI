import tkinter as tk
import json
import os
from tkinter import messagebox

filename = 'data.json'

# Memuat data dari file JSON jika ada
if os.path.exists(filename):
    with open(filename, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {'name': '', 'kelas': ''}
else:
    data = {'name': '', 'kelas': ''}
data.setdefault('name', '')
data.setdefault('kelas', '')

window = tk.Tk()

# Label dan Entry untuk Nama
tk.Label(window, text="Nama").pack()
name_entry = tk.Entry(window)
name_entry.insert(tk.INSERT, data['name'])
name_entry.pack()

# Label dan Entry untuk Nomor
tk.Label(window, text="kelas anda").pack()
no_entry = tk.Entry(window)
no_entry.insert(tk.INSERT, data['kelas'])
no_entry.pack()

# Fungsi untuk menyimpan data ke dalam file JSON
def save_command():
    name = name_entry.get()
    nomor = no_entry.get()
    data = {"name": name, "kelas": nomor}
    with open('data.json', 'w') as f:
        json.dump(data, f)
    messagebox.showinfo('Info', f'Hello {name}! kelas: {nomor}')

# Tombol untuk menyimpan inputan
tk.Button(window, text="Save", command=save_command).pack()

window.mainloop()
