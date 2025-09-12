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

# Build Step 2: Test Execution (ÖNEMLİ!)
@echo off
echo.
echo ========================================
echo TESTLER ÇALIŞTIRILIYOR
echo ========================================
echo.
pytest tests/test_smoke.py -v --tb=short --alluredir=allure-results --html=reports/test_report.html --self-contained-html

# Build Step 3: Allure Report Generation
@echo off
echo.
echo ========================================
echo ALLURE RAPORU OLUŞTURULUYOR
echo ========================================
echo.
allure generate allure-results -o allure-report --clean

# ========================================
# 2. POST-BUILD ACTIONS (Jenkins'te Post-build Actions bölümünde ekleyin)
# ========================================

# A) Allure Report (ANA ÖNEMLİ!)
# - Plugin: Allure Report
# - Results path: allure-results
# - Report path: allure-report

# B) Publish HTML reports (Opsiyonel)
# - HTML directory to archive: reports
# - Index page[s]: test_report.html
# - Report title: Pytest HTML Report

# C) Archive the artifacts
# - Files to archive: reports/*.html

# ========================================
# 3. FREESTYLE JOB KURULUM ADIMLARI
# ========================================

# 1. Jenkins'te "New Item" > "Freestyle project" oluşturun
# 2. Source Code Management: Git
#    - Repository URL: https://github.com/haticeser/hepsiburada-test-automation.git
#    - Branch: main
# 3. Build Steps: "Execute Windows batch command" ekleyin
#    - Yukarıdaki 3 komutu tek tek ekleyin
# 4. Post-build Actions:
#    - "Allure Report" ekleyin (Results path: allure-results)
#    - "Publish HTML reports" ekleyin (HTML directory: reports)
#    - "Archive the artifacts" ekleyin (Files: reports/*.html)

# ========================================
# 4. BAŞARI KRİTERLERİ
# ========================================

# ✅ Job başarıyla çalışır
# ✅ Test geçer (6-7 dakika sürer)
# ✅ Sol menüde "Allure Report" linki görünür
# ✅ Allure raporunda tüm bölümler dolu:
#    - Overview: Test özeti
#    - Categories: Test kategorileri
#    - Suites: Test suite'leri
#    - Graphs: Test grafikleri
#    - Timeline: Zaman çizelgesi
#    - Behaviors: Test adımları
#    - Packages: Test paketleri

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
