# pages/login_page.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class LoginPage(BasePage):
    """Hepsiburada giriş sayfası için Page Object Model"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_email(self, email):
        """Email adresini girer"""
        print(f"📧 Email giriliyor: {email}")
        
        try:
            email_input = self.wait.until(EC.presence_of_element_located((By.ID, "txtUserName")))
            email_input.clear()
            email_input.send_keys(email)
            print(f"✅ Email girildi: {email}")
            return True
        except Exception as e:
            print(f"❌ Email girme hatası: {e}")
            return False
    
    def enter_password(self, password):
        """Şifreyi girer"""
        print("🔒 Şifre giriliyor...")
        
        try:
            password_input = self.wait.until(EC.presence_of_element_located((By.ID, "txtPassword")))
            password_input.clear()
            password_input.send_keys(password)
            print("✅ Şifre girildi")
            return True
        except Exception as e:
            print(f"❌ Şifre girme hatası: {e}")
            return False
    
    def click_login_button(self):
        """Giriş yap butonuna tıklar"""
        print("🔑 Giriş yap butonuna tıklanıyor...")
        
        try:
            submit_button = self.wait.until(EC.element_to_be_clickable((By.ID, "btnLogin")))
            submit_button.click()
            print("✅ Giriş formu gönderildi")
            time.sleep(1)  # 3s -> 1s
            return True
        except Exception as e:
            print(f"❌ Giriş butonuna tıklama hatası: {e}")
            return False
    
    def enter_verification_code(self, verification_code):
        """Doğrulama kodunu girer"""
        print(f"🔐 Giriş doğrulama kodu giriliyor: {verification_code}")
        
        try:
            # Doğrulama kodu gir
            code_input = self.wait.until(EC.presence_of_element_located((By.ID, "txtVerificationCode")))
            code_input.clear()
            code_input.send_keys(verification_code)
            print("✅ Doğrulama kodu girildi")
            return True
        except Exception as e:
            print(f"❌ Doğrulama kodu girme hatası: {e}")
            return False
    
    def click_verify_button(self):
        """Doğrula butonuna tıklar"""
        print("✅ Giriş doğrulama butonuna tıklanıyor...")
        
        try:
            verify_button = self.wait.until(EC.element_to_be_clickable((By.ID, "btnVerify")))
            verify_button.click()
            print("✅ Giriş doğrulama butonuna tıklandı")
            time.sleep(5)
            return True
        except Exception as e:
            print(f"❌ Doğrulama butonuna tıklama hatası: {e}")
            return False
    
    def enter_email_with_xpath(self, email):
        """XPath ile email adresini girer"""
        print(f"📧 Email giriliyor (XPath ile): {email}")
        
        try:
            # Önce sayfa yüklenmesini bekle
            print("⏳ Giriş sayfasının tam yüklenmesi bekleniyor...")
            time.sleep(5)
            
            # Farklı selector'ları dene
            email_selectors = [
                # Orijinal XPath
                "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/input",
                # ID ile
                "input#txtUserName",
                # Name ile
                "input[name='username']",
                # Placeholder ile
                "input[placeholder='E-posta adresi']",
                # Class ile
                "input[class*='hb-AxhBV']"
            ]
            
            email_input = None
            for selector in email_selectors:
                try:
                    print(f"🔍 Selector deneniyor: {selector}")
                    if selector.startswith("/"):
                        # XPath
                        email_input = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        # CSS Selector
                        email_input = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Email input bulundu: {selector}")
                    break
                except:
                    continue
            
            if not email_input:
                print("❌ Hiçbir email selector çalışmadı")
                return False
                
            email_input.clear()
            time.sleep(1)  # Clear işlemi için bekle
            email_input.send_keys(email)
            print(f"✅ Email girildi: {email}")
            return True
        except Exception as e:
            print(f"❌ Email girme hatası: {e}")
            return False
    
    def enter_password_with_xpath(self, password):
        """XPath ile şifreyi girer"""
        print("🔒 Şifre giriliyor (XPath ile)...")
        
        try:
            # Farklı selector'ları dene
            password_selectors = [
                # Orijinal XPath
                "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/form/div[2]/div/input",
                # ID ile
                "input#txtPassword",
                # Name ile
                "input[name='password']",
                # Placeholder ile
                "input[placeholder='Şifre']",
                # Type ile
                "input[type='password']"
            ]
            
            password_input = None
            for selector in password_selectors:
                try:
                    print(f"🔍 Password selector deneniyor: {selector}")
                    if selector.startswith("/"):
                        # XPath
                        password_input = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        # CSS Selector
                        password_input = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Password input bulundu: {selector}")
                    break
                except:
                    continue
            
            if not password_input:
                print("❌ Hiçbir password selector çalışmadı")
                return False
                
            password_input.clear()
            time.sleep(1)  # Clear işlemi için bekle
            password_input.send_keys(password)
            print("✅ Şifre girildi")
            return True
        except Exception as e:
            print(f"❌ Şifre girme hatası: {e}")
            return False
    
    def click_login_button_with_xpath(self):
        """XPath ile giriş yap butonuna tıklar"""
        print("🔑 Giriş yap butonuna tıklanıyor (XPath ile)...")
        
        try:
            # Farklı selector'ları dene
            login_selectors = [
                # Orijinal XPath
                "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/form/button[1]",
                # ID ile
                "button#btnLogin",
                # Name ile
                "button[name='btnLogin']",
                # Class ile
                "button[class*='hb-AxhfK']",
                # Text ile
                "button:contains('Giriş yap')"
            ]
            
            login_button = None
            for selector in login_selectors:
                try:
                    print(f"🔍 Login button selector deneniyor: {selector}")
                    if selector.startswith("/"):
                        # XPath
                        login_button = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        # CSS Selector
                        login_button = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Login button bulundu: {selector}")
                    break
                except:
                    continue
            
            if not login_button:
                print("❌ Hiçbir login button selector çalışmadı")
                return False
                
            # JavaScript ile tıklama - daha güvenilir
            self.driver.execute_script("arguments[0].click();", login_button)
            print("✅ Giriş formu gönderildi")
            time.sleep(3)
            return True
        except Exception as e:
            print(f"❌ Giriş butonuna tıklama hatası: {e}")
            return False
    
    def login_with_xpath(self, email="viva.vista000@gmail.com", password="123456aA"):
        """XPath'lerle tam giriş işlemi yapar"""
        print("🔑 XPath ile giriş işlemi başlatılıyor...")
        print(f"📧 Email: {email}")
        print(f"🔒 Şifre: {password}")
        
        try:
            # 1. Email gir
            if not self.enter_email_with_xpath(email):
                return False
            
            # 2. Şifre gir
            if not self.enter_password_with_xpath(password):
                return False
            
            # 3. Giriş yap butonuna tıkla
            if not self.click_login_button_with_xpath():
                return False
            
            print("✅ XPath ile giriş işlemi tamamlandı")
            return True
            
        except Exception as e:
            print(f"❌ XPath ile giriş işlemi hatası: {e}")
            return False