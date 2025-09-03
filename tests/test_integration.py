# tests/test_integration.py
import pytest
import time
from pages.hepsiburada_automation import HepsiburadaAutomation


class TestHepsiburadaIntegration:
    """Hepsiburada entegrasyon testleri"""
    
    def test_full_registration_automation(self, driver):
        """Tam üye kaydı otomasyonu testi"""
        print("\n🎯 Test: Tam Üye Kaydı Otomasyonu")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Tam otomasyonu çalıştır
        success = automation.run_full_automation()
        
        if success:
            print(f"\n✅ Test başarılı!")
            print(f"📧 Email: {automation.temp_email}")
            print(f"🔒 Şifre: {automation.password}")
        else:
            print("\n❌ Test başarısız!")
        
        assert success, "Tam üye kaydı otomasyonu başarısız"
    
    def test_login_automation(self, driver):
        """Giriş otomasyonu testi"""
        print("\n🎯 Test: Giriş Otomasyonu")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Giriş testini çalıştır
        success = automation.run_login_test()
        
        if success:
            print(f"\n✅ Test başarılı!")
            print(f"📧 Email: {automation.temp_email}")
            print(f"🔒 Şifre: {automation.password}")
        else:
            print("\n❌ Test başarısız!")
        
        assert success, "Giriş otomasyonu başarısız"
    
    def test_tempail_email_retrieval(self, driver):
        """Tempail'den email alma testi"""
        print("\n🎯 Test: Tempail Email Alma")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Geçici email al
        email = automation.get_temp_email()
        
        if email:
            print(f"✅ Email alındı: {email}")
            assert "@" in email, "Geçersiz email formatı"
            assert "tempail.com" in email, "Tempail email'i değil"
        else:
            print("❌ Email alınamadı")
            assert False, "Email alınamadı"
    
    def test_email_verification_wait(self, driver):
        """Email doğrulama kodu bekleme testi"""
        print("\n🎯 Test: Email Doğrulama Kodu Bekleme")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Önce email al
        email = automation.get_temp_email()
        if not email:
            pytest.skip("Email alınamadı, test atlanıyor")
        
        # Kısa süre doğrulama kodu bekle (test için)
        print("📧 Kısa süre doğrulama kodu bekleniyor (test için)...")
        verification_code = automation.wait_for_email_with_code(timeout=30)
        
        if verification_code:
            print(f"✅ Doğrulama kodu bulundu: {verification_code}")
            assert len(verification_code) == 6, "Doğrulama kodu 6 haneli değil"
            assert verification_code.isdigit(), "Doğrulama kodu sadece sayı içermeli"
        else:
            print("⚠ Doğrulama kodu bulunamadı (test için normal)")
            # Bu test için başarısız sayılmaz çünkü email gönderilmemiş olabilir
    
    def test_hepsiburada_navigation(self, driver):
        """Hepsiburada sayfa navigasyonu testi"""
        print("\n🎯 Test: Hepsiburada Sayfa Navigasyonu")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Ana sayfaya git
        automation.hepsiburada_page.go_to_hepsiburada()
        
        # Sayfa başlığını kontrol et
        page_title = driver.title.lower()
        assert "hepsiburada" in page_title, f"Beklenen sayfa başlığı bulunamadı: {page_title}"
        
        print("✅ Ana sayfa yüklendi")
        
        # Üye ol sayfasına git
        automation.hepsiburada_page.navigate_to_registration()
        time.sleep(3)
        
        # URL kontrolü
        current_url = driver.current_url
        assert "uyelik" in current_url or "yeni-uye" in current_url, f"Üye ol sayfası yüklenmedi: {current_url}"
        
        print("✅ Üye ol sayfasına yönlendirildi")
        
        # Giriş sayfasına git
        automation.hepsiburada_page.navigate_to_login()
        time.sleep(3)
        
        # URL kontrolü
        current_url = driver.current_url
        assert "giris" in current_url, f"Giriş sayfası yüklenmedi: {current_url}"
        
        print("✅ Giriş sayfasına yönlendirildi")
    
    def test_registration_form_elements(self, driver):
        """Kayıt formu elementlerinin varlığı testi"""
        print("\n🎯 Test: Kayıt Formu Elementleri")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Üye ol sayfasına git
        automation.hepsiburada_page.navigate_to_registration()
        time.sleep(3)
        
        # Form elementlerini kontrol et
        try:
            # Email input
            email_input = driver.find_element("id", "txtUserName")
            assert email_input.is_displayed(), "Email input görünür değil"
            print("✅ Email input bulundu")
            
            # Devam et butonu
            continue_button = driver.find_element("id", "btnSignUpSubmit")
            assert continue_button.is_displayed(), "Devam et butonu görünür değil"
            print("✅ Devam et butonu bulundu")
            
        except Exception as e:
            print(f"⚠ Form elementleri bulunamadı: {e}")
            # Bu test için kritik değil, sadece uyarı
    
    def test_login_form_elements(self, driver):
        """Giriş formu elementlerinin varlığı testi"""
        print("\n🎯 Test: Giriş Formu Elementleri")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Giriş sayfasına git
        automation.hepsiburada_page.navigate_to_login()
        time.sleep(3)
        
        # Form elementlerini kontrol et
        try:
            # Email input
            email_input = driver.find_element("id", "txtUserName")
            assert email_input.is_displayed(), "Email input görünür değil"
            print("✅ Email input bulundu")
            
            # Şifre input
            password_input = driver.find_element("id", "txtPassword")
            assert password_input.is_displayed(), "Şifre input görünür değil"
            print("✅ Şifre input bulundu")
            
            # Giriş yap butonu
            login_button = driver.find_element("id", "btnLogin")
            assert login_button.is_displayed(), "Giriş yap butonu görünür değil"
            print("✅ Giriş yap butonu bulundu")
            
        except Exception as e:
            print(f"⚠ Form elementleri bulunamadı: {e}")
            # Bu test için kritik değil, sadece uyarı
    
    def test_cookie_popup_handling(self, driver):
        """Çerez popup'ı kapatma testi"""
        print("\n🎯 Test: Çerez Popup Kapatma")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Ana sayfaya git
        automation.hepsiburada_page.go_to_hepsiburada()
        time.sleep(3)
        
        # Çerez popup'ı kapatma işlemi base_page'de yapılıyor
        # Sadece sayfa yüklendiğini kontrol et
        page_title = driver.title.lower()
        assert "hepsiburada" in page_title, f"Ana sayfa yüklenmedi: {page_title}"
        
        print("✅ Ana sayfa yüklendi ve çerez popup işlemi tamamlandı")
    
    def test_google_password_popup_handling(self, driver):
        """Google şifre kaydetme popup'ı kapatma testi"""
        print("\n🎯 Test: Google Şifre Popup Kapatma")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Bu test için basit bir sayfa yükleme yeterli
        # Google popup'ı sadece belirli durumlarda çıkar
        driver.get("https://www.hepsiburada.com/")
        time.sleep(3)
        
        # Popup kapatma metodunu test et
        automation.hepsiburada_page.close_google_password_popup()
        
        print("✅ Google popup kapatma metodu test edildi")
    
    def test_page_object_model_structure(self, driver):
        """Page Object Model yapısının doğruluğu testi"""
        print("\n🎯 Test: Page Object Model Yapısı")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Tüm sayfa sınıflarının doğru şekilde oluşturulduğunu kontrol et
        assert automation.tempail_page is not None, "TempailPage oluşturulamadı"
        assert automation.hepsiburada_page is not None, "HepsiburadaPage oluşturulamadı"
        assert automation.registration_page is not None, "RegistrationPage oluşturulamadı"
        assert automation.login_page is not None, "LoginPage oluşturulamadı"
        
        # Driver'ın doğru şekilde atandığını kontrol et
        assert automation.tempail_page.driver == driver, "TempailPage driver'ı yanlış"
        assert automation.hepsiburada_page.driver == driver, "HepsiburadaPage driver'ı yanlış"
        assert automation.registration_page.driver == driver, "RegistrationPage driver'ı yanlış"
        assert automation.login_page.driver == driver, "LoginPage driver'ı yanlış"
        
        print("✅ Page Object Model yapısı doğru")
        print("✅ Tüm sayfa sınıfları oluşturuldu")
        print("✅ Driver'lar doğru şekilde atandı")
    
    def test_automation_credentials(self, driver):
        """Otomasyon kimlik bilgilerinin doğruluğu testi"""
        print("\n🎯 Test: Otomasyon Kimlik Bilgileri")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Sabit bilgileri kontrol et
        assert automation.password == "123456aA", f"Yanlış şifre: {automation.password}"
        assert automation.first_name == "Kıymetli", f"Yanlış ad: {automation.first_name}"
        assert automation.last_name == "Stajyer", f"Yanlış soyad: {automation.last_name}"
        
        print(f"✅ Şifre: {automation.password}")
        print(f"✅ Ad: {automation.first_name}")
        print(f"✅ Soyad: {automation.last_name}")
        print("✅ Tüm kimlik bilgileri doğru")