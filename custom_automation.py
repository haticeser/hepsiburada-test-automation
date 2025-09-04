#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hepsiburada Test Otomasyonu - Özel Script
Tests klasörü olmadan çalıştırılabilir versiyon
"""

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Pages modüllerini import et
from pages.hepsiburada_automation import HepsiburadaAutomation


def setup_driver():
    """Chrome WebDriver'ı kurar ve yapılandırır"""
    print("🚀 Chrome WebDriver kuruluyor...")
    
    chrome_options = Options()
    
    # Anti-detection ayarları
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Performans ve görünüm ayarları
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-notifications")
    
    # GPU ve WebGL optimizasyonları (uyarıları minimize eder)
    chrome_options.add_argument("--enable-unsafe-swiftshader")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-gpu-sandbox")
    chrome_options.add_argument("--disable-gpu-process-crash-limit")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")
    chrome_options.add_argument("--disable-renderer-backgrounding")
    
    # Log seviyesini azalt
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--silent")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Memory ve performans
    chrome_options.add_argument("--memory-pressure-off")
    chrome_options.add_argument("--max_old_space_size=4096")
    
    try:
        # Manuel indirdiğin ChromeDriver 140 yolunu kullan
        service = Service("C:/Users/eserh/hepsiburada_test_automation/drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("✅ Chrome WebDriver 140 başarıyla kuruldu")
        return driver
    except Exception as e:
        print(f"❌ ChromeDriver 140 hatası: {e}")
        print("💡 ChromeDriver 140'ın doğru yerde olduğundan emin olun:")
        print("   C:/Users/eserh/hepsiburada_test_automation/drivers/chromedriver.exe")
        raise e


def show_menu():
    """Ana menüyü gösterir"""
    print("\n" + "="*60)
    print("🎯 Hepsiburada Test Otomasyonu - Özel Script")
    print("="*60)
    print("1. 🚀 Tam Otomasyon (Üyelik + Ürün Seçimi)")
    print("2. 📝 Sadece Üye Kaydı")
    print("3. 🔑 Sadece Giriş Testi")
    print("4. 🛍️ Sadece Ürün Seçimi")
    print("5. 🎯 Filtreli Ürün Seçimi (Lenovo + Intel Core i7)")
    print("6. 📧 Sadece Tempail Email Testi")
    print("7. ❌ Çıkış")
    print("="*60)


def run_full_automation(driver):
    """Tam otomasyon sürecini çalıştırır"""
    print("\n🚀 TAM OTOMASYON BAŞLATILIYOR...")
    print("="*50)
    print("📋 Süreç: Tempail Email → Üye Kaydı → Ürün Seçimi")
    print("="*50)
    
    automation = HepsiburadaAutomation(driver)
    
    try:
        success = automation.run_full_automation()
        
        if success:
            print("\n🎉 TAM OTOMASYON BAŞARILI!")
            print(f"📧 Kullanılan Email: {automation.temp_email}")
            print(f"🔒 Kullanılan Şifre: {automation.password}")
            print(f"👤 Ad Soyad: {automation.first_name} {automation.last_name}")
        else:
            print("\n❌ TAM OTOMASYON BAŞARISIZ!")
            
        return success
        
    except Exception as e:
        print(f"\n❌ Tam otomasyon hatası: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_registration_only(driver):
    """Sadece üye kaydı işlemini çalıştırır"""
    print("\n📝 SADECE ÜYE KAYDI BAŞLATILIYOR...")
    print("="*50)
    
    automation = HepsiburadaAutomation(driver)
    
    try:
        # 1. Tempail'den email al
        print("📧 Geçici email alınıyor...")
        automation.temp_email = automation.get_temp_email()
        if not automation.temp_email:
            print("❌ Geçici email alınamadı")
            return False
        
        print(f"✅ Email alındı: {automation.temp_email}")
        
        # 2. Üye kaydı başlat
        print("📝 Üye kaydı başlatılıyor...")
        if not automation.register_on_hepsiburada():
            print("❌ Üye kaydı başlatılamadı")
            return False
        
        # 3. Doğrulama kodu bekle
        print("📧 Doğrulama kodu bekleniyor...")
        registration_code = automation.wait_for_email_with_code(120)
        if not registration_code:
            print("❌ Doğrulama kodu alınamadı")
            return False
        
        print(f"✅ Doğrulama kodu alındı: {registration_code}")
        
        # 4. Üye kaydını tamamla
        print("✅ Üye kaydı tamamlanıyor...")
        success = automation.complete_registration_with_code(registration_code)
        
        if success:
            print("\n🎉 ÜYE KAYDI BAŞARILI!")
            print(f"📧 Email: {automation.temp_email}")
            print(f"🔒 Şifre: {automation.password}")
        else:
            print("\n❌ ÜYE KAYDI BAŞARISIZ!")
            
        return success
        
    except Exception as e:
        print(f"\n❌ Üye kaydı hatası: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_login_only(driver):
    """Sadece giriş testini çalıştırır"""
    print("\n🔑 SADECE GİRİŞ TESTİ BAŞLATILIYOR...")
    print("="*50)
    
    automation = HepsiburadaAutomation(driver)
    
    try:
        success = automation.run_login_test()
        
        if success:
            print("\n🎉 GİRİŞ TESTİ BAŞARILI!")
            print(f"📧 Email: {automation.temp_email}")
            print(f"🔒 Şifre: {automation.password}")
        else:
            print("\n❌ GİRİŞ TESTİ BAŞARISIZ!")
            
        return success
        
    except Exception as e:
        print(f"\n❌ Giriş testi hatası: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_product_selection_only(driver):
    """Sadece ürün seçimi testini çalıştırır"""
    print("\n🛍️ SADECE ÜRÜN SEÇİMİ BAŞLATILIYOR...")
    print("="*50)
    
    automation = HepsiburadaAutomation(driver)
    
    try:
        success = automation.run_product_selection_test()
        
        if success:
            print("\n🎉 ÜRÜN SEÇİMİ BAŞARILI!")
        else:
            print("\n❌ ÜRÜN SEÇİMİ BAŞARISIZ!")
            
        return success
        
    except Exception as e:
        print(f"\n❌ Ürün seçimi hatası: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_filtered_product_selection(driver):
    """Filtreli ürün seçimi testini çalıştırır"""
    print("\n🎯 FİLTRELİ ÜRÜN SEÇİMİ BAŞLATILIYOR...")
    print("="*50)
    print("🔍 Filtreler: Lenovo marka + Intel Core i7 işlemci")
    print("="*50)
    
    automation = HepsiburadaAutomation(driver)
    
    try:
        success = automation.select_and_click_first_product()
        
        if success:
            print("\n🎉 FİLTRELİ ÜRÜN SEÇİMİ BAŞARILI!")
            print("✅ Lenovo + Intel Core i7 filtrelenmiş ürün seçildi")
        else:
            print("\n❌ FİLTRELİ ÜRÜN SEÇİMİ BAŞARISIZ!")
            
        return success
        
    except Exception as e:
        print(f"\n❌ Filtreli ürün seçimi hatası: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_tempail_test_only(driver):
    """Sadece Tempail email testini çalıştırır"""
    print("\n📧 SADECE TEMPAIL EMAIL TESTİ BAŞLATILIYOR...")
    print("="*50)
    
    automation = HepsiburadaAutomation(driver)
    
    try:
        # Email al
        print("📧 Geçici email alınıyor...")
        email = automation.get_temp_email()
        
        if email:
            print(f"✅ Email başarıyla alındı: {email}")
            
            # Email formatını kontrol et
            if "@" in email and "tempail.com" in email:
                print("✅ Email formatı doğru")
                print("✅ Tempail email testi başarılı!")
                return True
            else:
                print("❌ Email formatı yanlış")
                return False
        else:
            print("❌ Email alınamadı")
            return False
            
    except Exception as e:
        print(f"\n❌ Tempail testi hatası: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Ana fonksiyon"""
    driver = None
    
    try:
        # WebDriver'ı kur
        driver = setup_driver()
        
        while True:
            show_menu()
            
            try:
                choice = input("\nSeçiminizi yapın (1-7): ").strip()
                
                if choice == "1":
                    success = run_full_automation(driver)
                elif choice == "2":
                    success = run_registration_only(driver)
                elif choice == "3":
                    success = run_login_only(driver)
                elif choice == "4":
                    success = run_product_selection_only(driver)
                elif choice == "5":
                    success = run_filtered_product_selection(driver)
                elif choice == "6":
                    success = run_tempail_test_only(driver)
                elif choice == "7":
                    print("\n👋 Çıkış yapılıyor...")
                    break
                else:
                    print("❌ Geçersiz seçim. Lütfen 1-7 arasında bir sayı girin.")
                    continue
                
                # Sonuç göster
                print("\n" + "="*60)
                if 'success' in locals():
                    if success:
                        print("🎉 İŞLEM BAŞARILI!")
                    else:
                        print("❌ İŞLEM BAŞARISIZ!")
                print("="*60)
                
                # Devam etmek isteyip istemediğini sor
                continue_choice = input("\nBaşka bir işlem yapmak ister misiniz? (e/h): ").strip().lower()
                if continue_choice not in ['e', 'evet', 'y', 'yes']:
                    print("\n👋 Çıkış yapılıyor...")
                    break
                    
            except KeyboardInterrupt:
                print("\n\n⏹️ İşlem kullanıcı tarafından durduruldu.")
                break
            except Exception as e:
                print(f"\n❌ Beklenmeyen hata: {e}")
                continue
                
    except Exception as e:
        print(f"\n❌ Kritik hata: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # WebDriver'ı kapat
        if driver:
            print("\n🔒 WebDriver kapatılıyor...")
            try:
                driver.quit()
                print("✅ WebDriver başarıyla kapatıldı")
            except:
                print("⚠️ WebDriver kapatılırken hata oluştu")
        
        print("\n👋 Program sonlandırıldı.")


if __name__ == "__main__":
    main()
