#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hepsiburada Test Otomasyonu - Özel Script
Tests klasörü olmadan çalıştırılabilir versiyon
WebDriver optimizasyonu ile hızlı çalışma
"""

import sys
import time

# Pages modüllerini import et
from pages.hepsiburada_automation import HepsiburadaAutomation
from pages.driver_manager import driver_manager


def setup_driver():
    """Chrome WebDriver'ı kurar ve yapılandırır - Optimize edilmiş versiyon"""
    print("🚀 WebDriver alınıyor... (tek seferlik kurulum)")
    return driver_manager.get_driver_safely()


def show_menu():
    """Ana menüyü gösterir"""
    print("\n" + "="*60)
    print("🎯 Hepsiburada Test Otomasyonu - Özel Script")
    print("="*60)
    print("1. 🚀 Tam Otomasyon (Giriş + Laptop Kategorisi + Filtreleme + Ürün Seçimi + Sepete Ekleme + Sepetim + Ürün Sayısını Arttır + Alışverişi Tamamla + Yeni Adres Ekle + Adres Formu Doldur + Kart Bilgilerini Gir + Kart Formu Doldur + Siparişi Onayla)")
    print("2. 📝 Sadece Üye Kaydı")
    print("3. 🔑 Sadece Giriş Testi")
    print("4. 🔑 Direkt Giriş (viva.vista000@gmail.com)")
    print("5. 🛍️ Sadece Ürün Seçimi")
    print("6. 🎯 Filtreli Ürün Seçimi (Lenovo + Intel Core i7)")
    print("7. 🛒 Sepete Ekleme Testi (Ürün Seçimi + Sepete Ekleme)")
    print("8. 🎯 Adım Adım Test (XPath ile Giriş)")
    print("9. 🔑 Tam Giriş Testi (Tüm Adımlar)")
    print("10. ❌ Çıkış")
    print("="*60)


def run_full_automation(driver):
    """Tam otomasyon sürecini çalıştırır"""
    print("\n🚀 TAM OTOMASYON BAŞLATILIYOR...")
    print("="*50)
    print("📋 Süreç: Giriş Yap → Laptop Kategorisi → Filtreleme → Ürün Seçimi → Sepete Ekleme → Sepetim → Ürün Sayısını Arttır → Alışverişi Tamamla → Yeni Adres Ekle → Adres Formu Doldur → Kart Bilgilerini Gir → Kart Formu Doldur → Siparişi Onayla")
    print("="*50)
    print("🎯 Detaylı süreç:")
    print("   1. 🔑 Hepsiburada'ya giriş yapılır (viva.vista000@gmail.com)")
    print("   2. 🖥️ Laptop kategorisine gidilir")
    print("   3. 🔍 Marka (Lenovo) ve işlemci (Intel Core i7) filtreleri uygulanır")
    print("   4. 🎯 İlk filtrelenmiş ürün seçilir ve ürün sayfasına gidilir")
    print("   5. 🛒 Ürün sepete eklenir")
    print("   6. 🛒 Sepetim butonuna tıklanır")
    print("   7. ➕ Sepetteki ürün sayısı +1 arttırılır")
    print("   8. 🛒 Alışverişi tamamla butonuna basılır")
    print("   9. 📍 Yeni adres ekle butonuna tıklanır")
    print("   10-19. 📝 Adres formu doldurulur (Ad, Soyad, Telefon, İş yeri, Kapalı günler, Bina, Şehir, Örnek, Fatura, Kaydet)")
    print("   20. 💳 Kart bilgilerini gir butonuna tıklanır")
    print("   21-27. 💳 Kart formu doldurulur (Kart No, Ay/Yıl, CVC, İsim, Checkbox'lar, Devam et)")
    print("   28-29. ✅ Siparişi onayla (Sözleşme checkbox + Siparişi onayla butonu)")
    print("="*50)
    
    automation = HepsiburadaAutomation(driver)
    
    try:
        success = automation.run_full_automation()
        
        if success:
            print("\n🎉 TAM OTOMASYON BAŞARILI!")
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
    print("⚠️ Bu test artık TempMail kullanmıyor - sabit email ile test yapın")
    return False


def run_login_only(driver):
    """Sadece giriş testini çalıştırır"""
    print("\n🔑 SADECE GİRİŞ TESTİ BAŞLATILIYOR...")
    print("="*50)
    print("⚠️ Bu test artık TempMail kullanmıyor - sabit email ile test yapın")
    return False


