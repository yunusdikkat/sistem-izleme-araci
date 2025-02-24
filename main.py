from moduller import cpu, bellek, disk, ag, uyari, veri_kaydetme
import time 
from moduller import gui

def main():
    while True:
        # Cpu kullanımını izlemek için
        cpu_yuzdesi = cpu.cpu_kullanimi_al()
        print(f"CPU Kullanımı: %{cpu_yuzdesi}")
        # CPU Uyarı Kontrolü
        if cpu_yuzdesi > 80:  # Örnek eşik değeri
            uyari.uyari_ver("CPU", 80, cpu_yuzdesi)
        
        # Bellek kullanımını izlemek için
        bellek_bilgisi = bellek.bellek_kullanimi_al()
        print(f"Toplam Bellek: {bellek_bilgisi['toplam']:.2f} GB")
        print(f"Kullanılan Bellek: {bellek_bilgisi['kullanilan']:.2f} GB")
        print(f"Boş Bellek: {bellek_bilgisi['bos']:.2f} GB")
        # Bellek Uyarı Kontrolü
        if bellek_bilgisi['kullanilan'] / bellek_bilgisi['toplam'] > 0.8:  # Örnek eşik değeri
            uyari.uyari_ver("Bellek", 80, bellek_bilgisi['kullanilan'] / bellek_bilgisi['toplam'] * 100)
        
        # Disk Kullanımını izlemek için 
        disk_bilgisi = disk.disk_kullanimi_al("/")
        print(f"Toplam Disk: {disk_bilgisi['toplam']:.2f} GB")
        print(f"Kullanılan Disk: {disk_bilgisi['kullanilan']:.2f} GB")
        print(f"Boş Disk: {disk_bilgisi['bos']:.2f} GB")
        # Disk Uyarı Kontrolü
        if disk_bilgisi['kullanilan'] / disk_bilgisi['toplam'] > 0.8:  # Örnek eşik değeri
            uyari.uyari_ver("Disk", 80, disk_bilgisi['kullanilan'] / disk_bilgisi['toplam'] * 100)
        
        # Ağ bilgilerinin izlemek için
        ag_bilgisi = ag.ag_bilgisi_al()
        if ag_bilgisi:
            for arayuz_bilgisi in ag_bilgisi:  # Loop through the list of interfaces
                print(f"Ağ Arayüzü: {arayuz_bilgisi['arayuz']}")
                print(f" -Gönderilen Veri: {arayuz_bilgisi['gonderilen']:.2f} KB")
                print(f" -Alınan Veri: {arayuz_bilgisi['alinan']:.2f} KB")

            
        # Verileri Kaydetmek için (Örnek olarak CPU ve Bellek verilerini kaydet)
        veri = {
            "CPU Kullanımı": cpu_yuzdesi,
            "Kullanılan Bellek (GB)": bellek_bilgisi['kullanilan']
        }
        veri_kaydetme.verileri_kaydet(veri, "sistem_verileri.csv")
        
        gui.baslat()
        break  # GUI başlatıldıktan sonra döngüyü kır
        
        #time.sleep(1)  # time.sleep'e gerek yok, GUI kendi döngüsünde çalışacak


if __name__ == "__main__":
    main()