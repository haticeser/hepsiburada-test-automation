#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hepsiburada Test Otomasyonu - Hızlı Çalıştırma Scripti
Tests klasörü olmadan çalıştırılabilir
WebDriver optimizasyonu ile hızlı çalışma
"""

import sys
import time

# Pages modüllerini import et
from pages.hepsiburada_automation import HepsiburadaAutomation
from pages.driver_manager import driver_manager


def quick_setup():
    """Hızlı WebDriver kurulumu - Optimize edilmiş versiyon"""
    print("🚀 WebDriver alınıyor... (tek seferlik kurulum)")
    return driver_manager.get_driver_safely()


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
        print("  python run_automation.py direct      # Direkt giriş (viva.vista000@gmail.com)")
        print("  python run_automation.py product     # Sadece ürün seçimi")
        print("  python run_automation.py filtered    # Filtreli ürün seçimi")
        print("  python run_automation.py cart        # Sepete ekleme testi")
        print("  python run_automation.py step        # Adım adım test (XPath ile)")
        print("  python run_automation.py fullogin    # Tam giriş testi (Tüm adımlar)")
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
            print("⚠️ Bu test artık TempMail kullanmıyor - sabit email ile test yapın")
            success = False
                
        elif test_type == "login":
            print("🔑 Giriş testi başlatılıyor...")
            success = automation.run_login_test()
            
        elif test_type == "direct":
            print("🔑 Direkt giriş testi başlatılıyor...")
            success = automation.run_direct_login_test()
            
        elif test_type == "product":
            print("🛍️ Ürün seçimi başlatılıyor...")
            success = automation.run_product_selection_test()
            
        elif test_type == "filtered":
            print("🎯 Filtreli ürün seçimi başlatılıyor...")
            success = automation.select_and_click_first_product()
            
        elif test_type == "cart":
            print("🛒 Sepet işlemleri testi başlatılıyor...")
            success = automation.run_cart_operations_test()
            
        elif test_type == "step":
            print("🎯 Adım adım test başlatılıyor...")
            success = automation.run_step_by_step_test()
            
        elif test_type == "fullogin":
            print("🔑 Tam giriş testi başlatılıyor...")
            success = automation.run_full_login_test()
            
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
        # WebDriver'ı kapatma - singleton pattern ile yönetiliyor
        # Sadece program sonunda kapatılacak
        pass


if __name__ == "__main__":
    try:
        main()
    finally:
        # Program sonunda WebDriver'ı kapat
        print("\n🔒 WebDriver kapatılıyor...")
        driver_manager.quit_driver()
        print("✅ WebDriver kapatıldı")
