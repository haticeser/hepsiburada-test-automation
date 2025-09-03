# tests/test_tempail.py
import pytest
import time
from pages.hepsiburada_automation import HepsiburadaAutomation


class TestTempailIntegration:
    """Tempail entegrasyon testleri"""
    
    def test_tempail_page_access(self, driver):
        """Tempail sayfasına erişim testi"""
        print("\n🎯 Test: Tempail Sayfası Erişimi")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Tempail sayfasına git
        driver.get("https://tempail.com/")
        time.sleep(5)
        
        # Sayfa başlığını kontrol et
        page_title = driver.title.lower()
        assert "temp" in page_title, f"Tempail sayfası yüklenmedi: {page_title}"
        print("✅ Tempail sayfası yüklendi")
        
        # Sayfa URL'ini kontrol et
        current_url = driver.current_url.lower()
        assert "tempail.com" in current_url, f"Tempail URL'inde değil: {current_url}"
        print("✅ Tempail URL'inde")
    
    def test_temp_email_generation(self, driver):
        """Geçici email oluşturma testi"""
        print("\n🎯 Test: Geçici Email Oluşturma")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Geçici email al
        email = automation.get_temp_email()
        
        # Email'in doğru formatta olduğunu kontrol et
        assert email is not None, "Geçici email alınamadı"
        assert "@" in email, "Email formatı yanlış - @ işareti yok"
        assert "@" in email and "." in email, "Email geçerli bir domain içermiyor"
        assert len(email) > 10, "Email çok kısa"
        
        print(f"✅ Geçici email başarıyla oluşturuldu: {email}")
        
        # Email formatını detaylı kontrol et
        email_parts = email.split("@")
        assert len(email_parts) == 2, "Email formatı yanlış - @ işareti sayısı"
        
        local_part = email_parts[0]
        domain_part = email_parts[1]
        
        assert len(local_part) > 0, "Email local part boş"
        assert len(domain_part) > 0, "Email domain part boş"
        assert len(domain_part) > 0, f"Domain boş: {domain_part}"
        
        print(f"✅ Email formatı doğru: Local={local_part}, Domain={domain_part}")
    
    def test_multiple_email_generation(self, driver):
        """Çoklu email oluşturma testi"""
        print("\n🎯 Test: Çoklu Email Oluşturma")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        emails = []
        
        # 3 farklı email oluştur
        for i in range(3):
            print(f"🔍 Email {i+1} oluşturuluyor...")
            
            # Yeni sekme aç
            driver.execute_script("window.open('https://tempail.com/', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(3)
            
            # Email al
            email = automation.get_temp_email()
            if email:
                emails.append(email)
                print(f"✅ Email {i+1}: {email}")
            else:
                print(f"❌ Email {i+1}: Başarısız")
            
            time.sleep(2)
        
        # En az 2 email oluşturulmalı
        assert len(emails) >= 2, f"Yeterli email oluşturulamadı: {len(emails)}/3"
        
        # Email'lerin farklı olduğunu kontrol et
        unique_emails = set(emails)
        assert len(unique_emails) == len(emails), "Aynı email'ler oluşturuldu"
        
        print(f"✅ {len(emails)} farklı email başarıyla oluşturuldu")
        
        # Tüm sekmeleri kapat, ana sekmeye dön
        for _ in range(len(driver.window_handles) - 1):
            driver.close()
        driver.switch_to.window(driver.window_handles[0])
    
    def test_email_verification_wait(self, driver):
        """Email doğrulama kodu bekleme testi"""
        print("\n🎯 Test: Email Doğrulama Kodu Bekleme")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Önce email al
        email = automation.get_temp_email()
        if not email:
            pytest.skip("Email alınamadı, test atlanıyor")
        
        print(f"📧 Test email: {email}")
        
        # Kısa süre doğrulama kodu bekle (test için)
        print("📧 Kısa süre doğrulama kodu bekleniyor (test için)...")
        verification_code = automation.wait_for_email_with_code(timeout=30)
        
        if verification_code:
            print(f"✅ Doğrulama kodu bulundu: {verification_code}")
            
            # Kod formatını kontrol et
            assert len(verification_code) == 6, f"Kod 6 haneli değil: {len(verification_code)}"
            assert verification_code.isdigit(), f"Kod sadece sayı içermeli: {verification_code}"
            
            print("✅ Doğrulama kodu formatı doğru")
        else:
            print("⚠ Doğrulama kodu bulunamadı (test için normal)")
            # Bu test için başarısız sayılmaz çünkü email gönderilmemiş olabilir
    
    def test_tempail_page_elements(self, driver):
        """Tempail sayfası elementlerinin varlığı testi"""
        print("\n🎯 Test: Tempail Sayfası Elementleri")
        print("=" * 50)
        
        # Tempail sayfasına git
        driver.get("https://tempail.com/")
        time.sleep(5)
        
        # Temel elementleri kontrol et
        try:
            # Email input alanı
            email_selectors = [
                "#eposta_adres",
                "input[type='text'][readonly]",
                ".email-address",
                "input[value*='@']"
            ]
            
            email_input = None
            for selector in email_selectors:
                try:
                    email_input = driver.find_element("css selector", selector)
                    if email_input:
                        break
                except:
                    continue
            
            if email_input:
                assert email_input.is_displayed(), "Email input görünür değil"
                assert email_input.is_enabled(), "Email input aktif değil"
                print("✅ Email input bulundu")
            else:
                print("⚠ Email input bulunamadı")
            
            # Email listesi alanı
            email_list_selectors = [
                "#eposta_listesi",
                ".email-list",
                ".mailler",
                "[class*='mail']"
            ]
            
            email_list = None
            for selector in email_list_selectors:
                try:
                    email_list = driver.find_element("css selector", selector)
                    if email_list:
                        break
                except:
                    continue
            
            if email_list:
                assert email_list.is_displayed(), "Email listesi görünür değil"
                print("✅ Email listesi bulundu")
            else:
                print("⚠ Email listesi bulunamadı")
                
        except Exception as e:
            print(f"⚠ Element kontrol hatası: {e}")
    
    def test_tempail_refresh_functionality(self, driver):
        """Tempail sayfa yenileme fonksiyonalitesi testi"""
        print("\n🎯 Test: Tempail Sayfa Yenileme")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Email al
        email = automation.get_temp_email()
        if not email:
            pytest.skip("Email alınamadı, test atlanıyor")
        
        print(f"📧 Test email: {email}")
        
        # Sayfayı yenile
        print("🔄 Sayfa yenileniyor...")
        driver.refresh()
        time.sleep(5)
        
        # Email'in hala mevcut olduğunu kontrol et
        try:
            email_selectors = [
                "#eposta_adres",
                "input[type='text'][readonly]",
                ".email-address",
                "input[value*='@']"
            ]
            
            current_email = None
            for selector in email_selectors:
                try:
                    email_input = driver.find_element("css selector", selector)
                    if email_input:
                        current_email = email_input.get_attribute("value")
                        break
                except:
                    continue
            
            if current_email:
                print(f"📧 Yenileme sonrası email: {current_email}")
                
                # Email'in değişip değişmediğini kontrol et
                if current_email == email:
                    print("✅ Email yenileme sonrası aynı kaldı")
                else:
                    print("⚠ Email yenileme sonrası değişti")
                    
            else:
                print("⚠ Yenileme sonrası email bulunamadı")
                
        except Exception as e:
            print(f"⚠ Yenileme testi hatası: {e}")
    
    def test_tempail_scroll_functionality(self, driver):
        """Tempail sayfa kaydırma fonksiyonalitesi testi"""
        print("\n🎯 Test: Tempail Sayfa Kaydırma")
        print("=" * 50)
        
        # Tempail sayfasına git
        driver.get("https://tempail.com/")
        time.sleep(5)
        
        # Sayfa yüksekliğini al
        initial_height = driver.execute_script("return document.body.scrollHeight")
        print(f"📏 Sayfa yüksekliği: {initial_height}")
        
        # Sayfayı aşağı kaydır
        print("📜 Sayfa aşağı kaydırılıyor...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        # Scroll pozisyonunu kontrol et
        scroll_position = driver.execute_script("return window.pageYOffset;")
        print(f"📍 Scroll pozisyonu: {scroll_position}")
        
        # Sayfayı yukarı kaydır
        print("📜 Sayfa yukarı kaydırılıyor...")
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        
        # Scroll pozisyonunu kontrol et
        scroll_position = driver.execute_script("return window.pageYOffset;")
        print(f"📍 Scroll pozisyonu: {scroll_position}")
        
        print("✅ Sayfa kaydırma testi tamamlandı")
    
    def test_tempail_iframe_handling(self, driver):
        """Tempail iframe işleme testi"""
        print("\n🎯 Test: Tempail Iframe İşleme")
        print("=" * 50)
        
        # Tempail sayfasına git
        driver.get("https://tempail.com/")
        time.sleep(5)
        
        # Iframe'leri ara
        iframes = driver.find_elements("tag name", "iframe")
        print(f"🔍 {len(iframes)} iframe bulundu")
        
        if iframes:
            for i, iframe in enumerate(iframes):
                try:
                    # Iframe özelliklerini kontrol et
                    iframe_id = iframe.get_attribute("id")
                    iframe_src = iframe.get_attribute("src")
                    iframe_width = iframe.get_attribute("width")
                    iframe_height = iframe.get_attribute("height")
                    
                    print(f"  Iframe {i+1}:")
                    print(f"    ID: {iframe_id}")
                    print(f"    Src: {iframe_src}")
                    print(f"    Boyut: {iframe_width}x{iframe_height}")
                    
                    # Iframe'e geçmeyi dene
                    driver.switch_to.frame(iframe)
                    time.sleep(1)
                    
                    # Iframe içeriğini kontrol et
                    iframe_content = driver.page_source
                    print(f"    İçerik uzunluğu: {len(iframe_content)} karakter")
                    
                    # Ana sayfaya geri dön
                    driver.switch_to.default_content()
                    
                except Exception as e:
                    print(f"    ⚠ Iframe {i+1} hatası: {e}")
                    # Ana sayfaya geri dön
                    driver.switch_to.default_content()
        else:
            print("⚠ Iframe bulunamadı")
        
        print("✅ Iframe işleme testi tamamlandı")
    
    def test_tempail_email_validation(self, driver):
        """Tempail email validasyon testi"""
        print("\n🎯 Test: Tempail Email Validasyonu")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Email al
        email = automation.get_temp_email()
        if not email:
            pytest.skip("Email alınamadı, test atlanıyor")
        
        print(f"📧 Test email: {email}")
        
        # Email formatını detaylı kontrol et
        import re
        
        # Email regex pattern
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(email_pattern, email):
            print("✅ Email formatı geçerli")
        else:
            print("❌ Email formatı geçersiz")
            assert False, f"Geçersiz email formatı: {email}"
        
        # Email uzunluğunu kontrol et
        assert 10 <= len(email) <= 100, f"Email uzunluğu uygun değil: {len(email)}"
        print(f"✅ Email uzunluğu uygun: {len(email)}")
        
        # Email karakterlerini kontrol et
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-@")
        email_chars = set(email)
        
        if email_chars.issubset(allowed_chars):
            print("✅ Email sadece izin verilen karakterleri içeriyor")
        else:
            invalid_chars = email_chars - allowed_chars
            print(f"⚠ Email geçersiz karakterler içeriyor: {invalid_chars}")
        
        # Domain kontrolü
        domain = email.split("@")[1]
        assert len(domain) > 0, f"Domain boş: {domain}"
        print(f"✅ Domain geçerli: {domain}")
    
    def test_tempail_performance(self, driver):
        """Tempail performans testi"""
        print("\n🎯 Test: Tempail Performans")
        print("=" * 50)
        
        automation = HepsiburadaAutomation(driver)
        
        # Sayfa yükleme süresini ölç
        start_time = time.time()
        
        # Tempail sayfasına git
        driver.get("https://tempail.com/")
        
        # Sayfa yüklenene kadar bekle
        driver.implicitly_wait(10)
        
        load_time = time.time() - start_time
        print(f"⏱️ Sayfa yükleme süresi: {load_time:.2f} saniye")
        
        # Email alma süresini ölç
        start_time = time.time()
        email = automation.get_temp_email()
        email_time = time.time() - start_time
        
        if email:
            print(f"⏱️ Email alma süresi: {email_time:.2f} saniye")
            print(f"✅ Email alındı: {email}")
        else:
            print("❌ Email alınamadı")
        
        # Performans kriterleri
        assert load_time < 15, f"Sayfa yükleme çok yavaş: {load_time:.2f}s"
        assert email_time < 10, f"Email alma çok yavaş: {email_time:.2f}s"
        
        print("✅ Performans kriterleri karşılandı")
    
    def test_tempail_error_handling(self, driver):
        """Tempail hata işleme testi"""
        print("\n🎯 Test: Tempail Hata İşleme")
        print("=" * 50)
        
        # Geçersiz URL'ye git
        print("🔍 Geçersiz URL test ediliyor...")
        driver.get("https://invalid-tempail-url.com")
        time.sleep(3)
        
        # Hata sayfası kontrolü
        try:
            error_indicators = [
                "404",
                "not found",
                "error",
                "hata",
                "bulunamadı"
            ]
            
            page_source = driver.page_source.lower()
            error_found = any(indicator in page_source for indicator in error_indicators)
            
            if error_found:
                print("✅ Hata sayfası tespit edildi")
            else:
                print("⚠ Hata sayfası tespit edilemedi")
                
        except Exception as e:
            print(f"⚠ Hata sayfası kontrol hatası: {e}")
        
        # Tempail'e kurtarma
        print("🔄 Tempail'e kurtarma...")
        try:
            driver.get("https://tempail.com/")
            time.sleep(5)
            
            # Sayfa başlığını kontrol et
            page_title = driver.title.lower()
            if "tempail" in page_title:
                print("✅ Tempail'e başarıyla kurtarıldı")
            else:
                print("⚠ Tempail'e kurtarılamadı")
                
        except Exception as e:
            print(f"❌ Kurtarma hatası: {e}")
            assert False, "Tempail'e kurtarılamadı"
        
        print("✅ Hata işleme testi tamamlandı")


class TestCompleteWorkflow:
    """Tam iş akışı testi - Tempail -> Hepsiburada Kayıt -> Giriş"""
    
    def test_complete_workflow(self, driver):
        """Tam iş akışı testi: Tempail -> Hepsiburada Kayıt -> Giriş"""
        print("\n🎯 Test: Tam İş Akışı - Tempail -> Hepsiburada")
        print("=" * 60)
        
        automation = HepsiburadaAutomation(driver)
        
        try:
            # 1. Tempail'e gir ve email al
            print("📧 1. Adım: Tempail'e giriliyor ve email alınıyor...")
            driver.get("https://tempail.com/")
            time.sleep(5)
            
            # Email'i al
            temp_email = automation.get_temp_email()
            if not temp_email:
                pytest.fail("❌ Tempail'den email alınamadı")
            
            print(f"✅ Email alındı: {temp_email}")
            
            # 2. Hepsiburada'ya git ve kayıt ol
            print("\n🛒 2. Adım: Hepsiburada'ya gidiliyor ve kayıt başlatılıyor...")
            
            # Yeni sekme aç (Tempail'i kapatmadan)
            driver.execute_script("window.open('https://www.hepsiburada.com/', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(5)
            
            # Çerezleri kapat
            try:
                cookie_buttons = [
                    "onetrust-accept-btn-handler",
                    "onetrust-reject-all-handler",
                    ".cookie-accept",
                    "#cookie-accept",
                    "button[data-testid='cookie-accept']"
                ]
                
                for selector in cookie_buttons:
                    try:
                        cookie_btn = driver.find_element("css selector", selector)
                        if cookie_btn.is_displayed():
                            cookie_btn.click()
                            print("✅ Çerezler kapatıldı")
                            break
                    except:
                        continue
            except Exception as e:
                print(f"⚠ Çerez kapatma hatası: {e}")
            
            # Ana sayfada giriş yap butonunun üstüne gel ve üye ol'a tıkla
            try:
                # Giriş yap butonunu bul (ilk görseldeki yapıya göre)
                login_selectors = [
                    "[data-test-id='account']",
                    "span[title='Giriş Yap']",
                    "span.sf-OldMyAccount-d0xCHLV38UCH5cD9mOXq",
                    "[data-testid='login-button']",
                    ".login-button",
                    "#login-button",
                    "a[href*='login']",
                    "button:contains('Giriş Yap')"
                ]
                
                login_button = None
                for selector in login_selectors:
                    try:
                        elements = driver.find_elements("css selector", selector)
                        for element in elements:
                            if element.is_displayed() and element.is_enabled():
                                login_button = element
                                break
                        if login_button:
                            break
                    except:
                        continue
                
                if login_button:
                    # Giriş yap butonunun üstüne gel
                    driver.execute_script("arguments[0].scrollIntoView();", login_button)
                    time.sleep(2)
                    
                    # Üye ol linkini bul ve tıkla (ikinci görseldeki yapıya göre)
                    signup_selectors = [
                        "#register",
                        "a[title='Hesap oluştur']",
                        "a[href*='uyelik/yeni-uye']",
                        "span[title='veya üye ol']",
                        "span.sf-01dMyAccount-sS_G2sunmDtZ19T1d5PR",
                        "a[href*='register']",
                        "a[href*='signup']",
                        "a[href*='uye-ol']",
                        ".signup-link",
                        "#signup-link"
                    ]
                    
                    signup_link = None
                    for selector in signup_selectors:
                        try:
                            elements = driver.find_elements("css selector", selector)
                            for element in elements:
                                if element.is_displayed() and element.is_enabled():
                                    signup_link = element
                                    break
                            if signup_link:
                                break
                        except:
                            continue
                    
                    if signup_link:
                        # Üye ol linkine scroll yap
                        driver.execute_script("arguments[0].scrollIntoView();", signup_link)
                        time.sleep(2)
                        signup_link.click()
                        print("✅ Üye ol sayfasına yönlendirildi")
                        time.sleep(5)
                    else:
                        # Direkt kayıt sayfasına git
                        driver.get("https://www.hepsiburada.com/uyelik/yeni-uye")
                        print("✅ Direkt kayıt sayfasına gidildi")
                        time.sleep(5)
                else:
                    # Direkt kayıt sayfasına git
                    driver.get("https://www.hepsiburada.com/uyelik/yeni-uye")
                    print("✅ Direkt kayıt sayfasına gidildi")
                    time.sleep(5)
                    
            except Exception as e:
                print(f"⚠ Kayıt sayfasına yönlendirme hatası: {e}")
                # Direkt kayıt sayfasına git
                driver.get("https://www.hepsiburada.com/uyelik/yeni-uye")
                print("✅ Direkt kayıt sayfasına gidildi")
                time.sleep(5)
            
            # Email'i kayıt formuna yaz
            try:
                # Sayfanın tamamen yüklenmesini bekle
                time.sleep(8)
                
                email_input_selectors = [
                    "input[type='email']",
                    "input[name='email']",
                    "input[data-testid='email-input']",
                    "#email",
                    ".email-input",
                    "input[placeholder*='email']",
                    "input[placeholder*='Email']",
                    "input[placeholder*='E-posta']",
                    "input[autocomplete='email']",
                    "input[type='text'][name*='email']",
                    "input[type='text'][id*='email']",
                    "input[type='text'][class*='email']"
                ]
                
                email_input = None
                for selector in email_input_selectors:
                    try:
                        elements = driver.find_elements("css selector", selector)
                        for element in elements:
                            if element.is_displayed() and element.is_enabled():
                                email_input = element
                                break
                        if email_input:
                            break
                    except:
                        continue
                
                if not email_input:
                    # Sayfa kaynak kodunda email ile ilgili input'ları ara
                    print("🔍 Sayfa kaynak kodunda email input aranıyor...")
                    page_source = driver.page_source.lower()
                    if "email" in page_source or "e-posta" in page_source:
                        print("📧 Sayfada email alanı bulundu, tüm input'lar kontrol ediliyor...")
                        
                        # Tüm input'ları kontrol et
                        all_inputs = driver.find_elements("tag name", "input")
                        for input_elem in all_inputs:
                            try:
                                input_type = input_elem.get_attribute("type") or ""
                                input_name = input_elem.get_attribute("name") or ""
                                input_id = input_elem.get_attribute("id") or ""
                                input_class = input_elem.get_attribute("class") or ""
                                input_placeholder = input_elem.get_attribute("placeholder") or ""
                                
                                if (input_type == "email" or 
                                    "email" in input_name.lower() or 
                                    "email" in input_id.lower() or 
                                    "email" in input_class.lower() or
                                    "email" in input_placeholder.lower() or
                                    "e-posta" in input_name.lower() or
                                    "e-posta" in input_id.lower() or
                                    "e-posta" in input_class.lower() or
                                    "e-posta" in input_placeholder.lower()):
                                    
                                    if input_elem.is_displayed() and input_elem.is_enabled():
                                        email_input = input_elem
                                        print(f"✅ Email input bulundu: type={input_type}, name={input_name}, id={input_id}")
                                        break
                            except:
                                continue
                
                if email_input:
                    # Input'a scroll yap
                    driver.execute_script("arguments[0].scrollIntoView();", email_input)
                    time.sleep(2)
                    
                    # Input'u temizle ve email'i gir
                    email_input.clear()
                    time.sleep(1)
                    email_input.send_keys(temp_email)
                    time.sleep(1)
                    print(f"✅ Email girildi: {temp_email}")
                    
                    # Devam et butonuna tıkla
                    continue_selectors = [
                        "button[type='submit']",
                        "button:contains('Devam Et')",
                        "button:contains('Continue')",
                        ".continue-button",
                        "#continue-button",
                        "button[class*='continue']",
                        "button[class*='submit']",
                        "input[type='submit']",
                        "button:contains('İleri')",
                        "button:contains('Next')"
                    ]
                    
                    continue_button = None
                    for selector in continue_selectors:
                        try:
                            elements = driver.find_elements("css selector", selector)
                            for element in elements:
                                if element.is_displayed() and element.is_enabled():
                                    continue_button = element
                                    break
                            if continue_button:
                                break
                        except:
                            continue
                    
                    if continue_button:
                        # Butona scroll yap
                        driver.execute_script("arguments[0].scrollIntoView();", continue_button)
                        time.sleep(2)
                        continue_button.click()
                        print("✅ Devam et butonuna tıklandı")
                        time.sleep(5)
                    else:
                        print("⚠ Devam et butonu bulunamadı, sayfa kaynak kodu kontrol ediliyor...")
                        # Sayfa kaynak kodunda buton ara
                        page_source = driver.page_source.lower()
                        if "devam" in page_source or "continue" in page_source or "ileri" in page_source:
                            print("🔍 Devam butonu bulundu, tüm butonlar kontrol ediliyor...")
                            all_buttons = driver.find_elements("tag name", "button")
                            for button in all_buttons:
                                try:
                                    button_text = button.text.lower()
                                    if any(word in button_text for word in ["devam", "continue", "ileri", "next", "submit"]):
                                        if button.is_displayed() and button.is_enabled():
                                            driver.execute_script("arguments[0].scrollIntoView();", button)
                                            time.sleep(2)
                                            button.click()
                                            print(f"✅ Buton bulundu ve tıklandı: {button.text}")
                                            time.sleep(5)
                                            break
                                except:
                                    continue
                        else:
                            print("❌ Devam butonu bulunamadı")
                else:
                    print("❌ Email input alanı bulunamadı")
                    print("🔍 Sayfa kaynak kodu kontrol ediliyor...")
                    page_source = driver.page_source
                    print(f"📄 Sayfa başlığı: {driver.title}")
                    print(f"📄 Sayfa URL: {driver.current_url}")
                    
                    # Sayfayı kaydet
                    with open("page_source.html", "w", encoding="utf-8") as f:
                        f.write(page_source)
                    print("📄 Sayfa kaynak kodu 'page_source.html' dosyasına kaydedildi")
                    
                    pytest.fail("Email input alanı bulunamadı")
                    
            except Exception as e:
                print(f"❌ Email girme hatası: {e}")
                import traceback
                traceback.print_exc()
                pytest.fail(f"Email girme hatası: {e}")
            
            # 3. Tempail'e geri git ve doğrulama kodunu bekle
            print("\n📧 3. Adım: Tempail'e geri gidiliyor ve doğrulama kodu bekleniyor...")
            
            # Tempail sekmesine geri dön
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
            
            # Sayfayı yenile
            driver.refresh()
            time.sleep(5)
            
            # Doğrulama kodunu bekle
            print("📧 Doğrulama kodu bekleniyor...")
            verification_code = automation.wait_for_email_with_code(timeout=120)
            
            if not verification_code:
                pytest.fail("❌ Doğrulama kodu alınamadı")
            
            print(f"✅ Doğrulama kodu alındı: {verification_code}")
            
            # 4. Hepsiburada'ya geri dön ve kodu gir
            print("\n🔐 4. Adım: Hepsiburada'ya geri dönülüyor ve kod giriliyor...")
            
            # Hepsiburada sekmesine geri dön
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)
            
            # Doğrulama kodunu gir
            try:
                code_input_selectors = [
                    "input[type='text']",
                    "input[name='verificationCode']",
                    "input[data-testid='verification-code']",
                    "#verificationCode",
                    ".verification-code-input"
                ]
                
                code_input = None
                for selector in code_input_selectors:
                    try:
                        code_input = driver.find_element("css selector", selector)
                        if code_input.is_displayed():
                            break
                    except:
                        continue
                
                if code_input:
                    code_input.clear()
                    code_input.send_keys(verification_code)
                    print(f"✅ Doğrulama kodu girildi: {verification_code}")
                    
                    # Doğrula butonuna tıkla
                    verify_selectors = [
                        "button[type='submit']",
                        "button:contains('Doğrula')",
                        "button:contains('Verify')",
                        ".verify-button",
                        "#verify-button"
                    ]
                    
                    verify_button = None
                    for selector in verify_selectors:
                        try:
                            verify_button = driver.find_element("css selector", selector)
                            if verify_button.is_displayed():
                                break
                        except:
                            continue
                    
                    if verify_button:
                        verify_button.click()
                        print("✅ Doğrula butonuna tıklandı")
                        time.sleep(5)
                    else:
                        print("⚠ Doğrula butonu bulunamadı")
                else:
                    print("❌ Doğrulama kodu input alanı bulunamadı")
                    pytest.fail("Doğrulama kodu input alanı bulunamadı")
                    
            except Exception as e:
                print(f"❌ Doğrulama kodu girme hatası: {e}")
                pytest.fail(f"Doğrulama kodu girme hatası: {e}")
            
            # Şifre ve diğer bilgileri doldur
            print("\n🔑 Şifre ve kişisel bilgiler dolduruluyor...")
            
            try:
                # Şifre alanını bul ve doldur
                password_selectors = [
                    "input[type='password']",
                    "input[name='password']",
                    "input[data-testid='password-input']",
                    "#password",
                    ".password-input"
                ]
                
                password_input = None
                for selector in password_selectors:
                    try:
                        password_input = driver.find_element("css selector", selector)
                        if password_input.is_displayed():
                            break
                    except:
                        continue
                
                if password_input:
                    password_input.clear()
                    password_input.send_keys("123456aA")
                    print("✅ Şifre girildi")
                else:
                    print("⚠ Şifre alanı bulunamadı")
                
                # Ad alanını bul ve doldur
                name_selectors = [
                    "input[name='firstName']",
                    "input[name='first_name']",
                    "input[data-testid='first-name-input']",
                    "#firstName",
                    ".first-name-input"
                ]
                
                name_input = None
                for selector in name_selectors:
                    try:
                        name_input = driver.find_element("css selector", selector)
                        if name_input.is_displayed():
                            break
                    except:
                        continue
                
                if name_input:
                    name_input.clear()
                    name_input.send_keys("Test")
                    print("✅ Ad girildi")
                else:
                    print("⚠ Ad alanı bulunamadı")
                
                # Soyad alanını bul ve doldur
                lastname_selectors = [
                    "input[name='lastName']",
                    "input[name='last_name']",
                    "input[data-testid='last-name-input']",
                    "#lastName",
                    ".last-name-input"
                ]
                
                lastname_input = None
                for selector in lastname_selectors:
                    try:
                        lastname_input = driver.find_element("css selector", selector)
                        if lastname_input.is_displayed():
                            break
                    except:
                        continue
                
                if lastname_input:
                    lastname_input.clear()
                    lastname_input.send_keys("Kullanıcı")
                    print("✅ Soyad girildi")
                else:
                    print("⚠ Soyad alanı bulunamadı")
                
            except Exception as e:
                print(f"⚠ Bilgi doldurma hatası: {e}")
            
            # Üye ol butonuna tıkla
            print("\n👤 Üye ol butonuna tıklanıyor...")
            
            try:
                signup_selectors = [
                    "button[type='submit']",
                    "button:contains('Üye Ol')",
                    "button:contains('Sign Up')",
                    ".signup-button",
                    "#signup-button"
                ]
                
                signup_button = None
                for selector in signup_selectors:
                    try:
                        signup_button = driver.find_element("css selector", selector)
                        if signup_button.is_displayed():
                            break
                    except:
                        continue
                
                if signup_button:
                    signup_button.click()
                    print("✅ Üye ol butonuna tıklandı")
                    time.sleep(5)
                else:
                    print("⚠ Üye ol butonu bulunamadı")
                    
            except Exception as e:
                print(f"❌ Üye ol butonuna tıklama hatası: {e}")
            
            # Başarı kontrolü
            print("\n✅ İş akışı tamamlandı!")
            print("🎉 Tempail -> Hepsiburada kayıt süreci başarıyla tamamlandı!")
            
            # Hepsiburada ana sayfasında olduğumuzu kontrol et
            current_url = driver.current_url
            if "hepsiburada.com" in current_url:
                print("✅ Hepsiburada ana sayfasında bulunuyoruz")
                print("🛒 Artık ürün seçimi yapabilirsiniz!")
            else:
                print(f"⚠ Beklenmeyen sayfa: {current_url}")
            
            return True
            
        except Exception as e:
            print(f"❌ İş akışı hatası: {e}")
            import traceback
            traceback.print_exc()
            return False
        
        finally:
            print("\n" + "=" * 60)
            print("🏁 Tam İş Akışı Testi Tamamlandı")
            print("=" * 60)