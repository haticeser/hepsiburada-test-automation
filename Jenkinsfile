# FREESTYLE JOB İÇİN KOMUTLAR
# Bu dosya freestyle job'da kullanılacak komutları içerir
# Pipeline job yerine freestyle job kullanın

# ========================================
# 1. BUILD STEPS (Build Steps)
# ========================================

# Python sürümünü kontrol et
python --version

# Gerekli dizinleri oluştur
if not exist allure-results mkdir allure-results
if not exist reports mkdir reports
if not exist screenshots mkdir screenshots

# Bağımlılıkları yükle
pip install -r requirements.txt

# Testleri çalıştır - Allure results için önemli parametreler
pytest tests/test_smoke.py -v --tb=short --alluredir=allure-results --html=reports/test_report.html --self-contained-html

# Allure raporu oluştur (opsiyonel - freestyle job'da Allure Reports plugin otomatik yapar)
allure generate allure-results -o allure-report --clean

# Test özeti oluştur
echo === TEST ÖZETİ === > test_summary.txt
echo Tarih: %date% %time% >> test_summary.txt
echo Branch: %GIT_BRANCH% >> test_summary.txt
echo Commit: %GIT_COMMIT% >> test_summary.txt
echo. >> test_summary.txt
echo === PYTEST SONUÇLARI === >> test_summary.txt
pytest --collect-only -q >> test_summary.txt 2>&1

# ========================================
# 2. POST-BUILD ACTIONS (Yapılandırma Sonrası Aksiyonlar)
# ========================================

# A) Allure Report
# - Plugin: Allure Report
# - Results path: allure-results
# - Report path: allure-report (opsiyonel)

# B) Publish HTML reports (opsiyonel)
# - HTML directory to archive: reports
# - Index page[s]: test_report.html
# - Report title: Pytest HTML Report

# C) Archive the artifacts
# - Files to archive: reports/*.html, test_summary.txt, allure-report.zip

# D) Email Notification (opsiyonel)
# - Recipients: test-team@company.com
# - Subject: ${PROJECT_NAME} - Build #${BUILD_NUMBER} - ${BUILD_STATUS}
# - Body: Test sonuçları ve rapor linkleri

# ========================================
# 3. FREESTYLE JOB KURULUM ADIMLARI
# ========================================

# 1. Jenkins'te "New Item" > "Freestyle project" oluşturun
# 2. Source Code Management: Git
#    - Repository URL: https://github.com/haticeser/hepsiburada-test-automation.git
#    - Branch: main
# 3. Build Steps: "Execute Windows batch command" ekleyin
#    - Yukarıdaki komutları tek tek ekleyin
# 4. Post-build Actions:
#    - "Allure Report" ekleyin
#      * Results path: allure-results
#      * Report path: allure-report
#    - "Publish HTML reports" ekleyin (opsiyonel)
#      * HTML directory: reports
#      * Index page: test_report.html
#      * Report title: Pytest HTML Report
#    - "Archive the artifacts" ekleyin
#      * Files to archive: reports/*.html, test_summary.txt

# ========================================
# 4. ALLURE RAPORU İÇİN ÖNEMLİ NOTLAR
# ========================================

# Allure raporunun dolu görünmesi için:
# 1. pytest komutunda --alluredir=allure-results parametresi OLMALI
# 2. allure-results dizininde JSON dosyaları oluşmalı
# 3. Jenkins'te Allure Reports plugin yüklü olmalı
# 4. Post-build Action'da Results path: allure-results olmalı

# Test sonuçları şu bölümleri dolduracak:
# - Overview: Test özeti ve genel bilgiler
# - Categories: Test kategorileri (smoke, regression, vb.)
# - Suites: Test suite'leri
# - Graphs: Test sonuç grafikleri
# - Timeline: Test çalışma zaman çizelgesi
# - Behaviors: Test davranışları ve adımları
# - Packages: Test paket yapısı
