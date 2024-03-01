
import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from tkcalendar import Calendar  # Import Calendar widget from tkcalendar
import sql_mod
import datetime
import sql_modul


root = tk.Tk()
pgen_root=1400
pyuks_root=800

ekrangen= root.winfo_screenwidth()
ekranyuks=root.winfo_screenheight()

x=(ekrangen-pgen_root)//2
y=(ekranyuks-pyuks_root)//2
root.geometry(f"{pgen_root}x{pyuks_root}+{x}+{y}")

root.geometry("1400x800")
root.title("BATIKENT HALISAHA")

frm = ttk.Frame(root)
frm.grid(column=0, row=0, padx=50, pady=50)


saatler= ["17:00","", "18:00","","19:00","", "20:00","", "21:00","", "22:00","", "23:00","", "00:00","", "01.00","", "02.00",""]
gunler = ["PAZARTESİ", "SALI", "ÇARŞAMBA", "PERŞEMBE", "CUMA", "CUMARTESİ", "PAZAR"]
servis=["Servis 1","Servis 2","Servis 3"]
rehber_list = sql_mod.sql_query("rehber")

x=0
y=0

for i in gunler:
    ttk.Label(frm, text=i).grid(column=x+1, row=0)
    x+=1

for i in saatler:
    ttk.Label(frm, text=i).grid(column=0, row=y+1)
    y+=1

combo_list=[]

list_no=0

for i in range(7):
    for j in range(20):
        if j%2==0:
            combo = ttk.Combobox(frm, values=rehber_list, width=25)
            combo.grid(column=i+1, row=j+1, padx=5, pady=5)
            combo_list.append(combo)
        else:
            combo = ttk.Combobox(frm, values=servis, width=25)
            combo.grid(column=i + 1, row=j + 1, padx=5, pady=5)
            combo_list.append(combo)
    list_no+=1

def guncel_dolum():
    today = datetime.datetime.today()
    iso_calendar = today.isocalendar()
    mevcut_hafta = iso_calendar[1]

    sonuc = sql_modul.sql_query("takvim", "*", "hafta", mevcut_hafta)

    if len(sonuc) == 70:
        t = 0
        for i in range(0, len(combo_list), 2):
            pair = combo_list[i:i + 2]
            pair[0].set(sonuc[t][3])
            pair[1].set(sonuc[t][4])

            t += 1
    else:
        repetitions = 70 - len(sonuc)
        none_tuple = ("None",) * 5
        sonuc = sonuc + [none_tuple] * repetitions

        t = 0
        for i in range(0, len(combo_list), 2):
            pair = combo_list[i:i + 2]
            pair[0].set(sonuc[t][3])
            pair[1].set(sonuc[t][4])

            t += 1
guncel_dolum()

def show_calendar():

    cal = Calendar(selectmode="day", date_pattern="yyyy-mm-dd")
    cal.place(x=170, y=535)

    def on_select(event=None):

        cal.destroy()
        selected_date = cal.get_date()

        for comb in combo_list:
            comb.delete(0, tk.END)

        date_obj = datetime.datetime.strptime(selected_date, "%Y-%m-%d")
        iso_year, secilen_hafta, _ = date_obj.isocalendar()

        today = datetime.datetime.today()
        iso_calendar = today.isocalendar()
        mevcut_hafta = iso_calendar[1]

        sonuc = sql_modul.sql_query("takvim", "*", "hafta", secilen_hafta)

        if not sonuc:
            for combo in combo_list:
                combo.set("None")
                combo.config(state='disabled')

        elif secilen_hafta==mevcut_hafta:

            t = 0
            for i in range(0, len(combo_list), 2):
                pair = combo_list[i:i + 2]
                pair[0].set(sonuc[t][3])
                pair[1].set(sonuc[t][4])
                pair[0].config(state='normal')
                pair[1].config(state='normal')
                t += 1

        else:

            if len(sonuc)==70:
                t = 0
                for i in range(0, len(combo_list), 2):
                    pair = combo_list[i:i + 2]
                    pair[0].set(sonuc[t][3])
                    pair[1].set(sonuc[t][4])
                    pair[0].config(state='disabled')
                    pair[1].config(state='disabled')
                    t += 1
            else :
                repetitions= 70-len(sonuc)
                none_tuple = ("None",) * 5
                sonuc = sonuc + [none_tuple] * repetitions

                t = 0
                for i in range(0, len(combo_list), 2):
                    pair = combo_list[i:i + 2]
                    pair[0].set(sonuc[t][3])
                    pair[1].set(sonuc[t][4])
                    pair[0].config(state='disabled')
                    pair[1].config(state='disabled')
                    t += 1

    cal.bind("<<CalendarSelected>>", on_select)

