import tkinter as tk
import requests

class HavaDurumuUygulamasi:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Hava Durumu")
        self.pencere.geometry("600x200")  # Pencerenin boyutunu 600x200 yap

        # Pencere arka plan rengini açık pembe yap
        self.pencere.configure(bg="#FFC0CB")

        # Şehir adı girmek için bir etiket ve giriş kutusu
        self.etiket = tk.Label(pencere, text="Şehir Adı:", font=("Times New Roman", 14), bg="#FFC0CB")
        self.etiket.pack(pady=10)

        self.sehirGirisi = tk.Entry(pencere, font=("Times New Roman", 14))
        self.sehirGirisi.pack(pady=10)

        # Hava durumunu gösteren buton
        self.buton = tk.Button(pencere, text="Hava Durumunu Göster", command=self.havaDurumunuGoster, font=("Times New Roman", 14), bg="purple", fg="white")
        self.buton.pack(pady=10)

        # Sonuçları göstermek için bir etiket
        self.sonucEtiketi = tk.Label(pencere, text="", font=("Times New Roman", 14), bg="#FFC0CB")
        self.sonucEtiketi.pack(pady=10)

    def havaDurumunuGoster(self):
        sehir = self.sehirGirisi.get()
        
        # Eğer şehir adı boşsa, bir uyarı göster
        if sehir == "":
            self.sonucEtiketi.config(text="Lütfen bir şehir adı girin!")
            return

        try:
            # Hava durumu verilerini getiriyoruz
            havaDurumu = self.havaDurumunuGetir(sehir)
            if havaDurumu:
                # İlk harfi büyük yapma işlemi
                description = havaDurumu['description'].capitalize()
                self.sonucEtiketi.config(text=f"{sehir} için Hava Durumu: {description}, Sıcaklık: {havaDurumu['temp']}°C")
            else:
                self.sonucEtiketi.config(text="Hava durumu bilgisi alınamadı!")
        except:
            self.sonucEtiketi.config(text="Bir hata oluştu!")

    def havaDurumunuGetir(self, sehir):
        apiAnahtari = "dcbe55c1e3134568a5824acb8fc1ca1a"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&units=metric&appid={apiAnahtari}&lang=tr"

        yanit = requests.get(url)
        if yanit.status_code == 200:
            veri = yanit.json()
            havaDurumu = {
                "description": veri["weather"][0]["description"],
                "temp": veri["main"]["temp"]
            }
            return havaDurumu
        else:
            return None

# Uygulamanın çalışması için gereken kod
pencere = tk.Tk()
uygulama = HavaDurumuUygulamasi(pencere)
pencere.mainloop()