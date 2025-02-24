import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def grafik_olustur(pencere, veriler, baslik, x_etiketi, y_etiketi, grafik_alani):
    """Grafiği oluşturur ve pencereye ekler."""

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(veriler)
    ax.set_title(baslik)
    ax.set_xlabel(x_etiketi)
    ax.set_ylabel(y_etiketi)

    canvas = FigureCanvasTkAgg(fig, master=grafik_alani)
    canvas.draw()
    canvas.get_tk_widget().pack()