# pages/tempail_page.py
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class TempailPage(BasePage):
    """Tempail.com sayfası için Page Object Model"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.temp_email = None
    
    def get_temp_email(self):
        """Tempail.com'dan geçici email adresi alır"""
        print("🌐 Tempail.com'a gidiliyor...")
        print("📱 Yeni sekmede açılıyor...")
        self.driver.get("https://tempail.com/")
        time.sleep(5)
        
        try:
            # Email adresini al - farklı selector'ları dene
            email_selectors = [
                "#eposta_adres",
                "input[type='text'][readonly]",
                ".email-address",
                "input[value*='@']"
            ]
            
            email_input = None
            for selector in email_selectors:
                try:
                    email_input = self.wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    break
                except:
                    continue
            
            if email_input:
                self.temp_email = email_input.get_attribute("value")
                print(f"✅ Geçici email alındı: {self.temp_email}")
                return self.temp_email
            else:
                print("❌ Email input bulunamadı")
                return None
                
        except Exception as e:
            print(f"❌ Tempail'den email alınamadı: {e}")
            return None
    
    def wait_for_email_with_code(self, timeout=120):
        """Belirtilen süre boyunca doğrulama kodu içeren email bekler"""
        print(f"📧 Doğrulama kodu bekleniyor... (max {timeout} saniye)")
        print("🔍 Hepsiburada'dan gelen doğrulama emaili aranıyor...")
        
        start_time = time.time()
        attempts = 0
        
        while time.time() - start_time < timeout:
            try:
                attempts += 1
                print(f"🔄 Deneme {attempts}: Email kontrol ediliyor...")
                
                # Sayfayı yenile
                self.driver.refresh()
                time.sleep(5)  # Daha kısa bekleme
                
                # Sayfayı aşağı kaydır - mailleri görmek için
                print("📜 Sayfa aşağı kaydırılıyor...")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                
                # Sayfayı yukarı da kaydır
                self.driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(2)
                
                # Email listesini bul - önce Hepsiburada emailini ara
                print("🔍 Hepsiburada emaili aranıyor...")
                
                # Önce sayfadaki tüm email linklerini bul
                all_email_links = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='mail_']")
                print(f"📧 Toplam {len(all_email_links)} email linki bulundu")
                
                # Hepsiburada emailini bul
                hepsiburada_email_link = None
                for i, link in enumerate(all_email_links[:5]):  # İlk 5 emaili kontrol et
                    try:
                        href = link.get_attribute("href")
                        text = link.text.strip()
                        print(f"  📧 Email {i+1}: {text} - {href}")
                        
                        # Hepsiburada ile ilgili email mi kontrol et - daha spesifik arama
                        if any(keyword in text.lower() for keyword in [
                            'hepsiburada', 'hepsipay', 'doğrulama', 'verification', 
                            'kod', 'code', 'üyelik', 'membership', 'newsletter.hepsiburada'
                        ]):
                            hepsiburada_email_link = link
                            print(f"✅ Hepsiburada emaili bulundu: {text}")
                            break
                        
                        # Email içeriğinde de ara
                        try:
                            # Email linkinin içindeki text'leri kontrol et
                            email_elements = link.find_elements(By.CSS_SELECTOR, "div")
                            for element in email_elements:
                                element_text = element.text.strip().lower()
                                if any(keyword in element_text for keyword in [
                                    'hepsiburada', 'hepsipay', 'doğrulama', 'verification',
                                    'üyelik', 'membership', 'newsletter'
                                ]):
                                    hepsiburada_email_link = link
                                    print(f"✅ Hepsiburada emaili bulundu (içerikte): {element_text}")
                                    break
                            if hepsiburada_email_link:
                                break
                        except:
                            continue
                            
                    except Exception as e:
                        print(f"⚠ Email {i+1} kontrol hatası: {e}")
                        continue
                
                # Eğer Hepsiburada emaili bulunamazsa, ilk emaili kullan
                if not hepsiburada_email_link and all_email_links:
                    hepsiburada_email_link = all_email_links[0]
                    print("⚠ Hepsiburada emaili bulunamadı, ilk email kullanılıyor")
                
                email_link = hepsiburada_email_link
                
                if email_link:
                    try:
                        # Email'e tıkla
                        print("📧 Email açılıyor...")
                        email_link.click()
                        time.sleep(8)  # Daha uzun bekleme
                        
                        # Email içeriğini kontrol et
                        print("📖 Email içeriği okunuyor...")
                        
                        # Önce iframe var mı kontrol et
                        try:
                            iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe#iframe")
                            print("✅ Iframe bulundu, içine geçiliyor...")
                            self.driver.switch_to.frame(iframe)
                            time.sleep(3)
                            
                            # Iframe içinde doğrulama kodunu ara
                            print("🔍 Iframe içinde doğrulama kodu aranıyor...")
                            
                            # Görünür text'te 6 haneli kod ara
                            visible_text = self.driver.find_element(By.TAG_NAME, "body").text
                            print(f"📧 Görünür text uzunluğu: {len(visible_text)} karakter")
                            print(f"📧 Text içeriği (ilk 200 karakter): {visible_text[:200]}...")
                            
                            # 6 haneli kodu bul - Hepsiburada için özel
                            code_patterns = [
                                r'\b\d{6}\b',  # 6 haneli sayı
                                r'kod[:\s]*(\d{6})',  # "kod: 123456" formatı
                                r'code[:\s]*(\d{6})',  # "code: 123456" formatı
                                r'doğrulama[:\s]*(\d{6})',  # "doğrulama: 123456" formatı
                                r'verification[:\s]*(\d{6})',  # "verification: 123456" formatı
                                r'üyelik[:\s]*(\d{6})',  # "üyelik: 123456" formatı
                                r'membership[:\s]*(\d{6})',  # "membership: 123456" formatı
                                r'(\d{6})',  # Sadece 6 haneli sayı
                            ]
                            
                            print("🔍 Hepsiburada doğrulama kodu aranıyor...")
                            
                            for pattern in code_patterns:
                                matches = re.findall(pattern, visible_text, re.IGNORECASE)
                                if matches:
                                    verification_code = matches[0]
                                    if len(verification_code) == 6 and verification_code.isdigit():
                                        print(f"✅ Iframe'de doğrulama kodu bulundu: {verification_code}")
                                        self.driver.switch_to.default_content()
                                        return verification_code
                            
                            # Iframe'den çık
                            self.driver.switch_to.default_content()
                            print("⚠ Iframe'de kod bulunamadı")
                            
                        except Exception as e:
                            print(f"⚠ Iframe hatası: {e}")
                        
                        # Ana sayfada da ara
                        page_source = self.driver.page_source
                        print("🔍 Ana sayfada doğrulama kodu aranıyor...")
                        print(f"📧 Sayfa kaynak kodu uzunluğu: {len(page_source)} karakter")
                        
                        # 6 haneli kodu bul
                        for pattern in code_patterns:
                            matches = re.findall(pattern, page_source, re.IGNORECASE)
                            if matches:
                                verification_code = matches[0]
                                if len(verification_code) == 6 and verification_code.isdigit():
                                    print(f"✅ Ana sayfada doğrulama kodu bulundu: {verification_code}")
                                    return verification_code
                        
                        # Debug: Sayfadaki tüm sayıları listele
                        all_numbers = re.findall(r'\d+', page_source)
                        six_digit_numbers = [num for num in all_numbers if len(num) == 6]
                        if six_digit_numbers:
                            print(f"🔍 Sayfada bulunan 6 haneli sayılar: {six_digit_numbers}")
                        
                        print("⚠ Doğrulama kodu bulunamadı")
                        
                    except Exception as e:
                        print(f"⚠ Email okuma hatası: {e}")
                        continue
                else:
                    print("📧 Henüz email bulunamadı, bekleniyor...")
                
                # 10 saniye bekle
                time.sleep(10)
                
            except Exception as e:
                print(f"⏳ Email kontrol hatası: {e}")
                time.sleep(10)
        
        print("❌ Doğrulama kodu bulunamadı!")
        return None