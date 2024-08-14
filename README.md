# Yavas Kaplumbagalar YetGen Core Python Bitirme Projesi
Bu repo YetGen Core - Python eğitim programı bitirme projesi için açılmıştır.

# Pembe Hava Durumu Uygulaması

Bu, kullanıcıların herhangi bir şehrin güncel hava durumunu kontrol edebileceği basit bir hava durumu uygulamasıdır. Uygulama, OpenWeatherMap API'sinden sıcaklık ve hava durumu açıklaması verilerini alır. Kullanıcı arayüzü, `tkinter` kütüphanesi kullanılarak açık pembe bir tema ile tasarlanmıştır.

## Özellikler

- Şehir adını girerek mevcut hava durumu bilgilerini alın.
- Sıcaklık (Celsius cinsinden) ve kısa bir hava durumu açıklaması gösterilir.
- Hava durumunu kontrol etmek için basit bir grafik arayüz (GUI).

## Gereksinimler

Uygulamayı çalıştırmadan önce aşağıdaki gereksinimlerin yüklü olduğundan emin olun:

- Python 3.x
- `tkinter` (Python kurulumları ile genellikle birlikte gelir)
- `requests` kütüphanesi: Şu komutu kullanarak yükleyebilirsiniz:
  ```
  pip install requests
  ```

## Kurulum

1. Bu projeyi indirin veya klonlayın.
2. Gerekli kütüphanelerin (`tkinter` ve `requests`) yüklü olduğundan emin olun.

## Uygulamanın Çalıştırılması

1. Terminal veya komut istemcisini açın.
2. Python dosyasını çalıştırın:
   ```bash
   python pinkweatherapp.py
   ```
3. Bir GUI penceresi açılacaktır. Hava durumunu kontrol etmek istediğiniz şehrin adını girin ve ardından "Hava Durumunu Göster" butonuna tıklayarak sonuçları görüntüleyin.

## Nasıl Çalışır?

1. Kullanıcı, giriş alanına bir şehir adı girer.
2. Uygulama, OpenWeatherMap API'sine bir istek göndererek o şehir için hava durumu verilerini alır.
3. Şehir adı geçerli ve veri başarıyla alındıysa, uygulama hava durumu açıklamasını ve sıcaklığı gösterir.
4. Eğer bir hata olursa (örneğin geçersiz şehir adı veya ağ problemi), uygulama uygun bir uyarı mesajı gösterir.

## Örnek

[Ekran görüntüsü 2024-08-14 214159](https://github.com/user-attachments/assets/fae8ae09-479c-4cff-95be-1454d44e2765)

## API Anahtarı

Bu uygulama OpenWeatherMap API'sini kullanmaktadır. Uygulamayı çalıştırabilmek için bir API anahtarına ihtiyacınız olacak. Kodun içindeki API anahtarı kısmına (şu anda `dcbe55c1e3134568a5824acb8fc1ca1a` olan kısım) kendi API anahtarınızı eklemeniz gerekmektedir. API anahtarınızı almak için [OpenWeatherMap](https://openweathermap.org/) sitesine kaydolabilirsiniz.

Herhangi bir ekleme veya değişiklik yapmak isterseniz, bana bildirin!
