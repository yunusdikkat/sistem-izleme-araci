import psutil
def disk_kullanimi_al(disk_yolu):
    "Disk kullanımı bilgilerini döndürür."
    disk = psutil.disk_usage(disk_yolu)
    return {
        "toplam": disk.total / (1024 ** 3),
        "kullanilan": disk.used / (1024 ** 3),
        "bos": disk.free / (1024 ** 3)
    }