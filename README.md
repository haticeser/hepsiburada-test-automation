# Hepsiburada Test Automation

Bu proje, Hepsiburada web sitesi için kapsamlı test otomasyonu sağlar. Page Object Model (POM) deseni kullanılarak geliştirilmiş ve **tests klasörü olmadan** çalıştırılabilir basit scriptler ile kullanılabilir.

## 🚀 Özellikler

- **Page Object Model (POM)**: Sürdürülebilir ve okunabilir test kodu
- **Selenium WebDriver**: Modern web otomasyonu
- **Basit Çalıştırma**: Tests klasörü olmadan çalışır
- **İnteraktif Menü**: Kolay kullanım için menü sistemi
- **Komut Satırı Desteği**: Hızlı çalıştırma için CLI
- **Otomatik WebDriver**: ChromeDriver otomatik indirme
- **Error Handling**: Kapsamlı hata yönetimi
- **Ürün Seçimi Otomasyonu**: Elektronik menüsünden ürün kategorisi seçimi
- **Tempail Entegrasyonu**: Geçici email ile üye kaydı

## 📁 Proje Yapısı

```
hepsiburada_test_automation/
├── custom_automation.py            # ✅ İnteraktif menü scripti
├── run_automation.py               # ✅ Hızlı komut satırı scripti
├── pages/                          # Page Object Model sınıfları
│   ├── base_page.py               # Temel sayfa sınıfı
│   ├── hepsiburada_page.py        # Hepsiburada ana sayfa
│   ├── registration_page.py       # Kayıt sayfası
│   ├── login_page.py              # Giriş sayfası
│   ├── tempail_page.py            # Tempail email servisi
│   └── hepsiburada_automation.py  # Ana otomasyon sınıfı
├── reports/                        # Test raporları (opsiyonel)
├── conftest.py                    # WebDriver konfigürasyonu
├── requirements.txt                # Gerekli paketler
├── README.md                      # Bu dosya
└── README_CUSTOM.md               # Detaylı kullanım kılavuzu
```

## 🛠️ Kurulum

### Gereksinimler

- Python 3.8+
- Chrome Browser
- pip

### Hızlı Kurulum

1. **Repository'yi klonlayın:**
   ```bash
   git clone <repository-url>
   cd hepsiburada_test_automation
   ```

2. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Hazır! Artık çalıştırabilirsiniz:**
   ```bash
   python custom_automation.py
   ```

### Chrome WebDriver
ChromeDriver otomatik olarak indirilir ve yönetilir. Manuel kurulum gerekmez.

## 🧪 Test Çalıştırma

### 🎯 İnteraktif Menü (Önerilen)

```bash
python custom_automation.py
```

Menüden istediğiniz testi seçin:
- 🚀 Tam Otomasyon (Üyelik + Ürün Seçimi)
- 📝 Sadece Üye Kaydı
- 🔑 Sadece Giriş Testi
- 🛍️ Sadece Ürün Seçimi
- 🎯 Filtreli Ürün Seçimi (Lenovo + Intel Core i7)
- 📧 Sadece Tempail Email Testi

### ⚡ Hızlı Komut Satırı

```bash
# Tam otomasyon (Üyelik + Ürün Seçimi)
python run_automation.py full

# Sadece üye kaydı
python run_automation.py register

# Sadece giriş testi
python run_automation.py login

# Sadece ürün seçimi
python run_automation.py product

# Filtreli ürün seçimi (Lenovo + Intel Core i7)
python run_automation.py filtered

# Sadece Tempail email testi
python run_automation.py tempail

# İnteraktif menü
python run_automation.py menu
```

## 🎯 Test Senaryoları

### 1. 🚀 Tam Otomasyon
- Tempail'den geçici email alır
- Hepsiburada'da üye kaydı yapar
- Doğrulama kodunu bekler ve girer
- Dizüstü bilgisayar kategorisine gider
- Lenovo + Intel Core i7 filtresi uygular
- İlk filtrelenmiş ürünü seçer

### 2. 📝 Sadece Üye Kaydı
- Tempail'den email alır
- Hepsiburada'da üye kaydı formunu doldurur
- Doğrulama kodunu bekler ve girer
- Kişisel bilgileri doldurur
- Üye kaydını tamamlar

