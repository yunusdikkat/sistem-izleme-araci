import psutil
def bellek_kullanimi_al():
    "Bellek kullanımlarını döndürmek için"
    bellek = psutil.virtual_memory()
    return {
        "toplam": bellek.total / (1024 ** 3), #GB
        "kullanilan": bellek.used / (1024 ** 3), 
        "bos": bellek.available / (1024 ** 3)
    }
    