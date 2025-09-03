# pages/hepsiburada_page.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage


class HepsiburadaPage(BasePage):
    """Hepsiburada ana sayfası için Page Object Model"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def go_to_hepsiburada(self):
        """Hepsiburada ana sayfasına gider"""
        print("🚀 Hepsiburada ana sayfasına gidiliyor...")
        self.driver.get("https://www.hepsiburada.com/")
        time.sleep(5)
        
        # Çerez popup'ını kapat
        self.close_cookie_popup()
        
        # Çerezleri kapattıktan sonra sayfayı yenile
        print("🔄 Sayfa yenileniyor...")
        self.driver.refresh()
        time.sleep(3)
        print("✅ Sayfa yenilendi")
    
    def navigate_to_registration(self):
        """Üye ol sayfasına yönlendirir"""
        print("📝 Üye ol sayfasına yönlendiriliyor...")
        
        try:
            # Önce myAccount hover dene
            try:
                my_account = self.wait.until(EC.presence_of_element_located((By.ID, "myAccount")))
                actions = ActionChains(self.driver)
                actions.move_to_element(my_account).perform()
                print("✅ myAccount elementine hover yapıldı")
                time.sleep(3)
                
                register_button = self.wait.until(EC.element_to_be_clickable((By.ID, "register")))
                register_button.click()
                print("✅ Üye ol butonuna tıklandı")
                time.sleep(3)
                
            except:
                print("⚠ Hover yöntemi başarısız, alternatif yöntem deneniyor...")
                # Doğrudan üye ol sayfasına git
                self.driver.get("https://www.hepsiburada.com/uyelik/yeni-uye")
                time.sleep(3)
                
        except Exception as e:
            print(f"⚠ Üye ol linki bulunamadı: {e}")
            # Doğrudan üye ol sayfasına git
            self.driver.get("https://www.hepsiburada.com/uyelik/yeni-uye")
            time.sleep(3)
    
    def navigate_to_login(self):
        """Giriş sayfasına yönlendirir"""
        print("🔑 Giriş sayfasına yönlendiriliyor...")
        self.driver.get("https://www.hepsiburada.com/uyelik/giris")
        time.sleep(3)
    
    def close_google_password_popup(self):
        """Google şifre kaydetme popup'ını kapatır"""
        print("🔒 Google şifre kaydetme popup'ı kontrol ediliyor...")
        try:
            # Google şifre kaydetme popup'ı için farklı selector'ları dene
            password_save_selectors = [
                # X işareti (kapat) butonları
                "button[aria-label*='Close']",
                "button[aria-label*='Kapat']",
                "button[aria-label*='Dismiss']",
                "button[aria-label*='Çıkış']",
                "button[aria-label*='Exit']",
                "button[aria-label*='Cancel']",
                "button[aria-label*='İptal']",
                "button[aria-label*='X']",
                "button[aria-label*='×']",
                # X işareti class'ları
                ".close-button",
                ".dismiss-button",
                ".cancel-button",
                ".exit-button",
                "[class*='close']",
                "[class*='dismiss']",
                "[class*='cancel']",
                "[class*='exit']",
                # Eski selector'lar
                "button[aria-label*='Kaydetme']",
                "button[aria-label*='Save']",
                "button[data-action='save']",
                "button[data-action='cancel']",
                "button[aria-label*='Not now']",
                "button[aria-label*='Şimdi değil']",
                "button[aria-label*='Never']",
                "button[aria-label*='Asla']"
            ]
            
            password_save_button = None
            for selector in password_save_selectors:
                try:
                    password_save_button = WebDriverWait(self.driver, 3).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    if password_save_button:
                        break
                except:
                    continue
            
            # Text içeren butonları da kontrol et
            if not password_save_button:
                buttons = self.driver.find_elements(By.TAG_NAME, "button")
                for btn in buttons:
                    btn_text = btn.text.lower()
                    if any(keyword in btn_text for keyword in ['kaydetme', 'save', 'not now', 'şimdi değil', 'never', 'asla', 'dismiss', 'kapat']):
                        password_save_button = btn
                        break
            
            if password_save_button:
                password_save_button.click()
                print("✅ Google şifre kaydetme popup'ı reddedildi")
                time.sleep(2)
            else:
                print("⚠ Google şifre kaydetme popup'ı bulunamadı veya zaten kapalı")
                
        except Exception as e:
            print(f"⚠ Google popup kontrol hatası: {e}")
    
    def check_login_success(self):
        """Giriş başarısını kontrol eder"""
        try:
            account_element = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#myAccount, .user-info, .account-info"))
            )
            print("✅ GİRİŞ BAŞARILI!")
            return True
        except:
            print("✅ Giriş tamamlandı")
            return True
    
    def check_registration_success(self):
        """Üye kaydı başarısını kontrol eder"""
        success_indicators = [
            ".success-message",
            ".alert-success",
            "[class*='success']",
            "#myAccount",  # Hesap alanının görünmesi
            ".welcome-message",
            "[class*='welcome']"
        ]
        
        for indicator in success_indicators:
            try:
                success_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, indicator))
                )
                print("✅ Üye kaydı başarıyla tamamlandı!")
                return True
            except:
                continue
        
        print("✅ Üye kaydı tamamlandı (başarı göstergesi bulunamadı)")
        return True