import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def exponential_decay(x, a, b):
    """
    Üstel azalma fonksiyonu.
    """
    return a * np.exp(-b * x)

def ivme_kütle_grafik(ivme_degerleri, kütle_degerleri):
    """
    İvme ve kütle verilerini kullanarak ortalama bir üstel azalma trendi oluşturan grafik.
    """
    # Üstel azalma eğrisi için uygun parametreleri bul
    popt, _ = curve_fit(exponential_decay, kütle_degerleri, ivme_degerleri)
    
    # Daha geniş bir x ekseni aralığında eğri oluşturmak için yeni bir x dizisi
    x_genis = np.linspace(min(kütle_degerleri) * 0.8, max(kütle_degerleri) * 1.2, 100)
    trend_ivme = exponential_decay(x_genis, *popt)
    
    # Grafik çizimi
    plt.plot(kütle_degerleri, ivme_degerleri, 'o', label='Veri Noktaları', color='blue')
    plt.plot(x_genis, trend_ivme, '--', color='red', label='Üstel Trend Çizgisi')
    
    # Grafik başlık ve açıklamaları
    plt.title('Average Velocity Versus Total Mass')
    plt.xlabel('Total Mass (kg)')
    plt.ylabel('Average Velocity (m/s^2)')
    plt.legend()
    plt.grid(True)
    
    # X ve Y eksen sınırlarını ayarlama (yakınlaştırma)
    plt.xlim(0.2, 0.3)  # Daha geniş bir x sınırı
    plt.ylim(6, 10)     # Y eksenini de genişleterek eğrinin tam görünmesini sağlıyoruz
    
    plt.show()

# Örnek ivme ve kütle değerleri
ivme_degerleri = [9.668, 8.865, 8.132, 7.545]  # İvme değerleri (m/s^2)
kütle_degerleri = [0.220, 0.240, 0.260, 0.280]  # Kütle değerleri (kg)

# Fonksiyonu çağırarak grafik oluşturma
ivme_kütle_grafik(ivme_degerleri, kütle_degerleri)