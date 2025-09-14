# Hepsiburada Test Automation - Jenkins Integration

Bu klasör Jenkins CI/CD pipeline'ı için hazırlanmış pytest test dosyalarını içerir.

## 📁 Test Yapısı

```
tests/
├── conftest.py          # Pytest konfigürasyonu ve fixture'lar
├── test_smoke.py        # Smoke testler (temel işlevsellik)
├── test_regression.py   # Regression testler (tam işlevsellik)
├── test_login.py        # Giriş işlemleri testleri
├── test_product.py      # Ürün işlemleri testleri
├── test_cart.py         # Sepet işlemleri testleri
├── test_checkout.py     # Ödeme işlemleri testleri
└── README.md           # Bu dosya
```

## 🏷️ Test Kategorileri

### Smoke Tests (`test_smoke.py`)
- **Amaç**: Temel işlevsellik testleri
- **Süre**: Hızlı (1-2 dakika)
- **Kapsam**: Kritik işlevler
- **Markers**: `@pytest.mark.smoke`

### Regression Tests (`test_regression.py`)
- **Amaç**: Tam işlevsellik testleri
- **Süre**: Uzun (5-10 dakika)
- **Kapsam**: Tüm işlevler
- **Markers**: `@pytest.mark.regression`, `@pytest.mark.slow`

### Feature Tests
- **Login Tests** (`test_login.py`): Giriş işlemleri
- **Product Tests** (`test_product.py`): Ürün işlemleri
- **Cart Tests** (`test_cart.py`): Sepet işlemleri
- **Checkout Tests** (`test_checkout.py`): Ödeme işlemleri

## 🚀 Çalıştırma

### Lokal Çalıştırma
```bash
# Tüm testler
pytest tests/

# Sadece smoke testler
pytest tests/test_smoke.py

# Sadece regression testler
pytest tests/test_regression.py

# Belirli marker ile
pytest -m smoke
pytest -m regression
pytest -m slow
```

### Jenkins'te Çalıştırma
Jenkins pipeline otomatik olarak tüm testleri paralel olarak çalıştırır.

## 📊 Raporlama

### Allure Raporu
```bash
# Allure raporu oluştur
pytest --alluredir=allure-results
allure serve allure-results
```

### HTML Raporu
```bash
# HTML raporu oluştur
pytest --html=reports/report.html --self-contained-html
```

## ⚙️ Konfigürasyon

### pytest.ini
- Test discovery ayarları
- Marker tanımları
- Raporlama ayarları
- Timeout ayarları

### conftest.py
- WebDriver fixture'ları
- Test logger'ları
- Allure environment bilgileri
- Screenshot capture on failure

## 🔧 Jenkins Pipeline

### Aşamalar
1. **Checkout**: Repository'yi al
2. **Environment Setup**: Python ortamını hazırla
3. **Dependencies Install**: Bağımlılıkları yükle
4. **Test Execution**: Testleri paralel çalıştır
5. **Allure Report Generation**: Rapor oluştur
6. **Test Summary**: Özet oluştur

### Raporlar
- Allure raporu (interaktif)
- HTML raporları (her kategori için)
- Screenshot'lar (hata durumunda)
- Test özeti

## 📧 Bildirimler

### Başarılı Build
- Email bildirimi gönderilir
- Rapor linkleri dahil edilir

### Başarısız Build
- Email bildirimi gönderilir
- Hata detayları dahil edilir
- Log linkleri dahil edilir

## 🐛 Hata Ayıklama

### Screenshot'lar
Test başarısız olduğunda otomatik screenshot alınır:
- Konum: `screenshots/`
- Format: `failure_{test_name}_{timestamp}.png`

### Loglar
- Test logları console'da görünür
- Jenkins build loglarında detaylı bilgi

### Rerun
- Başarısız testler otomatik olarak 1 kez tekrar çalıştırılır
- Rerun delay: 2 saniye

## 📝 Notlar

- Tüm testler `HepsiburadaAutomation` sınıfını kullanır
- WebDriver otomatik olarak yönetilir
- Testler arasında driver paylaşılır (session scope)
- Her test için ayrı logger kullanılır
- Allure raporlama otomatik olarak yapılır
