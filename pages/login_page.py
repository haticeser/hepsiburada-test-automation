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
            time.sleep(3)
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