import tkinter as tk
from tkinter import messagebox

# Dosya işlemleri
def notlari_oku():
    try:
        with open("notlar.txt", "r", encoding="utf-8") as f:
            return [n.strip() for n in f.readlines()]
    except FileNotFoundError:
        return []

def notlari_yaz(notlar):
    with open("notlar.txt", "w", encoding="utf-8") as f:
        for n in notlar:
            f.write(n + "\n")

# Not ekleme
def not_ekle():
    yeni_not = entry.get()
    if yeni_not:
        listbox.insert(tk.END, yeni_not)
        notlari_yaz(listbox.get(0, tk.END))
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen boş not eklemeyin!")

# Not silme
def not_sil():
    secim = listbox.curselection()
    if secim:
        listbox.delete(secim)
        notlari_yaz(listbox.get(0, tk.END))
    else:
        messagebox.showwarning("Uyarı", "Silmek için bir not seçin!")

# Ana pencere
window = tk.Tk()
window.title("Not Defteri")
window.geometry("400x400")
window.config(bg="#f0f0f0")

# Liste kutusu
listbox = tk.Listbox(window, width=40, height=15, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Önceden kayıtlı notları yükle
for n in notlari_oku():
    listbox.insert(tk.END, n)

# Giriş alanı
entry = tk.Entry(window, width=30)
entry.pack(pady=5)

# Butonlar
frame = tk.Frame(window)
frame.pack(pady=5)

ekle_btn = tk.Button(frame, text="Ekle", command=not_ekle, bg="#4CAF50", fg="white", width=10)
ekle_btn.grid(row=0, column=0, padx=5)

sil_btn = tk.Button(frame, text="Sil", command=not_sil, bg="#f44336", fg="white", width=10)
sil_btn.grid(row=0, column=1, padx=5)

# Çalıştır
window.mainloop()
