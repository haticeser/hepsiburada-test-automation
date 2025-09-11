# pages/modules/auth_module.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ..base_page import BasePage


class AuthModule(BasePage):
    """Kimlik doğrulama işlemleri için modül"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def check_registration_success(self):
        """Kayıt başarılı mı kontrol eder"""
        print("🔍 Kayıt başarısı kontrol ediliyor...")
        
        # Stabil kontrol yöntemleri
        stable_indicators = [
            # URL tabanlı
            lambda: "success" in self.driver.current_url.lower() or "welcome" in self.driver.current_url.lower(),
            # Sayfa başlığı tabanlı
            lambda: any(keyword in self.driver.title.lower() for keyword in ["hoş geldin", "welcome", "başarılı"]),
            # Form yokluğu tabanlı
            lambda: not self._is_registration_form_visible()
        ]
        
        for indicator in stable_indicators:
            try:
                if indicator():
                    print("✅ Kayıt başarılı")
                    return True
            except:
                continue
        
        print("❌ Kayıt başarısı doğrulanamadı")
        return False
    
    def _is_registration_form_visible(self):
        """Kayıt formu görünür mü kontrol eder"""
        try:
            form_selectors = ["form", "#registrationForm", ".registration-form"]
            for selector in form_selectors:
                try:
                    form = self.driver.find_element(By.CSS_SELECTOR, selector)
                    if form.is_displayed():
                        return True
                except:
                    continue
            return False
        except:
            return False
    
    def check_login_success(self):
        """Giriş başarılı mı kontrol eder"""
        print("🔍 Giriş başarısı kontrol ediliyor...")
        
        # Kullanıcı menüsü veya hesap bilgileri kontrolü
        user_indicators = [
            "[data-testid='account-menu-button']",
            ".account-user",
            ".user-menu",
            "[href*='hesabim']",
            ".profile-menu",
            ".user-profile",
            ".account-info"
        ]
        
        for selector in user_indicators:
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                if element.is_displayed():
                    print("✅ Giriş başarılı!")
                    return True
            except TimeoutException:
                continue
        
        # URL kontrolü
        current_url = self.driver.current_url
        if "hesabim" in current_url.lower() or "account" in current_url.lower():
            print("✅ Giriş başarılı (URL kontrolü)")
            return True
        
        print("❌ Giriş başarısı doğrulanamadı")
        return False
    
    def check_user_logged_in(self):
        """Kullanıcı giriş yapmış mı kontrol eder"""
        print("🔍 Kullanıcı giriş durumu kontrol ediliyor...")
        
        # Giriş yapmış kullanıcı göstergeleri
        logged_in_indicators = [
            ".user-name",
            ".account-name",
            "[data-testid*='user-name']",
            ".profile-name",
            ".welcome-user"
        ]
        
        for selector in logged_in_indicators:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector)
                if element.is_displayed():
                    user_name = element.text
                    print(f"✅ Kullanıcı giriş yapmış: {user_name}")
                    return True
            except:
                continue
        
        # Giriş yapmamış kullanıcı göstergeleri
        not_logged_in_indicators = [
            "a[href*='giris']",
            "a[href*='login']",
            ".login-button",
            ".sign-in-button"
        ]
        
        for selector in not_logged_in_indicators:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector)
                if element.is_displayed():
                    print("❌ Kullanıcı giriş yapmamış")
                    return False
            except:
                continue
        
        print("⚠️ Kullanıcı giriş durumu belirsiz")
        return False
    
    def logout_user(self):
        """Kullanıcıyı çıkış yapar"""
        print("🚪 Kullanıcı çıkış yapılıyor...")
        
        logout_selectors = [
            "a[href*='cikis']",
            "a[href*='logout']",
            ".logout-button",
            ".sign-out-button",
            "[data-testid*='logout']",
            "button[title*='Çıkış']",
            "button[title*='Logout']"
        ]
        
        for selector in logout_selectors:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                element.click()
                print("✅ Kullanıcı çıkış yaptı")
                time.sleep(2)
                return True
            except TimeoutException:
                continue
        
        print("❌ Çıkış butonu bulunamadı")
        return False
    
    def get_user_info(self):
        """Kullanıcı bilgilerini alır"""
        print("👤 Kullanıcı bilgileri alınıyor...")
        
        user_info = {}
        
        # Kullanıcı adı
        name_selectors = [
            ".user-name",
            ".account-name",
            "[data-testid*='user-name']",
            ".profile-name"
        ]
        
        for selector in name_selectors:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector)
                if element.is_displayed():
                    user_info['name'] = element.text
                    break
            except:
                continue
        
        # Email
        email_selectors = [
            ".user-email",
            ".account-email",
            "[data-testid*='user-email']",
            ".profile-email"
        ]
        
        for selector in email_selectors:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector)
                if element.is_displayed():
                    user_info['email'] = element.text
                    break
            except:
                continue
        
        if user_info:
            print(f"✅ Kullanıcı bilgileri: {user_info}")
        else:
            print("⚠️ Kullanıcı bilgileri alınamadı")
        
        return user_info
    
    def check_verification_required(self):
        """Doğrulama gerekli mi kontrol eder"""
        print("🔍 Doğrulama gereksinimi kontrol ediliyor...")
        
        verification_indicators = [
            "input[name*='verification']",
            "input[name*='code']",
            ".verification-code",
            "[data-testid*='verification']",
            ".otp-input",
            ".code-input"
        ]
        
        for selector in verification_indicators:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector)
                if element.is_displayed():
                    print("✅ Doğrulama kodu gerekli")
                    return True
            except:
                continue
        
        print("❌ Doğrulama kodu gerekli değil")
        return False
    
    def wait_for_verification_success(self, timeout=30):
        """Doğrulama başarısını bekler"""
        print(f"⏳ Doğrulama başarısı bekleniyor (timeout: {timeout}s)...")
        
        success_indicators = [
            ".verification-success",
            "[data-testid*='verification-success']",
            ".code-verified",
            ".verification-complete"
        ]
        
        for selector in success_indicators:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                if element.is_displayed():
                    print("✅ Doğrulama başarılı!")
                    return True
            except TimeoutException:
                continue
        
        print("❌ Doğrulama başarısı beklenemedi")
        return False