def run_direct_login_only(driver):
    """Sabit email ve şifre ile direkt giriş testini çalıştırır"""
    print("\n🔑 DİREKT GİRİŞ TESTİ BAŞLATILIYOR...")
    print("="*50)
    print("📧 Email: viva.vista000@gmail.com")
    print("🔒 Şifre: 123456aA")
    print("="*50)
    
    automation = HepsiburadaAutomation(driver)
    
    try:
        success = automation.run_direct_login_test()
        
        if success:
            print("\n🎉 DİREKT GİRİŞ TESTİ BAŞARILI!")
            print("✅ viva.vista000@gmail.com ile giriş yapıldı!")
        else:
            print("\n❌ DİREKT GİRİŞ TESTİ BAŞARISIZ!")
            
        return success
        
    except Exception as e:
        print(f"\n❌ Direkt giriş testi hatası: {e}")
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


def run_add_to_cart_test(driver):
    """Sepete ekleme testini çalıştırır"""
    print("\n🛒 SEPETE EKLEME TESTİ BAŞLATILIYOR...")
    print("="*50)
    print("📋 Süreç: Laptop Kategorisi → Filtreleme → Ürün Seçimi → Sepete Ekleme")
    print("="*50)
    
    automation = HepsiburadaAutomation(driver)
    
    try:
        success = automation.run_add_to_cart_test()
        
        if success:
            print("\n🎉 SEPETE EKLEME TESTİ BAŞARILI!")
            print("✅ Ürün seçimi ve sepete ekleme tamamlandı!")
        else:
            print("\n❌ SEPETE EKLEME TESTİ BAŞARISIZ!")
            
        return success
        
    except Exception as e:
        print(f"\n❌ Sepete ekleme testi hatası: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_step_by_step_test(driver):
    """Adım adım test - sadece navigasyon"""
    print("\n🎯 ADIM ADIM TEST BAŞLATILIYOR...")
    print("="*50)
    print("📋 Süreç:")
    print("   1. 🏠 Hepsiburada ana sayfasına git")
    print("   2. 🍪 Çerezleri kabul et")
    print("   3. 🖱️ Giriş Yap butonuna hover yap")
    print("   4. 🔗 Submenüden Giriş Yap'a tıkla")
    print("="*50)
    
    automation = HepsiburadaAutomation(driver)
    
    try:
        success = automation.run_step_by_step_test()
        
        if success:
            print("\n🎉 ADIM ADIM TEST BAŞARILI!")
            print("✅ Tüm navigasyon adımları başarıyla tamamlandı!")
        else:
            print("\n❌ ADIM ADIM TEST BAŞARISIZ!")
            
        return success
        
    except Exception as e:
        print(f"\n❌ Adım adım test hatası: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_full_login_test(driver):
    """Tam giriş testi - tüm adımlar"""
    print("\n🔑 TAM GİRİŞ TESTİ BAŞLATILIYOR...")
    print("="*50)
    print("📋 Süreç:")
    print("   1. 🏠 Hepsiburada ana sayfasına git")
    print("   2. 🍪 Çerezleri kabul et")
    print("   3. 🖱️ Giriş Yap butonuna hover yap")
    print("   4. 🔗 Submenüden Giriş Yap'a tıkla")
    print("   5. 📧 Email adresini gir (viva.vista000@gmail.com)")
    print("   6. 🔒 Şifreyi gir (123456aA)")
    print("   7. 🔑 Giriş yap butonuna tıkla")
    print("="*50)
    
    automation = HepsiburadaAutomation(driver)
    
    try:
        success = automation.run_full_login_test()
        
        if success:
            print("\n🎉 TAM GİRİŞ TESTİ BAŞARILI!")
            print("✅ Tüm giriş adımları başarıyla tamamlandı!")
        else:
            print("\n❌ TAM GİRİŞ TESTİ BAŞARISIZ!")
            
        return success
        
    except Exception as e:
        print(f"\n❌ Tam giriş testi hatası: {e}")
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
                choice = input("\nSeçiminizi yapın (1-10): ").strip()
                
                if choice == "1":
                    success = run_full_automation(driver)
                elif choice == "2":
                    success = run_registration_only(driver)
                elif choice == "3":
                    success = run_login_only(driver)
                elif choice == "4":
                    success = run_direct_login_only(driver)
                elif choice == "5":
                    success = run_product_selection_only(driver)
                elif choice == "6":
                    success = run_filtered_product_selection(driver)
                elif choice == "7":
                    success = run_add_to_cart_test(driver)
                elif choice == "8":
                    success = run_step_by_step_test(driver)
                elif choice == "9":
                    success = run_full_login_test(driver)
                elif choice == "10":
                    print("\n👋 Çıkış yapılıyor...")
                    break
                else:
                    print("❌ Geçersiz seçim. Lütfen 1-10 arasında bir sayı girin.")
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
        # WebDriver'ı kapatma - singleton pattern ile yönetiliyor
        # Sadece program sonunda kapatılacak
        print("\n👋 Program sonlandırıldı.")


if __name__ == "__main__":
    try:
        main()
    finally:
        # Program sonunda WebDriver'ı kapat
        print("\n🔒 WebDriver kapatılıyor...")
        driver_manager.quit_driver()
        print("✅ WebDriver kapatıldı")
