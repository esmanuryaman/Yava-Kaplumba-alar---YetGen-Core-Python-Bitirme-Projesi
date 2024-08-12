import requests
import os
from PIL import Image

apiKey = "dcbe55c1e3134568a5824acb8fc1ca1a"
baseUrl = "http://api.openweathermap.org/data/2.5/"

# Görsel dosyalarının yolu
gorselYolu = {
    'clear sky': 'gunesli.png',
    'few clouds': 'bulutlu.png',
    'broken clouds': 'brokenclouds.png',
    'shower rain': 'showerrain.png',
    'rain': 'yagmurlu.png',
    'thunderstorm': 'firtinali.png',
    'snow': 'karli.png',
    'mist': 'sisli.png'
}

class HavaDurumuAlici:
    def __init__(self, apiKey):
        self.apiKey = apiKey

    def havaDurumuGetir(self, sehir):
        try:
            url = f"{baseUrl}weather?q={sehir}&appid={self.apiKey}&units=metric"
            cevap = requests.get(url)
            veri = cevap.json()

            if cevap.status_code == 200:
                return veri
            else:
                print(f"{sehir} şehri bulunamadı veya başka bir hata oluştu. Durum kodu: {cevap.status_code}.")
                return None
        except Exception as e:
            print(f"Hata: {e}")
            return None

    def tahminGetir(self, sehir):
        try:
            url = f"{baseUrl}forecast?q={sehir}&appid={self.apiKey}&units=metric"
            cevap = requests.get(url)
            veri = cevap.json()

            if cevap.status_code == 200:
                return veri
            else:
                print(f"{sehir} şehri bulunamadı veya başka bir hata oluştu. Durum kodu: {cevap.status_code}.")
                return None
        except Exception as e:
            print(f"Hata: {e}")
            return None

    def havaDurumuBilgileriniYazdir(self, sehir):
        havaDurumuVerisi = self.havaDurumuGetir(sehir)

        if havaDurumuVerisi:
            print(f"\n{sehir} için hava durumu:")
            print(f"Sıcaklık: {havaDurumuVerisi['main']['temp']}°C")
            print(f"Hissedilen Sıcaklık: {havaDurumuVerisi['main']['feels_like']}°C")
            print(f"Nem: {havaDurumuVerisi['main']['humidity']}%")
            print(f"Rüzgar Hızı: {havaDurumuVerisi['wind']['speed']} m/s")
            print(f"Rüzgar Yönü: {havaDurumuVerisi['wind']['deg']}°")

            if 'weather' in havaDurumuVerisi and len(havaDurumuVerisi['weather']) > 0:
                aciklama = havaDurumuVerisi['weather'][0]['description']
                print(f"Hava Durumu: {aciklama.capitalize()}")

                # Görseli göstermek için metot çağır
                self.gorselGoster(aciklama)
            else:
                print("Hava durumu bilgisi bulunamadı.")
    
    def farkliZamanDilimlerindeHavaDurumu(self, sehir):
        tahminVerisi = self.tahminGetir(sehir)
        if tahminVerisi:
            print(f"\n{sehir} için farklı zaman dilimlerinde hava durumu:")
            for giris in tahminVerisi['list']:
                tarih = giris['dt_txt']
                sicaklik = giris['main']['temp']
                aciklama = giris['weather'][0]['description']
                print(f"Tarih: {tarih} - Sıcaklık: {sicaklik}°C - Hava Durumu: {aciklama.capitalize()}")

    def gorselGoster(self, aciklama):
        # Görsel dosyasını belirle
        gorselAdi = gorselYolu.get(aciklama.lower(), 'default.png')
        
        # Görsel yolunu oluştur
        gorselYoluTam = os.path.join('images', gorselAdi)
        
        # Dosya var mı kontrol et
        if os.path.exists(gorselYoluTam):
            try:
                # Görseli yükle
                img = Image.open(gorselYoluTam)
                img.show()
            except Exception as e:
                print(f"Görsel yüklenirken başka bir hata oluştu: {e}")
        else:
            print(f"Görsel yüklenirken hata oluştu: {gorselYoluTam} dosyası bulunamadı.")

def ana():
    print("Hava Durumu Uygulamasına Hoşgeldiniz!")
    print("Bu program, girdiğiniz şehir için hava durumu bilgilerini, farklı zaman dilimlerinde hava durumunu ve hava durumu uyarılarını sağlar.")
    print("Programdan çıkmak için 'çık' yazabilirsiniz.\n")
    
    alici = HavaDurumuAlici(apiKey)
    
    while True:
        sehir = input("Şehir adını girin (çıkmak için 'çık' yazın): ").strip()
        if sehir.lower() == 'çık':
            print("Programdan çıkılıyor...")
            break
        if not sehir:
            print("Geçersiz şehir adı, lütfen tekrar deneyin.")
            continue

        alici.havaDurumuBilgileriniYazdir(sehir)
        alici.farkliZamanDilimlerindeHavaDurumu(sehir)

if __name__ == "__main__":
    ana()