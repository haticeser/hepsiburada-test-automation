# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Tüm sayfa sınıfları için temel sınıf"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)  # 20s -> 5s
    
    def wait_for_element(self, locator, timeout=5):
        """Element görünene kadar bekler"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_clickable(self, locator, timeout=5):
        """Element tıklanabilir olana kadar bekler"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def click_element_safely(self, locator, timeout=5):
        """Element'e güvenli şekilde tıklar"""
        element = self.wait_for_clickable(locator, timeout)
        element.click()
        return element
    
    def send_keys_safely(self, locator, text, timeout=5):
        """Element'e güvenli şekilde text gönderir"""
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        return element
    
    def try_multiple_selectors(self, selectors, action="find", timeout=3, by_type=By.CSS_SELECTOR, **kwargs):
        """Birden fazla selector dener, ilk başarılı olanı döner - Optimize edilmiş versiyon"""
        for i, selector in enumerate(selectors):
            # İlk selector için daha uzun, sonrakiler için kısa timeout
            # Bu sayede en yaygın selector'lar önce denenir
            current_timeout = timeout if i == 0 else 1
            
            try:
                locator = (by_type, selector)
                if action == "find":
                    element = WebDriverWait(self.driver, current_timeout).until(
                        EC.presence_of_element_located(locator)
                    )
                    print(f"✅ Element bulundu: {selector} (timeout: {current_timeout}s)")
                    return element
                elif action == "click":
                    element = WebDriverWait(self.driver, current_timeout).until(
                        EC.element_to_be_clickable(locator)
                    )
                    element.click()
                    print(f"✅ Element tıklandı: {selector} (timeout: {current_timeout}s)")
                    return element
                elif action == "send_keys":
                    element = WebDriverWait(self.driver, current_timeout).until(
                        EC.presence_of_element_located(locator)
                    )
                    element.clear()
                    element.send_keys(kwargs.get('text', ''))
                    print(f"✅ Text gönderildi: {selector} (timeout: {current_timeout}s)")
                    return element
            except TimeoutException:
                print(f"⏳ Selector başarısız: {selector} (timeout: {current_timeout}s)")
                continue
        print(f"❌ Hiçbir selector başarılı olmadı: {len(selectors)} selector denendi")
        return None
    
    def find_element_by_stable_attributes(self, tag_name, attributes, timeout=5):
        """Stabil attribute'lara göre element bulur"""
        print(f"🔍 Stabil attribute ile element aranıyor: {tag_name}")
        
        for attr_name, attr_values in attributes.items():
            for attr_value in attr_values:
                try:
                    selector = f"{tag_name}[{attr_name}*='{attr_value}']"
                    element = WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Stabil element bulundu: {selector}")
                    return element
                except TimeoutException:
                    continue
        return None
    
    def find_element_by_text_content(self, text_keywords, tag_name="*", timeout=5):
        """Text içeriğine göre element bulur"""
        print(f"🔍 Text içeriğine göre element aranıyor: {text_keywords}")
        
        try:
            # XPath ile text içeriğine göre arama
            for keyword in text_keywords:
                xpath = f"//{tag_name}[contains(text(), '{keyword}')]"
                try:
                    element = WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    print(f"✅ Text ile element bulundu: {keyword}")
                    return element
                except TimeoutException:
                    continue
        except:
            pass
        return None
    
    def wait_for_any_element(self, selectors, timeout=10):
        """Herhangi bir element görünene kadar bekler (hızlı)"""
        print(f"⚡ Herhangi bir element bekleniyor: {len(selectors)} selector")
        
        for selector in selectors:
            try:
                element = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                print(f"⚡ Hızlı element bulundu: {selector}")
                return element
            except TimeoutException:
                continue
        return None
    
    def find_element_fast(self, selectors, by_type=By.CSS_SELECTOR):
        """Hızlı element bulma - Sadece 1 saniye timeout ile"""
        for selector in selectors:
            try:
                locator = (by_type, selector)
                element = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located(locator)
                )
                print(f"⚡ Hızlı element bulundu: {selector}")
                return element
            except TimeoutException:
                continue
        return None
    
    def close_cookie_popup(self):
        """Çerez popup'ını kapatmaya çalışır - Hızlı versiyon"""
        cookie_selectors = [
            "#onetrust-accept-btn-handler",
            ".consent-accept-all",
            "[data-testid='cookieAcceptAll']",
            ".cookie-accept"
        ]
        
        for selector in cookie_selectors:
            try:
                element = WebDriverWait(self.driver, 1).until(  # 3s -> 1s
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                element.click()
                print(f"Cookie popup kapatıldı: {selector}")
                return True
            except TimeoutException:
                continue
        return False
    
    def close_google_password_popup(self):
        """Google şifre kaydetme popup'ını kapatır"""
        try:
            # Google şifre kaydetme popup'ını kapat
            google_popup_selectors = [
                "button[aria-label='Kaydetme']",
                "button[aria-label='Save']",
                ".google-password-save",
                "[class*='google-password']",
                "button[data-testid*='save']",
                "button[data-testid*='password']",
                "button[aria-label*='Kaydet']",
                "button[aria-label*='Save']"
            ]
            
            for selector in google_popup_selectors:
                try:
                    google_button = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    if google_button.is_displayed():
                        google_button.click()
                        print(f"Google şifre popup kapatıldı: {selector}")
                        return True
                except TimeoutException:
                    continue
        except:
            pass
        return False