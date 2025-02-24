import csv
def verileri_kaydet(veri, dosya_adi):
    with open(dosya_adi, "w", newline="") as dosya:
        yazici = csv.writer(dosya)
        yazici.writerow(veri.keys())
        yazici.writerow(veri.values())
        