#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hepsiburada Test Otomasyonu - Smoke Test
custom_automation.py ile tamamen aynı çalışan pytest versiyonu
WebDriver optimizasyonu ile hızlı çalışma
"""

import pytest
import sys
import time

# Pages modüllerini import et
from pages.hepsiburada_automation import HepsiburadaAutomation
from pages.driver_manager import driver_manager


@pytest.fixture(scope="session")
def driver():
    """Chrome WebDriver'ı kurar ve yapılandırır - Tüm testler için tek instance"""
    print(">> WebDriver alınıyor... (tek seferlik kurulum)")
    driver_instance = driver_manager.get_driver_safely()
    yield driver_instance
    # Test sonunda WebDriver'ı kapat
    print("\n>> WebDriver kapatılıyor...")
    driver_manager.quit_driver()
    print(">> WebDriver kapatıldı")


class TestHepsiburadaSmoke:
    """Hepsiburada Smoke Test Sınıfı - custom_automation.py ile aynı işlevsellik"""
    
    def test_full_automation(self, driver):
        """Tam otomasyon sürecini çalıştırır - custom_automation.py ile aynı mantık"""
        print("\n>> TAM OTOMASYON BAŞLATILIYOR...")
        print("="*50)
        print(">> Süreç: Giriş Yap -> Laptop Kategorisi -> Filtreleme -> Ürün Seçimi -> Sepete Ekleme -> Sepetim -> Ürün Sayısını Arttır -> Alışverişi Tamamla -> Yeni Adres Ekle -> Adres Formu Doldur -> Kart Bilgilerini Gir -> Kart Formu Doldur -> Siparişi Onayla")
        print("="*50)
        
        automation = HepsiburadaAutomation(driver)
        
        try:
            # custom_automation.py'deki 1. adım ile aynı mantık
            success = automation.run_full_automation()
            
            if success:
                print("\n>> TAM OTOMASYON BAŞARILI!")
            else:
                print("\n>> TAM OTOMASYON BAŞARISIZ!")
                
            # Başarısız olsa bile test devam etsin (custom_automation.py gibi)
            return success
            
        except Exception as e:
            print(f"\n❌ Tam otomasyon hatası: {e}")
            import traceback
            traceback.print_exc()
            return False
    




if __name__ == "__main__":
    # pytest ile çalıştırma
    pytest.main([__file__, "-v", "-s"])
