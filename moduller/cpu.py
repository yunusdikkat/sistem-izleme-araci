import psutil

def cpu_kullanimi_al():
    """CPU kullanım yüzdesini döndürmek için"""
    return psutil.cpu_percent(interval=1)
