# Hepsiburada Test Automation

Bu proje, Hepsiburada web sitesi için kapsamlı test otomasyonu sağlar. Page Object Model (POM) deseni kullanılarak geliştirilmiş ve pytest framework'ü ile test edilmiştir.

## 🚀 Özellikler

- **Page Object Model (POM)**: Sürdürülebilir ve okunabilir test kodu
- **Selenium WebDriver**: Modern web otomasyonu
- **Pytest Framework**: Güçlü test framework'ü
- **HTML Raporlama**: Detaylı test raporları
- **Parallel Test Execution**: Hızlı test çalıştırma
- **Cross-browser Support**: Chrome, Firefox, Edge desteği
- **Responsive Testing**: Farklı ekran boyutlarında test
- **Error Handling**: Kapsamlı hata yönetimi

## 📁 Proje Yapısı

```
hepsiburada_tests/
├── pages/                          # Page Object Model sınıfları
│   ├── base_page.py               # Temel sayfa sınıfı
│   ├── hepsiburada_page.py        # Hepsiburada ana sayfa
│   ├── registration_page.py       # Kayıt sayfası
│   ├── login_page.py              # Giriş sayfası
│   ├── tempail_page.py            # Tempail email servisi
│   └── hepsiburada_automation.py  # Ana otomasyon sınıfı
├── tests/                          # Test dosyaları
│   ├── test_integration.py        # Entegrasyon testleri
│   ├── test_registration.py       # Kayıt testleri
│   ├── test_login.py              # Giriş testleri
│   └── test_tempail.py            # Tempail testleri
├── reports/                        # Test raporları
├── conftest.py                    # Pytest konfigürasyonu
├── pytest.ini                     # Pytest ayarları
├── requirements.txt                # Gerekli paketler
├── run_tests.py                   # Test çalıştırıcı
└── README.md                      # Bu dosya
```

## 🛠️ Kurulum

### Gereksinimler

- Python 3.8+
- Chrome WebDriver (otomatik yönetim)
- pip

### Kurulum Adımları

1. **Repository'yi klonlayın:**
   ```bash
   git clone <repository-url>
   cd hepsiburada_test_automation
   ```

2. **Virtual environment oluşturun:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # veya
   venv\Scripts\activate     # Windows
   ```

3. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r hepsiburada_tests/requirements.txt
   ```

4. **Chrome WebDriver'ı yükleyin:**
   ```bash
   # Otomatik yönetim (önerilen)
   pip install webdriver-manager
   ```

## 🧪 Test Çalıştırma

### İnteraktif Mod

```bash
cd hepsiburada_tests
python run_tests.py
```

### Komut Satırı Modu

```bash
# Tüm testleri çalıştır
python run_tests.py all

# Sadece entegrasyon testleri
python run_tests.py integration

# Sadece kayıt testleri
python run_tests.py registration

# Sadece giriş testleri
python run_tests.py login

# Sadece Tempail testleri
python run_tests.py tempail

# Verbose mod ile
python run_tests.py all -v

# Parallel mod ile
python run_tests.py all -p
```

### Pytest Direkt

```bash
# Tüm testler
pytest

# Belirli test dosyası
pytest tests/test_registration.py

# Belirli test sınıfı
pytest tests/test_registration.py::TestHepsiburadaRegistration

# Belirli test metodu
pytest tests/test_registration.py::TestHepsiburadaRegistration::test_registration_flow

# Verbose mod
pytest -v

# HTML rapor ile
pytest --html=reports/report.html --self-contained-html

# Parallel execution
pytest -n auto
```

## 📊 Test Türleri

### 1. Entegrasyon Testleri (`test_integration.py`)
- Tam üye kaydı otomasyonu
- Giriş otomasyonu
- Sayfa navigasyonu
- Form elementleri
- Popup kapatma

### 2. Kayıt Testleri (`test_registration.py`)
- Kayıt formu validasyonu
- Geçersiz email testleri
- Şifre gereksinimleri
- Doğrulama kodu formatı
- Kişisel bilgi formu

### 3. Giriş Testleri (`test_login.py`)
- Giriş formu elementleri
- Geçersiz kimlik bilgileri
- Doğrulama kodu formatı
- Başarı göstergeleri
- Responsive tasarım

### 4. Tempail Testleri (`test_tempail.py`)
- Email oluşturma
- Çoklu email testi
- Doğrulama kodu bekleme
- Sayfa elementleri
- Performans testleri

## 🔧 Konfigürasyon

### Pytest Ayarları (`pytest.ini`)

```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --tb=short
    --strict-markers
    --disable-warnings
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    smoke: marks tests as smoke tests
```

### Test Fixtures (`conftest.py`)

- `driver`: WebDriver instance
- `wait`: WebDriverWait instance
- `test_credentials`: Test kimlik bilgileri

## 📈 Raporlama

### HTML Raporlar
- Otomatik rapor oluşturma
- Test sonuçları
- Hata detayları
- Screenshot'lar
- Zaman bilgileri

### Rapor Konumu
```
reports/
└── test_report_YYYYMMDD_HHMMSS.html
```

## 🚨 Hata Yönetimi

### Yaygın Hatalar

1. **WebDriver Hatası**
   - Chrome WebDriver'ın güncel olduğundan emin olun
   - `webdriver-manager` kullanarak otomatik yönetim

2. **Element Bulunamadı**
   - Sayfa yüklenme süresini artırın
   - Selector'ları güncelleyin
   - Explicit wait kullanın

3. **Timeout Hatası**
   - `conftest.py`'de timeout değerlerini artırın
   - Ağ bağlantısını kontrol edin

### Debug Modu

```bash
# Verbose mod ile çalıştır
pytest -v -s

# Belirli testi debug et
pytest tests/test_registration.py::test_registration_flow -v -s
```

## 🔄 CI/CD Entegrasyonu

### GitHub Actions

```yaml
name: Test Automation
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        pip install -r hepsiburada_tests/requirements.txt
    - name: Run tests
      run: |
        cd hepsiburada_tests
        pytest --html=reports/report.html
```

## 📝 Geliştirme

### Yeni Test Ekleme

1. **Test dosyası oluşturun:**
   ```python
   # tests/test_new_feature.py
   import pytest
   from pages.hepsiburada_automation import HepsiburadaAutomation
   
   class TestNewFeature:
       def test_new_functionality(self, driver):
           automation = HepsiburadaAutomation(driver)
           # Test kodunuz
   ```

2. **Page Object ekleyin:**
   ```python
   # pages/new_page.py
   from .base_page import BasePage
   
   class NewPage(BasePage):
       def new_method(self):
           # Sayfa metodu
   ```

### Kod Standartları

- PEP 8 uyumlu
- Docstring'ler zorunlu
- Type hints kullanın
- Error handling ekleyin

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
- **Proje Linki**: https://github.com/haticeser/hepsiburada-test-automation

## 🙏 Teşekkürler

- Selenium WebDriver ekibi
- Pytest geliştiricileri
- Page Object Model topluluğu

---

**Not**: Bu proje eğitim amaçlı geliştirilmiştir. Gerçek web sitelerinde test yaparken site kullanım şartlarını göz önünde bulundurun.
