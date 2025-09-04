#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hepsiburada Test Otomasyonu - Hızlı Çalıştırma Scripti
Tests klasörü olmadan çalıştırılabilir
"""

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Pages modüllerini import et
from pages.hepsiburada_automation import HepsiburadaAutomation


def quick_setup():
    """Hızlı WebDriver kurulumu"""
    print("🚀 Hızlı WebDriver kurulumu...")
    
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")
    
    try:
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("✅ WebDriver hazır!")
        return driver
    except Exception as e:
        print(f"❌ WebDriver hatası: {e}")
        driver = webdriver.Chrome(options=chrome_options)
        print("✅ WebDriver hazır (fallback)!")
        return driver


def main():
    """Ana fonksiyon - Komut satırı argümanlarına göre çalışır"""
    print("🎯 Hepsiburada Test Otomasyonu - Hızlı Çalıştırma")
    print("="*60)
    
    # Komut satırı argümanlarını kontrol et
    if len(sys.argv) > 1:
        test_type = sys.argv[1].lower()
    else:
        print("📋 Kullanım:")
        print("  python run_automation.py full        # Tam otomasyon")
        print("  python run_automation.py register    # Sadece üye kaydı")
        print("  python run_automation.py login       # Sadece giriş")
        print("  python run_automation.py product     # Sadece ürün seçimi")
        print("  python run_automation.py filtered    # Filtreli ürün seçimi")
        print("  python run_automation.py tempail     # Sadece Tempail testi")
        print("  python run_automation.py menu        # İnteraktif menü")
        return
    
    driver = None
    
    try:
        # WebDriver'ı kur
        driver = quick_setup()
        automation = HepsiburadaAutomation(driver)
        
        print(f"🔍 Test türü: {test_type}")
        print("-" * 60)
        
        if test_type == "full":
            print("🚀 Tam otomasyon başlatılıyor...")
            success = automation.run_full_automation()
            
        elif test_type == "register":
            print("📝 Üye kaydı başlatılıyor...")
            # Email al
            automation.temp_email = automation.get_temp_email()
            if not automation.temp_email:
                print("❌ Email alınamadı")
                return
            
            # Kayıt başlat
            if automation.register_on_hepsiburada():
                # Doğrulama kodu bekle
                code = automation.wait_for_email_with_code(120)
                if code:
                    success = automation.complete_registration_with_code(code)
                else:
                    print("❌ Doğrulama kodu alınamadı")
                    return
            else:
                print("❌ Kayıt başlatılamadı")
                return
                
        elif test_type == "login":
            print("🔑 Giriş testi başlatılıyor...")
            success = automation.run_login_test()
            
        elif test_type == "product":
            print("🛍️ Ürün seçimi başlatılıyor...")
            success = automation.run_product_selection_test()
            
        elif test_type == "filtered":
            print("🎯 Filtreli ürün seçimi başlatılıyor...")
            success = automation.select_and_click_first_product()
            
        elif test_type == "tempail":
            print("📧 Tempail testi başlatılıyor...")
            email = automation.get_temp_email()
            success = email is not None
            if success:
                print(f"✅ Email alındı: {email}")
            
        elif test_type == "menu":
            print("📋 İnteraktif menü başlatılıyor...")
            # custom_automation.py'yi çalıştır
            import subprocess
            subprocess.run([sys.executable, "custom_automation.py"])
            return
            
        else:
            print(f"❌ Bilinmeyen test türü: {test_type}")
            return
        
        # Sonuç göster
        print("\n" + "="*60)
        if 'success' in locals():
            if success:
                print("🎉 İŞLEM BAŞARILI!")
                if hasattr(automation, 'temp_email') and automation.temp_email:
                    print(f"📧 Email: {automation.temp_email}")
                    print(f"🔒 Şifre: {automation.password}")
            else:
                print("❌ İŞLEM BAŞARISIZ!")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\n⏹️ İşlem kullanıcı tarafından durduruldu.")
        
    except Exception as e:
        print(f"\n❌ Hata: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        if driver:
            print("\n🔒 WebDriver kapatılıyor...")
            try:
                driver.quit()
                print("✅ WebDriver kapatıldı")
            except:
                print("⚠️ WebDriver kapatılırken hata oluştu")


if __name__ == "__main__":
    main()
