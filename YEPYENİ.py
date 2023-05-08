import numpy as np

def fibonacci_ratios():
    # Fibonacci oranlarının hesaplanması
    ratios = [0.236, 0.382, 0.5, 0.618, 0.786, 1.0, 1.236, 1.382, 1.618]
    return ratios

def find_previous_extrema(prices):
    # Önceki tepe ve taban noktalarını bulma
    extrema = []
    for i in range(1, len(prices)-1):
        if prices[i] > prices[i-1] and prices[i] > prices[i+1]:  # Tepe noktası
            extrema.append(('tepe', i, prices[i]))
        elif prices[i] < prices[i-1] and prices[i] < prices[i+1]:  # Taban noktası
            extrema.append(('taban', i, prices[i]))
    return extrema

def calculate_fibonacci_levels(tepe_noktasi, taban_noktasi):
    # Fibonacci oranları ve tahmin edilen tepe-taban noktalarının hesaplanması
    fibonacci_levels = []
    ratios = fibonacci_ratios()
    difference = tepe_noktasi - taban_noktasi
    for ratio in ratios:
        level = tepe_noktasi - (ratio * difference)
        fibonacci_levels.append(level)
    return fibonacci_levels

def moving_average_prediction():
    # Verilerin alınması
    prices = [562381.70, 578751.83, 562262.43, 576496.41, 349624935545, 11148335517922]
    
    # Önceki tepe ve taban noktalarını kullanıcıdan alma
    tepe_noktasi = float(input("Önceki tepe noktasını girin: "))
    taban_noktasi = float(input("Önceki taban noktasını girin: "))
    
    # Fibonacci seviyelerini hesaplayarak tahmin edilen tepe ve taban noktalarını bulma
    fibonacci_levels = calculate_fibonacci_levels(tepe_noktasi, taban_noktasi)
    tahmin_edilen_tepe = fibonacci_levels[5]
    tahmin_edilen_taban = fibonacci_levels[0]
    
    return tahmin_edilen_tepe, tahmin_edilen_taban

# Tahmini sonuçları alıp ekrana yazdırma
tahmini_tepe, tahmini_taban = moving_average_prediction()
if tahmini_tepe is not None and tahmini_taban is not None:
    print("Tahmini Tepe Noktası:", tahmini_tepe)
    print("Tahmini Taban Noktası:", tahmini_taban)

