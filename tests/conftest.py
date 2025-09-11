#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pytest Configuration ve Fixtures
Jenkins ve Allure raporlama için gerekli konfigürasyonlar
"""

import pytest
import allure
import sys
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Proje root dizinini Python path'e ekle
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.driver_manager import driver_manager
from pages.hepsiburada_automation import HepsiburadaAutomation


@pytest.fixture(scope="session")
def driver():
    """WebDriver fixture - tüm testler için tek bir driver instance"""
    print("🚀 WebDriver başlatılıyor...")
    driver = driver_manager.get_driver_safely()
    yield driver
    print("🔒 WebDriver kapatılıyor...")
    try:
        driver.quit()
    except:
        pass  # Driver zaten kapanmış olabilir


@pytest.fixture(scope="function")
def automation(driver):
    """HepsiburadaAutomation instance fixture"""
    return HepsiburadaAutomation(driver)


@pytest.fixture(autouse=True)
def test_logger(request):
    """Her test için otomatik logger"""
    test_name = request.node.name
    start_time = datetime.now()
    
    print(f"\n{'='*60}")
    print(f"🧪 Test Başlatılıyor: {test_name}")
    print(f"⏰ Başlangıç Zamanı: {start_time.strftime('%H:%M:%S')}")
    print(f"{'='*60}")
    
    yield
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    print(f"\n{'='*60}")
    print(f"✅ Test Tamamlandı: {test_name}")
    print(f"⏰ Bitiş Zamanı: {end_time.strftime('%H:%M:%S')}")
    print(f"⏱️ Süre: {duration:.2f} saniye")
    print(f"{'='*60}")


@pytest.fixture(autouse=True)
def allure_environment_info():
    """Allure environment bilgileri"""
    # Allure environment bilgileri - bu versiyonda desteklenmiyor
    pass


def pytest_configure(config):
    """Pytest konfigürasyonu"""
    # Allure raporlama için gerekli ayarlar
    config.addinivalue_line(
        "markers", "smoke: Smoke testler - temel işlevsellik"
    )
    config.addinivalue_line(
        "markers", "regression: Regression testler - tam işlevsellik"
    )
    config.addinivalue_line(
        "markers", "slow: Yavaş testler - uzun süren işlemler"
    )


def pytest_collection_modifyitems(config, items):
    """Test koleksiyonu modifikasyonu"""
    for item in items:
        # Test dosyası adına göre marker ekle
        if "smoke" in item.nodeid:
            item.add_marker(pytest.mark.smoke)
        elif "regression" in item.nodeid:
            item.add_marker(pytest.mark.regression)
        else:
            item.add_marker(pytest.mark.regression)  # Varsayılan olarak regression
        
        # Uzun süren testler için slow marker
        if "full_automation" in item.nodeid or "complete" in item.nodeid:
            item.add_marker(pytest.mark.slow)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Test raporu oluşturma hook'u"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        # Test başarısız olduğunda screenshot al
        try:
            driver = item.funcargs.get('driver')
            if driver:
                screenshot_path = f"screenshots/failure_{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                os.makedirs("screenshots", exist_ok=True)
                driver.save_screenshot(screenshot_path)
                allure.attach.file(
                    screenshot_path,
                    name=f"Screenshot - {item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"⚠️ Screenshot alınamadı: {e}")