btn_calendar = ttk.Button(root, text="Takvim", command=show_calendar)
btn_calendar.place(x=80, y=700)


def kisi_listesi(ekle=None):
    top = tk.Toplevel()
    top.geometry("700x350")
    top.title("Üye Listesi")
    lb_1 = tk.Listbox(top, width=35, height=15)
    lb_1.place(x=40, y=15)

    scrollbar = tk.Scrollbar(top)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
    lb_1.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb_1.yview)
    scrollbar.place(x=235, y=10, height=260)

    def double_click(event):

        top_2 = tk.Toplevel()
        top_2.geometry("350x150")
        top_2.title("Kişi Güncelle")

        entry_name = tk.Entry(top_2)
        entry_name.place(x=120, y=30, width=165)

        entry_phone = tk.Entry(top_2)
        entry_phone.place(x=120, y=60, width=165)

        tk.Label(top_2, text="Adı Soyadi").place(x=50, y=30)
        tk.Label(top_2, text="Telefon No").place(x=50, y=60)

        def kisi_guncelle():


            liste_index = lb_1.curselection()
            if liste_index:
                secilen = lb_1.get(liste_index)
                name, phone = secilen.split(" - ")

            name_new = entry_name.get()
            phone_new = entry_phone.get()

            try:
                vt = sql.connect('test.db')
                cursor = vt.cursor()
                cursor.execute("UPDATE kisi_listesi SET isim=?, telefon=? WHERE isim=? AND telefon=?",
                               (name_new, phone_new, name, phone))
                vt.commit()
                vt.close()
            except:
                pass

        b3 = tk.Button(top_2, text="Güncelle", command=kisi_guncelle)
        b3.place(x=120, y=90, width=80, height=25)



        liste_index = lb_1.curselection()
        if liste_index:
            secilen = lb_1.get(liste_index)
            name, phone = secilen.split(" - ")
            entry_name.delete(0, tk.END)
            entry_name.insert(0, name)
            entry_phone.delete(0, tk.END)
            entry_phone.insert(0, phone)

    lb_1.bind("<Double-Button-1>", double_click)

    def on_close():
        top.destroy()

    top.protocol("WM_DELETE_WINDOW", on_close)



    for i in rehber_list:
        lb_1.insert(tk.END, i[0]+" - "+str(i[1]))

    def kisi_sil():
        liste_index = lb_1.curselection()
        if liste_index:
            secilen = lb_1.get(liste_index)
            name, phone = secilen.split(" - ")

            sql_mod.sql_delete("rehber", name, phone)


            lb_1.delete(0, tk.END)
            rehber_list.clear()
            rehber_list.extend(sql_mod.sql_query("rehber"))
            for i in rehber_list:
                lb_1.insert(tk.END, i[0]+" - "+str(i[1]))

    entry_name = tk.Entry(top)
    entry_name.place(x=400, y=40, width=165)

    entry_phone = tk.Entry(top)
    entry_phone.place(x=400, y=60, width=165)

    tk.Label(top, text="Adı Soyadi").place(x=320, y=40)
    tk.Label(top, text="Telefon No").place(x=320, y=60)


    def duzenle():
        liste_index = lb_1.curselection()
        if liste_index:
            secilen = lb_1.get(liste_index)
            name, phone = secilen.split(" - ")
            entry_name.delete(0, tk.END)
            entry_name.insert(0, name)
            entry_phone.delete(0, tk.END)
            entry_phone.insert(0, phone)

    def kisi_yeni():
        name_new = entry_name.get()
        phone_new = entry_phone.get()

        sql_mod.sql_into("rehber", name_new, phone_new)

        lb_1.delete(0, tk.END)
        rehber_list.clear()
        rehber_list.extend(sql_mod.sql_query("rehber"))
        for i in rehber_list:
            lb_1.insert(tk.END, i[0] + " - " + str(i[1]))


    #b1 = tk.Button(top, text="Düzenle")
    #b1.place(x=40, y=270, width=90, height=30)

    b2 = tk.Button(top, text="Sil", command=kisi_sil)
    b2.place(x=140, y=270, width=90, height=30)



    b4 = tk.Button(top, text="Yeni Kisi Ekle", command=kisi_yeni)
    b4.place(x=490, y=90, width=80, height=25)

    top.mainloop()

def kaydet():
    pass





kaydet = ttk.Button(root, text="Kaydet", command=kaydet)
kaydet.place(x=1280, y=700)

menubar = tk.Menu(root)
root.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Kişi Listesi", command=kisi_listesi)
filemenu.add_command(label="Kişi Ekle")
filemenu.add_command(label="Close")

menubar.add_cascade(label="Rehber", menu=filemenu)



#current_date = datetime.date.today()
#formatted_date = current_date.strftime("%Y-%m-%d")



root.mainloop()