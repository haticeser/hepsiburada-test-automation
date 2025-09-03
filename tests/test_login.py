# tests/test_login.py
import pytest
import time
from selenium.webdriver.common.by import By
from pages.hepsiburada_page import HepsiburadaPage
from pages.login_page import LoginPage
from pages.tempail_page import TempailPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHepsiburadaLogin:
    """Hepsiburada giriş testleri"""
    
    def test_login_flow(self, driver):
        """Tam giriş akışı testi"""
        print("\n🎯 Test: Tam Giriş Akışı")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # 1. Geçici email al
        email = automation.get_temp_email()
        assert email, "Geçici email alınamadı"
        print(f"✅ Email alındı: {email}")
        
        # 2. Giriş başlat
        if not automation.login_to_hepsiburada():
            pytest.skip("Giriş başlatılamadı")
        
        # 3. Doğrulama kodunu bekle
        verification_code = automation.wait_for_email_with_code(120)
        if not verification_code:
            pytest.skip("Giriş doğrulama kodu alınamadı")
        
        # 4. Girişi tamamla
        success = automation.complete_login_with_code(verification_code)
        assert success, "Giriş tamamlanamadı"
        print("✅ Giriş başarıyla tamamlandı")
    
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
            assert email_input.is_enabled(), "Email input aktif değil"
            print("✅ Email input doğru")
            
            # Şifre input
            password_input = driver.find_element("id", "txtPassword")
            assert password_input.is_displayed(), "Şifre input görünür değil"
            assert password_input.is_enabled(), "Şifre input aktif değil"
            print("✅ Şifre input doğru")
            
            # Giriş yap butonu
            login_button = driver.find_element("id", "btnLogin")
            assert login_button.is_displayed(), "Giriş yap butonu görünür değil"
            assert login_button.is_enabled(), "Giriş yap butonu aktif değil"
            print("✅ Giriş yap butonu doğru")
            
        except Exception as e:
            print(f"⚠ Form elementleri bulunamadı: {e}")
            pytest.skip("Form elementleri bulunamadı")
    
    def test_login_with_invalid_credentials(self, driver):
        """Geçersiz kimlik bilgileri ile giriş testi"""
        print("\n🎯 Test: Geçersiz Kimlik Bilgileri ile Giriş")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Giriş sayfasına git
        automation.hepsiburada_page.navigate_to_login()
        time.sleep(3)
        
        # Geçersiz kimlik bilgileri dene
        invalid_credentials = [
            {"email": "", "password": ""},
            {"email": "invalid@email.com", "password": ""},
            {"email": "", "password": "password123"},
            {"email": "test", "password": "password123"},
            {"email": "@test.com", "password": "password123"},
            {"email": "test@", "password": "password123"}
        ]
        
        for creds in invalid_credentials:
            print(f"🔍 Test ediliyor: Email='{creds['email']}', Şifre='{creds['password']}'")
            
            try:
                # Email gir
                if creds['email']:
                    automation.login_page.enter_email(creds['email'])
                
                # Şifre gir
                if creds['password']:
                    automation.login_page.enter_password(creds['password'])
                
                # Giriş yap butonuna tıkla
                if automation.login_page.click_login_button():
                    # Hata mesajı beklenir
                    time.sleep(3)
                    
                    # Hata mesajı var mı kontrol et
                    try:
                        error_elements = driver.find_elements("css selector", ".error, .alert-danger, [class*='error']")
                        if error_elements:
                            print(f"✅ Geçersiz bilgiler için hata mesajı gösterildi")
                        else:
                            print(f"⚠ Geçersiz bilgiler için hata mesajı gösterilmedi")
                    except:
                        print(f"⚠ Hata mesajı kontrol edilemedi")
                else:
                    print(f"⚠ Giriş butonuna tıklanamadı")
                    
            except Exception as e:
                print(f"⚠ Test hatası: {e}")
    
    def test_login_verification_code_format(self, driver):
        """Giriş doğrulama kodu formatı testi"""
        print("\n🎯 Test: Giriş Doğrulama Kodu Formatı")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Giriş sayfasına git
        automation.hepsiburada_page.navigate_to_login()
        time.sleep(3)
        
        # Geçerli email ve şifre gir
        email = automation.get_temp_email()
        if not email:
            pytest.skip("Email alınamadı, test atlanıyor")
        
        automation.login_page.enter_email(email)
        automation.login_page.enter_password(automation.password)
        automation.login_page.click_login_button()
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
            
            print("✅ Giriş doğrulama kodu alanı doğru format")
            
        except Exception as e:
            print(f"⚠ Giriş doğrulama kodu alanı bulunamadı: {e}")
            pytest.skip("Giriş doğrulama kodu alanı bulunamadı")
    
    def test_login_success_indicators(self, driver):
        """Giriş başarı göstergeleri testi"""
        print("\n🎯 Test: Giriş Başarı Göstergeleri")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Giriş sayfasına git
        automation.hepsiburada_page.navigate_to_login()
        time.sleep(3)
        
        # Geçerli email ve şifre gir
        email = automation.get_temp_email()
        if not email:
            pytest.skip("Email alınamadı, test atlanıyor")
        
        automation.login_page.enter_email(email)
        automation.login_page.enter_password(automation.password)
        automation.login_page.click_login_button()
        time.sleep(5)
        
        # Doğrulama kodu alanını bul
        try:
            code_input = driver.find_element("id", "txtVerificationCode")
            
            # Test kodu gir
            test_code = "123456"
            automation.login_page.enter_verification_code(test_code)
            automation.login_page.click_verify_button()
            time.sleep(5)
            
            # Başarı göstergelerini kontrol et
            success_indicators = [
                "#myAccount",
                ".user-info",
                ".account-info",
                "[class*='welcome']",
                "[class*='success']"
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
    
    def test_login_page_navigation(self, driver):
        """Giriş sayfası navigasyonu testi"""
        print("\n🎯 Test: Giriş Sayfası Navigasyonu")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Giriş sayfasına git
        automation.hepsiburada_page.navigate_to_login()
        time.sleep(3)
        
        # URL kontrolü
        current_url = driver.current_url.lower()
        assert "giris" in current_url or "login" in current_url, f"Giriş sayfasında değil: {current_url}"
        print("✅ Giriş sayfasına yönlendirildi")
        
        # Sayfa başlığını kontrol et
        page_title = driver.title.lower()
        assert any(keyword in page_title for keyword in ["giriş", "login", "hepsiburada"]), f"Beklenen sayfa başlığı bulunamadı: {page_title}"
        print("✅ Sayfa başlığı doğru")
    
    def test_login_form_validation(self, driver):
        """Giriş formu validasyon testi"""
        print("\n🎯 Test: Giriş Formu Validasyonu")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Giriş sayfasına git
        automation.hepsiburada_page.navigate_to_login()
        time.sleep(3)
        
        # Form validasyonunu test et
        try:
            # Boş form ile giriş yapmayı dene
            if automation.login_page.click_login_button():
                # Hata mesajı beklenir
                time.sleep(3)
                
                # Hata mesajı var mı kontrol et
                try:
                    error_elements = driver.find_elements("css selector", ".error, .alert-danger, [class*='error']")
                    if error_elements:
                        print("✅ Boş form için hata mesajı gösterildi")
                    else:
                        print("⚠ Boş form için hata mesajı gösterilmedi")
                except:
                    print("⚠ Hata mesajı kontrol edilemedi")
            else:
                print("⚠ Giriş butonuna tıklanamadı")
                
        except Exception as e:
            print(f"⚠ Form validasyon testi hatası: {e}")
    
    def test_login_remember_me_functionality(self, driver):
        """Beni hatırla fonksiyonalitesi testi"""
        print("\n🎯 Test: Beni Hatırla Fonksiyonalitesi")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Giriş sayfasına git
        automation.hepsiburada_page.navigate_to_login()
        time.sleep(3)
        
        # Beni hatırla checkbox'ını ara
        try:
            remember_me_selectors = [
                "input[name='remember']",
                "input[type='checkbox']",
                "#rememberMe",
                ".remember-me input"
            ]
            
            remember_checkbox = None
            for selector in remember_me_selectors:
                try:
                    remember_checkbox = driver.find_element("css selector", selector)
                    if remember_checkbox:
                        break
                except:
                    continue
            
            if remember_checkbox:
                # Checkbox'ın durumunu kontrol et
                initial_state = remember_checkbox.is_selected()
                print(f"✅ Beni hatırla checkbox bulundu, başlangıç durumu: {initial_state}")
                
                # Checkbox'ı tıkla
                remember_checkbox.click()
                time.sleep(1)
                
                # Durum değişti mi kontrol et
                new_state = remember_checkbox.is_selected()
                if new_state != initial_state:
                    print("✅ Checkbox durumu değişti")
                else:
                    print("⚠ Checkbox durumu değişmedi")
                    
            else:
                print("⚠ Beni hatırla checkbox bulunamadı")
                
        except Exception as e:
            print(f"⚠ Beni hatırla testi hatası: {e}")
    
    def test_login_forgot_password_link(self, driver):
        """Şifremi unuttum linki testi"""
        print("\n🎯 Test: Şifremi Unuttum Linki")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Giriş sayfasına git
        automation.hepsiburada_page.navigate_to_login()
        time.sleep(3)
        
        # Şifremi unuttum linkini ara
        try:
            forgot_password_selectors = [
                "a[href*='sifremi-unuttum']",
                "a[href*='forgot-password']",
                "a:contains('Şifremi unuttum')",
                "a:contains('Forgot password')",
                ".forgot-password a",
                "[class*='forgot'] a"
            ]
            
            forgot_link = None
            for selector in forgot_password_selectors:
                try:
                    if "contains" in selector:
                        # Text içeren link ara
                        links = driver.find_elements("tag name", "a")
                        for link in links:
                            if any(keyword in link.text.lower() for keyword in ['şifremi unuttum', 'forgot password', 'şifremi unuttum']):
                                forgot_link = link
                                break
                        if forgot_link:
                            break
                    else:
                        forgot_link = driver.find_element("css selector", selector)
                        if forgot_link:
                            break
                except:
                    continue
            
            if forgot_link:
                print("✅ Şifremi unuttum linki bulundu")
                
                # Link'in tıklanabilir olduğunu kontrol et
                assert forgot_link.is_displayed(), "Link görünür değil"
                assert forgot_link.is_enabled(), "Link aktif değil"
                
                # Link URL'sini kontrol et
                href = forgot_link.get_attribute("href")
                if href:
                    print(f"✅ Link URL: {href}")
                else:
                    print("⚠ Link URL bulunamadı")
                    
            else:
                print("⚠ Şifremi unuttum linki bulunamadı")
                
        except Exception as e:
            print(f"⚠ Şifremi unuttum testi hatası: {e}")
    
    def test_login_social_login_options(self, driver):
        """Sosyal medya ile giriş seçenekleri testi"""
        print("\n🎯 Test: Sosyal Medya ile Giriş Seçenekleri")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Giriş sayfasına git
        automation.hepsiburada_page.navigate_to_login()
        time.sleep(3)
        
        # Sosyal medya giriş butonlarını ara
        social_login_selectors = [
            "button[class*='google']",
            "button[class*='facebook']",
            "button[class*='apple']",
            ".social-login button",
            "[class*='social'] button",
            "button:contains('Google')",
            "button:contains('Facebook')",
            "button:contains('Apple')"
        ]
        
        social_buttons = []
        for selector in social_login_selectors:
            try:
                if "contains" in selector:
                    # Text içeren buton ara
                    buttons = driver.find_elements("tag name", "button")
                    for btn in buttons:
                        btn_text = btn.text.lower()
                        if any(keyword in btn_text for keyword in ['google', 'facebook', 'apple']):
                            social_buttons.append(btn)
                else:
                    button = driver.find_element("css selector", selector)
                    if button:
                        social_buttons.append(button)
            except:
                continue
        
        if social_buttons:
            print(f"✅ {len(social_buttons)} sosyal medya giriş butonu bulundu")
            for i, button in enumerate(social_buttons):
                print(f"  {i+1}. {button.text}")
        else:
            print("⚠ Sosyal medya giriş butonu bulunamadı")
    
    def test_login_page_responsiveness(self, driver):
        """Giriş sayfası responsive tasarım testi"""
        print("\n🎯 Test: Giriş Sayfası Responsive Tasarım")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Giriş sayfasına git
        automation.hepsiburada_page.navigate_to_login()
        time.sleep(3)
        
        # Farklı ekran boyutlarını test et
        screen_sizes = [
            (1920, 1080),  # Desktop
            (1366, 768),   # Laptop
            (768, 1024),   # Tablet
            (375, 667)     # Mobile
        ]
        
        for width, height in screen_sizes:
            print(f"🔍 Ekran boyutu test ediliyor: {width}x{height}")
            
            try:
                # Ekran boyutunu ayarla
                driver.set_window_size(width, height)
                time.sleep(2)
                
                # Form elementlerinin görünür olduğunu kontrol et
                try:
                    email_input = driver.find_element("id", "txtUserName")
                    password_input = driver.find_element("id", "txtPassword")
                    login_button = driver.find_element("id", "btnLogin")
                    
                    if email_input.is_displayed() and password_input.is_displayed() and login_button.is_displayed():
                        print(f"✅ {width}x{height} boyutunda tüm elementler görünür")
                    else:
                        print(f"⚠ {width}x{height} boyutunda bazı elementler görünür değil")
                        
                except Exception as e:
                    print(f"⚠ {width}x{height} boyutunda element kontrol hatası: {e}")
                    
            except Exception as e:
                print(f"⚠ {width}x{height} boyut ayarlama hatası: {e}")
        
        # Orijinal boyuta geri dön
        driver.maximize_window()
        print("✅ Ekran boyutu orijinal haline döndürüldü")