# pages/modules/navigation_module.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ..base_page import BasePage


class NavigationModule(BasePage):
    """Navigasyon işlemleri için modül"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.hepsiburada.com"
    
    def go_to_hepsiburada(self):
        """Hepsiburada ana sayfasına gider - Hızlı versiyon"""
        print("🏠 Hepsiburada ana sayfasına gidiliyor...")
        self.driver.get(self.base_url)
        time.sleep(1)  # 3s -> 1s
        
        # Çerez popup'ını kapat
        self.close_cookie_popup()
        time.sleep(0.5)  # 2s -> 0.5s
        
        print("✅ Hepsiburada ana sayfası yüklendi")
        return True
    
    def navigate_to_login_with_specific_xpath(self):
        """Belirli XPath'lerle giriş sayfasına yönlendirir"""
        print("🔑 Giriş sayfasına yönlendiriliyor (XPath ile)...")
        
        try:
            # 1. Giriş Yap butonunun üzerine gel (hover)
            print("🔍 Giriş Yap butonu aranıyor...")
            login_button_xpath = "/html/body/div[1]/section[3]/div/div[4]/div/div/div/div[1]/div[2]/div[3]/div[2]"
            
            try:
                login_button = WebDriverWait(self.driver, 5).until(  # 10s -> 5s
                    EC.presence_of_element_located((By.XPATH, login_button_xpath))
                )
                print("✅ Giriş Yap butonu bulundu")
                
                # Hover yap
                actions = ActionChains(self.driver)
                actions.move_to_element(login_button).perform()
                print("✅ Giriş Yap butonuna hover yapıldı")
                time.sleep(1)  # 3s -> 1s
                
                # 2. Submenüden Giriş Yap'a tıkla - ID ile daha güvenilir
                print("🔍 Submenüde Giriş Yap linki aranıyor (ID ile)...")
                
                try:
                    # Sayfa yüklenmesini bekle
                    time.sleep(0.5)  # 2s -> 0.5s
                    
                    # ID ile Giriş Yap linkini bul
                    submenu_login = WebDriverWait(self.driver, 5).until(  # 10s -> 5s
                        EC.element_to_be_clickable((By.ID, "login"))
                    )
                    # JavaScript ile tıklama - daha güvenilir
                    self.driver.execute_script("arguments[0].click();", submenu_login)
                    print("✅ Submenüden Giriş Yap'a tıklandı (ID: login)")
                    time.sleep(1)  # 3s -> 1s
                    return True
                    
                except TimeoutException:
                    print("❌ Submenüde Giriş Yap linki bulunamadı (ID: login)")
                    return False
                    
            except TimeoutException:
                print("❌ Giriş Yap butonu bulunamadı")
                return False
                
        except Exception as e:
            print(f"❌ Giriş sayfası yönlendirme hatası: {e}")
            return False
    
    def navigate_to_registration(self):
        """Kayıt sayfasına yönlendirir"""
        print("📝 Kayıt sayfasına yönlendiriliyor...")
        
        try:
            # Giriş yap butonunu bul ve hover yap
            print("🔍 Giriş yap butonu aranıyor...")
            login_selectors = [
                "#myAccount",
                "#myAccount span[data-test-id='account']",
                "#myAccount span[title='Giriş Yap']",
                "[data-testid='account']",
                "[data-test-id='account']",
                "[data-testid='account-menu-button']",
                ".account-user",
                "a[href*='giris']",
                ".login-button",
                "a[href*='login']"
            ]
            
            # XPath ile text içeriğine göre arama
            login_xpath_selectors = [
                "//button[contains(text(), 'Giriş')]",
                "//a[contains(text(), 'Giriş')]"
            ]
            
            login_button = None
            for selector in login_selectors:
                try:
                    login_button = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    if login_button.is_displayed():
                        print(f"✅ Giriş butonu bulundu: {selector}")
                        break
                except:
                    continue
            
            # XPath selector'larını dene
            if not login_button:
                for xpath in login_xpath_selectors:
                    try:
                        login_button = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, xpath))
                        )
                        if login_button.is_displayed():
                            print(f"✅ Giriş butonu bulundu (XPath): {xpath}")
                            break
                    except:
                        continue
            
            if login_button:
                # Hover yap
                actions = ActionChains(self.driver)
                actions.move_to_element(login_button).perform()
                print("✅ Giriş butonuna hover yapıldı")
                time.sleep(3)  # Submenünün açılması için daha uzun bekle
                
                # Hover sonrası açılan submenüde üye ol linkini ara
                return self._find_and_click_register_link()
            else:
                print("❌ Giriş butonu bulunamadı")
                return False
        
        except Exception as e:
            print(f"❌ Kayıt sayfası yönlendirme hatası: {e}")
        
        print("❌ Kayıt sayfasına yönlendirilemedi")
        return False
    
    def navigate_to_login(self):
        """Giriş sayfasına yönlendirir"""
        print("🔑 Giriş sayfasına yönlendiriliyor...")
        
        try:
            # Giriş yap butonunu bul ve hover yap
            print("🔍 Giriş yap butonu aranıyor...")
            login_selectors = [
                "#myAccount",
                "#myAccount span[title='Giriş Yap']",
                "span[title='Giriş Yap']",
                "#myAccount span",
                "[data-testid='account']",
                "[data-test-id='account']",
                "[data-testid='account-menu-button']",
                ".account-user",
                "a[href*='giris']",
                ".login-button",
                "a[href*='login']"
            ]
            
            # XPath ile text içeriğine göre arama
            login_xpath_selectors = [
                "//span[contains(text(), 'Giriş Yap')]",
                "//*[contains(text(), 'Giriş Yap')]",
                "//button[contains(text(), 'Giriş')]",
                "//a[contains(text(), 'Giriş')]",
                "//a[contains(text(), 'Giriş Yap')]",
                "//button[contains(text(), 'Giriş Yap')]"
            ]
            
            login_button = None
            for selector in login_selectors:
                try:
                    login_button = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    if login_button.is_displayed():
                        print(f"✅ Giriş butonu bulundu: {selector}")
                        break
                except:
                    continue
            
            # XPath selector'larını dene
            if not login_button:
                for xpath in login_xpath_selectors:
                    try:
                        login_button = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, xpath))
                        )
                        if login_button.is_displayed():
                            print(f"✅ Giriş butonu bulundu (XPath): {xpath}")
                            break
                    except:
                        continue
            
            if login_button:
                # Hover yap
                actions = ActionChains(self.driver)
                actions.move_to_element(login_button).perform()
                print("✅ Giriş butonuna hover yapıldı")
                time.sleep(3)  # Submenünün açılması için bekle
                
                # Hover sonrası açılan submenüde giriş yap linkini ara
                return self._find_and_click_login_link()
            else:
                print("❌ Giriş butonu bulunamadı")
                return False
        
        except Exception as e:
            print(f"❌ Giriş sayfası yönlendirme hatası: {e}")
        
        print("❌ Giriş sayfasına yönlendirilemedi")
        return False
    
    def _find_and_click_login_link(self):
        """Giriş yap linkini bulur ve tıklar"""
        print("🔍 Submenüde giriş yap linki aranıyor...")
        submenu_selectors = [
            "#login",
            "a[id='login']",
            "a[title='Giriş Yap']",
            "a[href*='giris']",
            "a[href*='login']",
            "a[href*='uyelik/giris']",
            ".login-button",
            "[data-testid*='login']",
            ".dropdown-menu a[href*='giris']",
            ".dropdown a[href*='login']",
            "#myAccount a[href*='giris']"
        ]
        
        # XPath ile text içeriğine göre arama
        submenu_xpath_selectors = [
            "//a[contains(text(), 'Giriş Yap')]",
            "//a[contains(text(), 'Giriş')]",
            "//button[contains(text(), 'Giriş Yap')]",
            "//button[contains(text(), 'Giriş')]",
            "//div[@class='menu-item']//a[contains(text(), 'Giriş Yap')]",
            "//div[@class='dropdown-item']//a[contains(text(), 'Giriş')]",
            "//div[@id='myAccount']//a[contains(text(), 'Giriş Yap')]"
        ]
        
        for selector in submenu_selectors:
            try:
                submenu_link = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                if submenu_link.is_displayed():
                    submenu_link.click()
                    print(f"✅ Submenüden giriş sayfasına yönlendirildi: {selector}")
                    time.sleep(3)
                    return True
            except:
                continue
        
        # XPath selector'larını dene
        for xpath in submenu_xpath_selectors:
            try:
                submenu_link = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                if submenu_link.is_displayed():
                    submenu_link.click()
                    print(f"✅ Submenüden giriş sayfasına yönlendirildi (XPath): {xpath}")
                    time.sleep(3)
                    return True
            except:
                continue
        
        # Eğer submenü linkleri bulunamazsa, text içeriğine göre arama yap
        print("🔍 Text içeriğine göre giriş yap linki aranıyor...")
        try:
            all_links = self.driver.find_elements(By.TAG_NAME, "a")
            for link in all_links:
                try:
                    link_text = link.text.lower()
                    if ("giriş yap" in link_text or "giriş" in link_text or "login" in link_text) and link.is_displayed():
                        link.click()
                        print(f"✅ Text ile giriş yap linki bulundu ve tıklandı: {link.text}")
                        time.sleep(3)
                        return True
                except:
                    continue
        except:
            pass
        
        return False
    
    def _find_and_click_register_link(self):
        """Üye ol linkini bulur ve tıklar"""
        print("🔍 Submenüde üye ol linki aranıyor...")
        submenu_selectors = [
            "#register",
            "a[id='register']",
            "a[title='Hesap oluştur']",
            "a[href*='uyelik/yeni-uye']",
            "a[href*='uyelik']",
            "a[href*='register']", 
            "a[href*='uye-ol']",
            ".register-button",
            "[data-testid*='register']",
            ".dropdown-menu a[href*='uyelik']",
            ".dropdown a[href*='register']",
            "#myAccount a[href*='uyelik']"
        ]
        
        # XPath ile text içeriğine göre arama
        submenu_xpath_selectors = [
            "//a[contains(text(), 'Üye Ol')]",
            "//a[contains(text(), 'Kayıt Ol')]",
            "//button[contains(text(), 'Üye Ol')]",
            "//button[contains(text(), 'Kayıt Ol')]",
            "//div[@class='menu-item']//a[contains(text(), 'Üye Ol')]",
            "//div[@class='dropdown-item']//a[contains(text(), 'Kayıt Ol')]",
            "//div[@id='myAccount']//a[contains(text(), 'Üye Ol')]"
        ]
        
        for selector in submenu_selectors:
            try:
                submenu_link = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                if submenu_link.is_displayed():
                    submenu_link.click()
                    print(f"✅ Submenüden kayıt sayfasına yönlendirildi: {selector}")
                    time.sleep(3)
                    return True
            except:
                continue
        
        # XPath selector'larını dene
        for xpath in submenu_xpath_selectors:
            try:
                submenu_link = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                if submenu_link.is_displayed():
                    submenu_link.click()
                    print(f"✅ Submenüden kayıt sayfasına yönlendirildi (XPath): {xpath}")
                    time.sleep(3)
                    return True
            except:
                continue
        
        # Eğer submenü linkleri bulunamazsa, text içeriğine göre arama yap
        print("🔍 Text içeriğine göre üye ol linki aranıyor...")
        try:
            all_links = self.driver.find_elements(By.TAG_NAME, "a")
            for link in all_links:
                try:
                    link_text = link.text.lower()
                    if ("üye ol" in link_text or "kayıt ol" in link_text or "register" in link_text) and link.is_displayed():
                        link.click()
                        print(f"✅ Text ile üye ol linki bulundu ve tıklandı: {link.text}")
                        time.sleep(3)
                        return True
                except:
                    continue
        except:
            pass
        
        return False