### 3. 🔑 Sadece Giriş Testi
- Tempail'den email alır
- Hepsiburada'ya giriş yapar
- Doğrulama kodunu bekler ve girer

### 4. 🛍️ Sadece Ürün Seçimi
- Hepsiburada ana sayfasına gider
- Dizüstü bilgisayar kategorisine gider

### 5. 🎯 Filtreli Ürün Seçimi
- Dizüstü bilgisayar kategorisine gider
- Lenovo marka filtresi uygular
- Intel Core i7 işlemci filtresi uygular
- İlk filtrelenmiş ürünü seçer

### 6. 📧 Sadece Tempail Email Testi
- Tempail.com'a gider
- Geçici email alır
- Email formatını kontrol eder

## 🔧 Özellikler

### ✅ Avantajlar
- **Tests klasörü gerekmez** - Sadece `pages/` klasörü yeterli
- **İnteraktif menü** - Kolay kullanım
- **Komut satırı desteği** - Hızlı çalıştırma
- **Detaylı loglar** - Her adımı takip edebilirsiniz
- **Hata yönetimi** - Güvenli çalışma
- **Otomatik WebDriver** - ChromeDriver otomatik indirilir

### 🎯 Kullanım Örnekleri

**İlk kez çalıştırıyorsanız:**
```bash
python custom_automation.py
# Menüden "1" seçerek tam otomasyonu deneyin
```

**Hızlı test için:**
```bash
python run_automation.py tempail
# Sadece Tempail email testini çalıştırın
```

**Üye kaydı testi için:**
```bash
python run_automation.py register
```

## ⚠️ Önemli Notlar

1. **Chrome Browser Gerekli**: Script Chrome browser kullanır
2. **İnternet Bağlantısı**: Tempail ve Hepsiburada'ya erişim gerekli
3. **Doğrulama Kodu**: Email doğrulama kodları manuel olarak beklenir
4. **Timeout**: Bazı işlemler 120 saniye timeout ile çalışır

## 🐛 Sorun Giderme

### WebDriver Hatası
```bash
# WebDriver Manager otomatik olarak ChromeDriver indirir
# Eğer hata alırsanız, Chrome browser'ın güncel olduğundan emin olun
```

### Import Hatası
```bash
# Pages modüllerinin doğru konumda olduğundan emin olun
# Script'i proje ana dizininden çalıştırın
```

### Email Alamama
```bash
# Tempail.com erişilebilir olduğundan emin olun
# İnternet bağlantınızı kontrol edin
```

## 📞 Destek

Herhangi bir sorun yaşarsanız:
1. Hata mesajını kontrol edin
2. İnternet bağlantınızı kontrol edin
3. Chrome browser'ın güncel olduğundan emin olun
4. Script'i proje ana dizininden çalıştırdığınızdan emin olun

## 📝 Geliştirme

### Yeni Özellik Ekleme

1. **Yeni sayfa sınıfı ekleyin:**
   ```python
   # pages/new_page.py
   from .base_page import BasePage
   
   class NewPage(BasePage):
       def new_method(self):
           # Sayfa metodu
   ```

2. **Ana otomasyon sınıfına entegre edin:**
   ```python
   # pages/hepsiburada_automation.py
   from .new_page import NewPage
   
   class HepsiburadaAutomation:
       def __init__(self, driver):
           self.new_page = NewPage(driver)
   ```

### Kod Standartları

- PEP 8 uyumlu
- Docstring'ler zorunlu
- Error handling ekleyin
- Detaylı log çıktıları

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 📞 İletişim

- **Proje Sahibi**: haticeser
- **Email**: haticeser@example.com
- **Proje Linki**: https://github.com/haticeser/hepsiburada-test-automation-last

## 🙏 Teşekkürler

- Selenium WebDriver ekibi
- Page Object Model topluluğu
- Tempail.com servisi

---

**Not**: Bu proje eğitim amaçlı geliştirilmiştir. Gerçek web sitelerinde test yaparken site kullanım şartlarını göz önünde bulundurun.

## 📚 Ek Kaynaklar

- [README_CUSTOM.md](README_CUSTOM.md) - Detaylı kullanım kılavuzu
- [requirements.txt](requirements.txt) - Gerekli kütüphaneler
- [custom_automation.py](custom_automation.py) - İnteraktif menü scripti
- [run_automation.py](run_automation.py) - Hızlı çalıştırma scripti
