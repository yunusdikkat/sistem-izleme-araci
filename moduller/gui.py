import tkinter as tk
from tkinter import ttk
import psutil
import time
from moduller import grafik

def baslat():
    pencere = tk.Tk()
    pencere.title("Sistem İzleme Aracı")

    # Etiketler ve Değişkenler
    cpu_etiket = ttk.Label(pencere, text="CPU Kullanımı: %0")
    cpu_etiket.grid(row=0, column=0, sticky="w")
    cpu_deger = tk.DoubleVar()

    bellek_etiket = ttk.Label(pencere, text="Bellek Kullanımı: %0")
    bellek_etiket.grid(row=1, column=0, sticky="w")
    bellek_deger = tk.DoubleVar()

    disk_etiket = ttk.Label(pencere, text="Disk Kullanımı: %0")
    disk_etiket.grid(row=2, column=0, sticky="w")
    disk_deger = tk.DoubleVar()

    ag_etiket = ttk.Label(pencere, text="Ağ Kullanımı: %0")
    ag_etiket.grid(row=3, column=0, sticky="w")
    ag_deger = tk.DoubleVar()

    # Grafik alanları
    cpu_grafik_alani = tk.Frame(pencere)
    cpu_grafik_alani.grid(row=4, column=0, sticky="ew")

    bellek_grafik_alani = tk.Frame(pencere)
    bellek_grafik_alani.grid(row=5, column=0, sticky="ew")

    disk_grafik_alani = tk.Frame(pencere)
    disk_grafik_alani.grid(row=6, column=0, sticky="ew")

    ag_grafik_alani = tk.Frame(pencere)
    ag_grafik_alani.grid(row=7, column=0, sticky="ew")

    # Grafik verileri için listeler
    cpu_verileri = []
    bellek_verileri = []
    disk_verileri = []
    ag_verileri = []

    # Bilgileri güncelleyen fonksiyon
    def bilgileri_guncelle():
        cpu_yuzdesi = psutil.cpu_percent(interval=0.1)
        cpu_deger.set(cpu_yuzdesi)
        cpu_etiket.config(text=f"CPU Kullanımı: %{cpu_yuzdesi:.1f}")

        bellek = psutil.virtual_memory()
        bellek_yuzdesi = bellek.percent
        bellek_deger.set(bellek_yuzdesi)
        bellek_etiket.config(text=f"Bellek Kullanımı: %{bellek_yuzdesi:.1f}")

        disk = psutil.disk_usage("/")
        disk_yuzdesi = disk.percent
        disk_deger.set(disk_yuzdesi)
        disk_etiket.config(text=f"Disk Kullanımı: %{disk_yuzdesi:.1f}")

        ag_arayuzleri = psutil.net_if_addrs()
        ag_io = psutil.net_io_counters(pernic=True)
        for arayuz, detaylar in ag_arayuzleri.items():
            if arayuz in ag_io:
                io_counters = ag_io[arayuz]
                ag_gonderilen = io_counters.bytes_sent / (1024)
                ag_alinan = io_counters.bytes_recv / (1024)
                ag_deger.set(ag_gonderilen + ag_alinan)
                ag_etiket.config(text=f"Ağ Kullanımı: %{ag_gonderilen + ag_alinan:.1f} KB")
                break

        # Grafik verilerini güncelle
        cpu_verileri.append(cpu_yuzdesi)
        bellek_verileri.append(bellek_yuzdesi)
        disk_verileri.append(disk_yuzdesi)
        ag_verileri.append(ag_gonderilen + ag_alinan)

        # Grafikleri oluştur veya güncelle
        grafik.grafik_olustur(pencere, cpu_verileri, "CPU Kullanımı", "Zaman", "Yüzde", cpu_grafik_alani)
        grafik.grafik_olustur(pencere, bellek_verileri, "Bellek Kullanımı", "Zaman", "Yüzde", bellek_grafik_alani)
        grafik.grafik_olustur(pencere, disk_verileri, "Disk Kullanımı", "Zaman", "Yüzde", disk_grafik_alani)
        grafik.grafik_olustur(pencere, ag_verileri, "Ağ Kullanımı", "Zaman", "KB", ag_grafik_alani)

        pencere.after(1000, bilgileri_guncelle)

    bilgileri_guncelle()
    pencere.mainloop()