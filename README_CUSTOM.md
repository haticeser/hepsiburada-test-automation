# Hepsiburada Test Otomasyonu - Özel Script

Bu script, tests klasörü olmadan çalıştırılabilir versiyondur.

## 🚀 Hızlı Başlangıç

### 1. Gereksinimler
```bash
pip install -r requirements.txt
```

### 2. Çalıştırma Yöntemleri

#### A) İnteraktif Menü (Önerilen)
```bash
python custom_automation.py
```

#### B) Komut Satırından Hızlı Çalıştırma
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

## 📋 Mevcut Test Senaryoları

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

- ✅ Tests klasörü olmadan çalışır
- ✅ İnteraktif menü sistemi
- ✅ Komut satırı desteği
- ✅ Detaylı log çıktıları
- ✅ Hata yönetimi
- ✅ Otomatik WebDriver kurulumu
- ✅ Çoklu test senaryosu

## 📁 Dosya Yapısı

```
hepsiburada_test_automation/
├── custom_automation.py      # İnteraktif menü scripti
├── run_automation.py         # Hızlı çalıştırma scripti
├── pages/                    # Ana otomasyon sınıfları
│   ├── hepsiburada_automation.py
│   ├── hepsiburada_page.py
│   ├── tempail_page.py
│   ├── registration_page.py
│   ├── login_page.py
│   └── base_page.py
├── conftest.py              # Pytest konfigürasyonu
├── requirements.txt         # Gerekli kütüphaneler
└── README_CUSTOM.md         # Bu dosya
```

## 🎯 Kullanım Örnekleri

### Örnek 1: Tam Otomasyon
```bash
python run_automation.py full
```

### Örnek 2: İnteraktif Menü
```bash
python custom_automation.py
# Menüden seçim yapın
```

### Örnek 3: Sadece Üye Kaydı
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
