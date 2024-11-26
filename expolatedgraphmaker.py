import matplotlib.pyplot as plt
import numpy as np

# Veriler
a = np.array([1.86, 2.06, 2.25, 2.45]) # X ekseni için m (gram) değerleri

# Y ekseni için Fg (Newton) değerleri
Fa = np.array([0.19, 0.210, 0.230, 0.250])  # a yerine belirtilen yeni değerler

# Doğrudan orijinden geçen bir doğru için eğimi hesapla (regresyon, intercept = 0)
slope = np.dot(Fa, a) / np.dot(Fa, Fa)  # Linear fit with intercept forced to 0

# Extrapolation için daha geniş bir x aralığı oluşturma
Fa_genisletilmis = np.linspace(Fa.min(), Fa.max(), 100)  # Fa değer aralığında daha fazla x değeri
a_dogru_genisletilmis = slope * Fa_genisletilmis  # Regresyon doğrusunu genişletilmiş x değerlerine uygulama

# Grafik oluşturma
plt.figure(figsize=(10, 5))

# Ölçülen noktaları çizme
plt.scatter(Fa, a, color='g', label='Measured Values')

# Extrapolated doğruyu çizme
plt.plot(Fa_genisletilmis, a_dogru_genisletilmis, linestyle='-', color='b', label='Fitted line (y = {:.6f}x)'.format(slope))

# X ekseninde yalnızca Fa değerlerini gösterme
plt.xticks(Fa)  # Sadece Fa değerlerini işaretle

# (0, 0)'dan geçen çizgiyi çizme
plt.plot([0, Fa.max()], [0, slope * Fa.max()], 'g--', label='Line through (0, 0)')

# X ve Y eksenlerinin sınırlarını manuel olarak ayarlama
plt.xlim([Fa.min() - 0.01, Fa.max() + 0.01])  # X eksenini biraz genişlet
plt.ylim([1.7, 2.3])  # Y eksenini uygun bir aralıkla sınırlama

# Başlık ve etiketler
plt.title("Gravitational Force VS Mass")
plt.xlabel("Mass (kg)")
plt.ylabel("Gravitational Force (N)")

# Legend ve grid ekleme
plt.legend()
plt.grid(True)

# Grafiği göster
plt.show()