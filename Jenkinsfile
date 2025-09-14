# ========================================
# HEPBİRADURA TEST AUTOMATION - JENKINS SETUP
# ========================================
# Bu dosya Jenkins freestyle job kurulumu için hazırlanmıştır
# Pipeline job yerine freestyle job kullanın

# ========================================
# 1. BUILD STEPS (Jenkins'te Execute Windows batch command olarak ekleyin)
# ========================================

# Build Step 1: Environment Setup
@echo off
echo ========================================
echo HEPBİRADURA TEST AUTOMATION BAŞLATILIYOR
echo ========================================
echo.

echo Python sürümü kontrol ediliyor...
python --version

echo.
echo Gerekli dizinler oluşturuluyor...
if not exist allure-results mkdir allure-results
if not exist reports mkdir reports
if not exist screenshots mkdir screenshots

echo.
echo Bağımlılıklar yükleniyor...
pip install -r requirements.txt

# Build Step 2: Test Execution (Sadece Allure için)
@echo off
echo.
echo ========================================
echo TESTLER ÇALIŞTIRILIYOR (SADECE ALLURE)
echo ========================================
echo.
pytest tests/test_smoke.py::TestHepsiburadaSmoke::test_full_automation -v --tb=short --alluredir=allure-results --no-reruns

# Build Step 3: Allure Report Generation
@echo off
echo.
echo ========================================
echo ALLURE RAPORU OLUŞTURULUYOR
echo ========================================
echo.
echo Eski Allure verileri temizleniyor...
if exist allure-results rmdir /s /q allure-results
if exist allure-report rmdir /s /q allure-report
echo pytest.ini konfigürasyonu kontrol ediliyor...
echo Test tek kez çalıştırılacak (rerun devre dışı)...
echo Allure raporu oluşturuluyor...
allure generate allure-results -o allure-report --clean --single-file
echo.
echo ========================================
echo TEST ÖZETİ OLUŞTURULUYOR (DEVRE DIŞI)
echo ========================================
echo.
echo Test özeti oluşturma devre dışı bırakıldı - sadece Allure kullanılacak

# ========================================
# 2. POST-BUILD ACTIONS (Jenkins'te Post-build Actions bölümünde ekleyin)
# ========================================

# A) Allure Report (ANA ÖNEMLİ!)
# - Plugin: Allure Report
# - Results path: allure-results
# - Report path: allure-report

# B) Sadece Allure raporu kullanılacak - diğer raporlar kaldırıldı

# ========================================
# 3. FREESTYLE JOB KURULUM ADIMLARI
# ========================================

# 1. Jenkins'te "New Item" > "Freestyle project" oluşturun
# 2. Source Code Management: Git
#    - Repository URL: https://github.com/haticeser/hepsiburada-test-automation.git
#    - Branch: main
# 3. Build Steps: "Execute Windows batch command" ekleyin
#    - Yukarıdaki 3 komutu tek tek ekleyin
# 4. Post-build Actions (Sadece Allure):
#    - "Allure Report" ekleyin (Results path: allure-results)
#    - Diğer raporlar kaldırıldı - sadece Allure kullanılacak

# ========================================
# 4. BAŞARI KRİTERLERİ
# ========================================

# ✅ Job başarıyla çalışır
# ✅ Test geçer (3-4 dakika sürer)
# ✅ Sol menüde sadece "Allure Report" linki görünür
# ✅ Allure raporunda tüm bölümler dolu:
#    - Overview: Test özeti
#    - Categories: Test kategorileri
#    - Suites: Test suite'leri
#    - Graphs: Test grafikleri
#    - Timeline: Zaman çizelgesi
#    - Behaviors: Test adımları
#    - Packages: Test paketleri
# ✅ Diğer raporlar (HTML, artifacts) kaldırıldı

# ========================================
# 5. SORUN GİDERME
# ========================================

# Allure raporu boşsa:
# 1. pytest komutunda --alluredir=allure-results parametresi olduğunu kontrol edin
# 2. allure-results dizininde JSON dosyaları oluştuğunu kontrol edin
# 3. Jenkins'te Allure Reports plugin yüklü olduğunu kontrol edin

# Test çalışmıyorsa:
# 1. Python ve pip yüklü olduğunu kontrol edin
# 2. requirements.txt dosyasının mevcut olduğunu kontrol edin
# 3. tests/test_smoke.py dosyasının mevcut olduğunu kontrol edin
