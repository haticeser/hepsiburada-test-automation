# Jenkins Freestyle Job Kurulum Rehberi - Allure Reports

## 🎯 Amaç
Allure Reports'u doğru şekilde görüntülemek için freestyle job oluşturma rehberi. Raporun tüm bölümleri (Overview, Categories, Suites, Graphs, Timeline, Behaviors, Packages) dolu olacak.

## 📋 Adım Adım Kurulum

### 1. Yeni Freestyle Job Oluşturma
1. Jenkins ana sayfasında **"New Item"** tıklayın
2. **"Freestyle project"** seçin
3. Job adı: `hepsiburada_test_automation_freestyle`
4. **"OK"** tıklayın

### 2. Source Code Management Ayarları
1. **"Source Code Management"** bölümünde **"Git"** seçin
2. **Repository URL:** `https://github.com/haticeser/hepsiburada-test-automation.git`
3. **Branch Specifier:** `main`
4. **Credentials:** Gerekirse GitHub kimlik bilgilerinizi ekleyin

### 3. Build Steps Ayarları
**"Build Steps"** bölümünde **"Execute Windows batch command"** ekleyin:

#### Build Step 1: Environment Setup
```batch
@echo off
echo Python sürümü kontrol ediliyor...
python --version

echo Gerekli dizinler oluşturuluyor...
if not exist allure-results mkdir allure-results
if not exist reports mkdir reports
if not exist screenshots mkdir screenshots

echo Bağımlılıklar yükleniyor...
pip install -r requirements.txt
```

#### Build Step 2: Test Execution (ÖNEMLİ!)
```batch
@echo off
echo Testler çalıştırılıyor...
pytest tests/test_smoke.py -v --tb=short --alluredir=allure-results --html=reports/test_report.html --self-contained-html
```

**⚠️ ÖNEMLİ:** `--alluredir=allure-results` parametresi mutlaka olmalı!

#### Build Step 3: Allure Report Generation (ÖNEMLİ!)
```batch
@echo off
echo Allure raporu oluşturuluyor...
allure generate allure-results -o allure-report --clean
```

#### Build Step 4: Test Summary (Opsiyonel)
```batch
@echo off
echo Test özeti oluşturuluyor...
echo === TEST ÖZETİ === > test_summary.txt
echo Tarih: %date% %time% >> test_summary.txt
echo. >> test_summary.txt
echo === PYTEST SONUÇLARI === >> test_summary.txt
pytest --collect-only -q >> test_summary.txt 2>&1
echo Test özeti oluşturuldu: test_summary.txt
```

### 4. Post-build Actions Ayarları

#### 4.1 Allure Report (ANA ÖNEMLİ!)
1. **"Add post-build action"** > **"Allure Report"** seçin
2. **Results path:** `allure-results` (mutlaka bu olmalı!)
3. **Report path:** `allure-report` (opsiyonel)
4. **Keep results:** ✅ (işaretli bırakın)

#### 4.2 Publish HTML reports (Opsiyonel)
1. **"Add post-build action"** > **"Publish HTML reports"** seçin
2. **HTML directory to archive:** `reports`
3. **Index page[s]:** `test_report.html`
4. **Report title:** `Pytest HTML Report`
5. **Keep past HTML reports:** ✅

#### 4.3 Archive the artifacts
1. **"Add post-build action"** > **"Archive the artifacts"** seçin
2. **Files to archive:** `reports/*.html, test_summary.txt`

### 5. Job'ı Kaydetme ve Çalıştırma
1. **"Save"** tıklayın
2. **"Build Now"** tıklayarak job'ı çalıştırın
3. Build tamamlandıktan sonra sol menüde **"Allure Report"** linkini göreceksiniz

## 🔧 Gerekli Jenkins Plugin'leri

### Allure Reports Plugin
1. **Manage Jenkins** > **Manage Plugins**
2. **Available** sekmesinde **"Allure"** arayın
3. **"Allure Jenkins Plugin"**i yükleyin
4. Jenkins'i yeniden başlatın

### HTML Publisher Plugin (Opsiyonel)
1. **Manage Jenkins** > **Manage Plugins**
2. **Available** sekmesinde **"HTML Publisher"** arayın
3. **"HTML Publisher Plugin"**i yükleyin

## ✅ Beklenen Sonuç

Job çalıştıktan sonra:
- Sol menüde **"Allure Report"** linki görünecek
- Allure raporunda **TÜM BÖLÜMLER DOLU** olacak:
  - **Overview:** Test özeti ve genel bilgiler
  - **Categories:** Test kategorileri (smoke, regression, vb.)
  - **Suites:** Test suite'leri
  - **Graphs:** Test sonuç grafikleri
  - **Timeline:** Test çalışma zaman çizelgesi
  - **Behaviors:** Test davranışları ve adımları
  - **Packages:** Test paket yapısı

## 🐛 Sorun Giderme

### Allure Report görünmüyorsa:
1. **Results path**'in `allure-results` olduğundan emin olun
2. Allure Reports plugin'inin yüklü olduğunu kontrol edin
3. Build loglarında `pytest` komutunun `--alluredir=allure-results` parametresi ile çalıştığını kontrol edin

### Test sonuçları boşsa:
1. `pytest` komutunun `--alluredir=allure-results` parametresi ile çalıştığını kontrol edin
2. `allure-results` dizininde JSON dosyalarının oluştuğunu kontrol edin
3. Test dosyalarında `@allure` decorator'larının olduğunu kontrol edin

### Rapor bölümleri boşsa:
1. Test dosyalarında Allure annotation'ları olduğundan emin olun:
   ```python
   @allure.feature("Feature Name")
   @allure.story("Story Name")
   @allure.severity(allure.severity_level.CRITICAL)
   ```
2. `pytest.ini` dosyasında `--alluredir=allure-results` parametresinin olduğunu kontrol edin

## 📞 Destek

Sorun yaşarsanız:
1. Build loglarını kontrol edin
2. `allure-results` dizinindeki dosyaları kontrol edin
3. Jenkins plugin'lerinin güncel olduğundan emin olun
4. Test dosyalarında Allure annotation'larının doğru kullanıldığını kontrol edin

## 🎯 Başarı Kriterleri

✅ Job başarıyla çalışır
✅ Sol menüde "Allure Report" linki görünür
✅ Allure raporunda Overview bölümü dolu
✅ Allure raporunda Categories bölümü dolu
✅ Allure raporunda Suites bölümü dolu
✅ Allure raporunda Graphs bölümü dolu
✅ Allure raporunda Timeline bölümü dolu
✅ Allure raporunda Behaviors bölümü dolu
✅ Allure raporunda Packages bölümü dolu
