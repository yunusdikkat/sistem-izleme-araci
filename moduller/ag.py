import psutil

def ag_bilgisi_al():
    "Ağ arayüzleri hakkında bilgileri döndürmek için"
    ag_arayuzleri = psutil.net_if_addrs()
    ag_io = psutil.net_io_counters(pernic=True)
    bilgiler = []
    for arayuz, detaylar in ag_arayuzleri.items():
        if arayuz in ag_io:  # Arayüz bilgisi mevcutsa
            io_counters = ag_io[arayuz]
            if detaylar:
                bilgiler.append({
                    "arayuz": arayuz,
                    "gonderilen": io_counters.bytes_sent / (1024),
                    "alinan": io_counters.bytes_recv / (1024)  # KB CİNSİNDEN
                })
    return bilgiler