import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from tkinter import messagebox as mb

import sql_mod

root_giris = tk.Tk()

#root_giris.tk_setPalette("#11114b")

pgen=350
pyuks=150

ekrangen= root_giris.winfo_screenwidth()
ekranyuks=root_giris.winfo_screenheight()

x=(ekrangen-pgen)//2
y=(ekranyuks-pyuks)//2

root_giris.geometry(f"{pgen}x{pyuks}+{x}+{y}")
root_giris.title("KULLANICI GİRİŞİ")

entry_giris = tk.Entry()
entry_giris.place(x=130, y=30, width=165)
entry_giris.focus_set()

entry_sifre = tk.Entry(show="*")
entry_sifre.place(x=130, y=60, width=165)

tk.Label(text="Kullanıcı Adı").place(x=50, y=30)
tk.Label(text="Şifre").place(x=50, y=60)

def giris_yap():

    id=entry_giris.get()
    sifre=entry_sifre.get()

    veri = sql_mod.sql_query("kullanici", id, sifre)

    if veri:
        root_giris.destroy()
        import ana_ekran

    else:
        mb.showerror("Hatalı Giriş !", "Lüfren geçerli bir kullanıcı adı ve şifre girin.", icon="error")

def enter_key(event):
    giris_yap()

b_giris = tk.Button(text="Giriş Yap", command=giris_yap)
b_giris.place(x=160, y=90, width=80, height=25)

root_giris.bind('<Return>', enter_key)

root_giris.mainloop()