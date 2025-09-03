# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Tüm sayfa sınıfları için temel sınıf"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
    def wait_for_element(self, locator, timeout=20):
        """Element görünene kadar bekler"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_clickable(self, locator, timeout=20):
        """Element tıklanabilir olana kadar bekler"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def click_element_safely(self, locator, timeout=20):
        """Element'e güvenli şekilde tıklar"""
        element = self.wait_for_clickable(locator, timeout)
        element.click()
        return element
    
    def send_keys_safely(self, locator, text, timeout=20):
        """Element'e güvenli şekilde text gönderir"""
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        return element
    
    def try_multiple_selectors(self, selectors, action="find", timeout=5, **kwargs):
        """Birden fazla selector dener, ilk başarılı olanı döner"""
        for selector in selectors:
            try:
                locator = (By.CSS_SELECTOR, selector)
                if action == "find":
                    return WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located(locator)
                    )
                elif action == "click":
                    element = WebDriverWait(self.driver, timeout).until(
                        EC.element_to_be_clickable(locator)
                    )
                    element.click()
                    return element
                elif action == "send_keys":
                    element = WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located(locator)
                    )
                    element.clear()
                    element.send_keys(kwargs.get('text', ''))
                    return element
            except TimeoutException:
                continue
        return None
    
    def close_cookie_popup(self):
        """Çerez popup'ını kapatmaya çalışır"""
        cookie_selectors = [
            "#onetrust-accept-btn-handler",
            ".consent-accept-all",
            "[data-testid='cookieAcceptAll']",
            ".cookie-accept"
        ]
        
        for selector in cookie_selectors:
            try:
                element = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                element.click()
                print(f"Cookie popup kapatıldı: {selector}")
                return True
            except TimeoutException:
                continue
        return False