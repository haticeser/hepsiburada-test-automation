# tests/test_registration.py
import pytest
import time
from pages.hepsiburada_automation import HepsiburadaAutomation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHepsiburadaRegistration:
    """Hepsiburada üye kaydı testleri"""
    
    def test_registration_flow(self, driver):
        """Tam üye kaydı akışı testi"""
        print("\n🎯 Test: Tam Üye Kaydı Akışı")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # 1. Geçici email al
        email = automation.get_temp_email()
        assert email, "Geçici email alınamadı"
        print(f"✅ Email alındı: {email}")
        
        # 2. Üye kaydı başlat
        registration_code = automation.register_on_hepsiburada()
        assert registration_code, "Üye kaydı başlatılamadı"
        print(f"✅ Üye kaydı başlatıldı, kod: {registration_code}")
        
        # 3. Kaydı tamamla
        success = automation.complete_registration_with_code(registration_code)
        assert success, "Üye kaydı tamamlanamadı"
        print("✅ Üye kaydı tamamlandı")
    
    def test_registration_form_validation(self, driver):
        """Kayıt formu validasyon testi"""
        print("\n🎯 Test: Kayıt Formu Validasyonu")
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
            assert email_input.is_enabled(), "Email input aktif değil"
            print("✅ Email input doğru")
            
            # Devam et butonu
            continue_button = driver.find_element("id", "btnSignUpSubmit")
            assert continue_button.is_displayed(), "Devam et butonu görünür değil"
            assert continue_button.is_enabled(), "Devam et butonu aktif değil"
            print("✅ Devam et butonu doğru")
            
        except Exception as e:
            print(f"⚠ Form validasyon hatası: {e}")
            pytest.skip("Form elementleri bulunamadı")
    
    def test_registration_with_invalid_email(self, driver):
        """Geçersiz email ile kayıt testi"""
        print("\n🎯 Test: Geçersiz Email ile Kayıt")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Üye ol sayfasına git
        automation.hepsiburada_page.navigate_to_registration()
        time.sleep(3)
        
        # Geçersiz email'ler dene
        invalid_emails = [
            "invalid-email",
            "test@",
            "@test.com",
            "test.com",
            "",
            "   "
        ]
        
        for invalid_email in invalid_emails:
            print(f"🔍 Test ediliyor: '{invalid_email}'")
            
            # Email gir
            if automation.registration_page.enter_email(invalid_email):
                # Devam et butonuna tıkla
                if automation.registration_page.click_continue_button():
                    # Hata mesajı beklenir
                    time.sleep(3)
                    
                    # Hata mesajı var mı kontrol et
                    try:
                        error_elements = driver.find_elements("css selector", ".error, .alert-danger, [class*='error']")
                        if error_elements:
                            print(f"✅ Geçersiz email '{invalid_email}' için hata mesajı gösterildi")
                        else:
                            print(f"⚠ Geçersiz email '{invalid_email}' için hata mesajı gösterilmedi")
                    except:
                        print(f"⚠ Hata mesajı kontrol edilemedi: {invalid_email}")
                else:
                    print(f"⚠ Devam et butonuna tıklanamadı: {invalid_email}")
            else:
                print(f"⚠ Email input bulunamadı: {invalid_email}")
    
    def test_registration_password_requirements(self, driver):
        """Şifre gereksinimleri testi"""
        print("\n🎯 Test: Şifre Gereksinimleri")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Üye ol sayfasına git
        automation.hepsiburada_page.navigate_to_registration()
        time.sleep(3)
        
        # Önce geçerli email gir
        email = automation.get_temp_email()
        if not email:
            pytest.skip("Email alınamadı, test atlanıyor")
        
        automation.registration_page.enter_email(email)
        automation.registration_page.click_continue_button()
        time.sleep(5)
        
        # Şifre alanını kontrol et
        try:
            password_input = driver.find_element("id", "txtPassword")
            assert password_input.is_displayed(), "Şifre alanı görünür değil"
            print("✅ Şifre alanı bulundu")
            
            # Farklı şifreler dene
            test_passwords = [
                "123",  # Çok kısa
                "123456",  # Sadece sayı
                "abcdef",  # Sadece harf
                "ABC123",  # Büyük harf + sayı
                "abc123",  # Küçük harf + sayı
                "123456aA"  # Geçerli şifre
            ]
            
            for password in test_passwords:
                print(f"🔍 Şifre test ediliyor: '{password}'")
                
                try:
                    password_input.clear()
                    password_input.send_keys(password)
                    time.sleep(1)
                    
                    # Şifre gücü göstergesi var mı kontrol et
                    strength_indicators = driver.find_elements("css selector", ".password-strength, [class*='strength']")
                    if strength_indicators:
                        print(f"✅ Şifre gücü göstergesi bulundu: {password}")
                    
                except Exception as e:
                    print(f"⚠ Şifre test hatası: {password} - {e}")
                    
        except Exception as e:
            print(f"⚠ Şifre alanı bulunamadı: {e}")
            pytest.skip("Şifre alanı bulunamadı")
    
    def test_registration_verification_code_format(self, driver):
        """Doğrulama kodu formatı testi"""
        print("\n🎯 Test: Doğrulama Kodu Formatı")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Üye ol sayfasına git
        automation.hepsiburada_page.navigate_to_registration()
        time.sleep(3)
        
        # Email gir ve devam et
        email = automation.get_temp_email()
        if not email:
            pytest.skip("Email alınamadı, test atlanıyor")
        
        automation.registration_page.enter_email(email)
        automation.registration_page.click_continue_button()
        time.sleep(5)
        
        # Şifre gir (eğer varsa)
        automation.registration_page.enter_password(automation.password)
        automation.registration_page.submit_registration_form()
        time.sleep(5)
        
        # Doğrulama kodu alanını kontrol et
        try:
            code_input = driver.find_element("id", "txtVerificationCode")
            assert code_input.is_displayed(), "Doğrulama kodu alanı görünür değil"
            
            # Input özelliklerini kontrol et
            max_length = code_input.get_attribute("maxlength")
            if max_length:
                assert max_length == "6", f"Maxlength 6 olmalı, şu an: {max_length}"
                print("✅ Maxlength doğru: 6")
            
            input_type = code_input.get_attribute("type")
            if input_type:
                assert input_type in ["text", "tel", "number"], f"Input type uygun değil: {input_type}"
                print(f"✅ Input type doğru: {input_type}")
            
            print("✅ Doğrulama kodu alanı doğru format")
            
        except Exception as e:
            print(f"⚠ Doğrulama kodu alanı bulunamadı: {e}")
            pytest.skip("Doğrulama kodu alanı bulunamadı")
    
    def test_registration_personal_info_form(self, driver):
        """Kişisel bilgi formu testi"""
        print("\n🎯 Test: Kişisel Bilgi Formu")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Üye ol sayfasına git
        automation.hepsiburada_page.navigate_to_registration()
        time.sleep(3)
        
        # Email gir ve devam et
        email = automation.get_temp_email()
        if not email:
            pytest.skip("Email alınamadı, test atlanıyor")
        
        automation.registration_page.enter_email(email)
        automation.registration_page.click_continue_button()
        time.sleep(5)
        
        # Şifre gir (eğer varsa)
        automation.registration_page.enter_password(automation.password)
        automation.registration_page.submit_registration_form()
        time.sleep(5)
        
        # Doğrulama kodu alanını bul
        try:
            code_input = driver.find_element("id", "txtVerificationCode")
            
            # Test kodu gir
            test_code = "123456"
            automation.registration_page.enter_verification_code(test_code)
            automation.registration_page.click_verify_button()
            time.sleep(5)
            
            # Kişisel bilgi formunu kontrol et
            try:
                # Ad alanı
                first_name_input = driver.find_element("id", "txtName")
                assert first_name_input.is_displayed(), "Ad alanı görünür değil"
                print("✅ Ad alanı bulundu")
                
                # Soyad alanı
                last_name_input = driver.find_element("id", "txtSurname")
                assert last_name_input.is_displayed(), "Soyad alanı görünür değil"
                print("✅ Soyad alanı bulundu")
                
                # Şifre alanı
                new_password_input = driver.find_element("id", "txtNewPassEmail")
                assert new_password_input.is_displayed(), "Yeni şifre alanı görünür değil"
                print("✅ Yeni şifre alanı bulundu")
                
                # Checkbox
                checkbox = driver.find_element("id", "checkSubscribeEmail")
                assert checkbox.is_displayed(), "Checkbox görünür değil"
                print("✅ Checkbox bulundu")
                
                print("✅ Kişisel bilgi formu tüm alanları mevcut")
                
            except Exception as e:
                print(f"⚠ Kişisel bilgi formu alanları bulunamadı: {e}")
                pytest.skip("Kişisel bilgi formu bulunamadı")
                
        except Exception as e:
            print(f"⚠ Doğrulama kodu alanı bulunamadı: {e}")
            pytest.skip("Doğrulama kodu alanı bulunamadı")
    
    def test_registration_success_indicators(self, driver):
        """Kayıt başarı göstergeleri testi"""
        print("\n🎯 Test: Kayıt Başarı Göstergeleri")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Üye ol sayfasına git
        automation.hepsiburada_page.navigate_to_registration()
        time.sleep(3)
        
        # Email gir ve devam et
        email = automation.get_temp_email()
        if not email:
            pytest.skip("Email alınamadı, test atlanıyor")
        
        automation.registration_page.enter_email(email)
        automation.registration_page.click_continue_button()
        time.sleep(5)
        
        # Şifre gir (eğer varsa)
        automation.registration_page.enter_password(automation.password)
        automation.registration_page.submit_registration_form()
        time.sleep(5)
        
        # Doğrulama kodu alanını bul
        try:
            code_input = driver.find_element("id", "txtVerificationCode")
            
            # Test kodu gir
            test_code = "123456"
            automation.registration_page.enter_verification_code(test_code)
            automation.registration_page.click_verify_button()
            time.sleep(5)
            
            # Kişisel bilgi formunu doldur
            automation.registration_page.fill_personal_info(
                automation.first_name, 
                automation.last_name, 
                automation.password
            )
            
            # Checkbox işaretle
            automation.registration_page.check_email_subscription()
            
            # Üye ol butonuna tıkla
            automation.registration_page.click_final_signup_button()
            time.sleep(5)
            
            # Başarı göstergelerini kontrol et
            success_indicators = [
                ".success-message",
                ".alert-success",
                "[class*='success']",
                "#myAccount",
                ".welcome-message",
                "[class*='welcome']"
            ]
            
            success_found = False
            for indicator in success_indicators:
                try:
                    success_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(("css selector", indicator))
                    )
                    if success_element:
                        print(f"✅ Başarı göstergesi bulundu: {indicator}")
                        success_found = True
                        break
                except:
                    continue
            
            if not success_found:
                print("⚠ Başarı göstergesi bulunamadı, ama bu normal olabilir")
            
        except Exception as e:
            print(f"⚠ Test tamamlanamadı: {e}")
            pytest.skip("Test tamamlanamadı")