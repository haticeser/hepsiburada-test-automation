# pages/modules/product_module.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ..base_page import BasePage


class ProductModule(BasePage):
    """Ürün seçimi işlemleri için modül"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    
    def select_laptop_product(self, debug_mode=False, force_hover=True):
        """Dizüstü bilgisayar kategorisini seçer - Hover Focused"""
        print("💻 Dizüstü bilgisayar kategorisi seçiliyor...")
        
        try:
            if force_hover:
                # SADECE HOVER YÖNTEMİNİ KULLAN
                print("🖱️ Hover navigasyon yöntemi başlatılıyor...")
                return self._hover_navigation_method()
            else:
                # 1. ÖNCE DOĞRUDAN ARAMA YAP (Hızlı yöntem)
                laptop_found = self._quick_laptop_search()
                if laptop_found:
                    return True
                
                # 2. EĞER ARAMA BAŞARISIZSA, HOVER YÖNTEMİNİ DENE
                print("🔍 Hızlı arama başarısız, hover yöntemi deneniyor...")
                return self._hover_navigation_method()
                
        except Exception as e:
            print(f"❌ Dizüstü bilgisayar seçimi hatası: {e}")
            return False
    
    def _quick_laptop_search(self):
        """Hızlı laptop arama - Disabled for Hover Mode"""
        print("⚡ Hızlı laptop arama devre dışı - Hover modu aktif")
        return False  # Hover modu için devre dışı

    
    def _hover_navigation_method(self):
        """Hover navigasyon yöntemi - Step by Step Visual Navigation"""
        print("🖱️ Hover navigasyon yöntemi başlatılıyor...")
        print("📋 Adım 1: Elektronik menüsü bulunuyor...")
        
        # Elektronik menüsünü bul
        elektronik_menu = self.find_elektronik_menu_optimized()
        if not elektronik_menu:
            print("❌ Elektronik menüsü bulunamadı")
            return False
        
        print("✅ Elektronik menüsü bulundu!")
        
        # Elemente scroll yaparak görünür hale getir
        print("📜 Elektronik menüsüne scroll yapılıyor...")
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", elektronik_menu)
        print("⏳ Scroll animasyonu için 1 saniye bekleniyor...")
        time.sleep(1)  # Kısa bekleme
        
        print("📋 Adım 2: Elektronik menüsüne hover yapılıyor...")
        # Elektronik menüsüne hover yap
        actions = ActionChains(self.driver)
        
        # Hover işlemi
        print("🖱️ Elektronik menüsüne hover yapılıyor...")
        actions.move_to_element(elektronik_menu).perform()
        print("✅ Elektronik menüsüne hover yapıldı")
        
        # Submenu'nun açılması için kısa bekleme
        print("⏳ Submenu'nun açılması bekleniyor...")
        time.sleep(2)  # Kısa bekleme
        
        # Submenu'nun açıldığını kontrol et
        try:
            submenu_elements = self.driver.find_elements(By.CSS_SELECTOR, ".submenu, .dropdown-menu, [class*='submenu'], [class*='dropdown']")
            if submenu_elements:
                print("✅ Submenu açıldı!")
            else:
                print("⚠️ Submenu açılmadı, devam ediliyor...")
        except:
            print("⚠️ Submenu kontrolü başarısız, devam ediliyor...")
        
        print("📋 Adım 3: Bilgisayar alt menüsü aranıyor...")
        # Bilgisayar alt menüsünü bul
        bilgisayar_menu = self.find_bilgisayar_submenu_optimized()
        if not bilgisayar_menu:
            print("❌ Bilgisayar alt menüsü bulunamadı")
            return False
        
        print("✅ Bilgisayar alt menüsü bulundu!")
        
        print("📋 Adım 4: Bilgisayar menüsüne hover yapılıyor...")
        # Bilgisayar menüsüne hover
        print("🖱️ Bilgisayar menüsüne hover yapılıyor...")
        actions.move_to_element(bilgisayar_menu).perform()
        print("✅ Bilgisayar menüsüne hover yapıldı")
        
        # Laptop submenu'nun açılması için kısa bekleme
        print("⏳ Laptop submenu'nun açılması bekleniyor...")
        time.sleep(2)  # Kısa bekleme
        
        # Laptop submenu'nun açıldığını kontrol et
        try:
            laptop_elements = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='dizustu'], a[href*='laptop'], a[href*='notebook']")
            if laptop_elements:
                print("✅ Laptop submenu açıldı!")
            else:
                print("⚠️ Laptop submenu açılmadı, devam ediliyor...")
        except:
            print("⚠️ Laptop submenu kontrolü başarısız, devam ediliyor...")
        
        print("📋 Adım 5: Dizüstü bilgisayar linki aranıyor...")
        # Dizüstü bilgisayar linkini bul ve tıkla
        dizustu_link = self.find_dizustu_bilgisayar_link_optimized()
        if dizustu_link:
            print("✅ Dizüstü bilgisayar linki bulundu!")
            
            print("📋 Adım 6: Dizüstü bilgisayar linkine tıklanıyor...")
            print("🖱️ Dizüstü bilgisayar linkine tıklanıyor...")
            dizustu_link.click()
            print("✅ Dizüstü bilgisayar kategorisi seçildi")
            return True
        else:
            print("❌ Dizüstü bilgisayar linki bulunamadı")
            return False
    
    def find_elektronik_menu_optimized(self):
        """Elektronik menüsünü bulur - Optimized & Fast"""
        print("🔍 Elektronik menüsü aranıyor...")
        
        # Stabil selector'lar - Hepsiburada'nın değişmeyen yapıları
        stable_selectors = [
            # DOĞRU XPath - Kullanıcının verdiği
            "/html/body/div[1]/section[4]/div/div[2]/div/div/div/div/div/div/div[1]/div/ul/li[1]",
            
            # URL pattern'leri (en stabil)
            "a[href*='/elektronik']",
            "a[href*='/electronics']",
            "a[href*='elektronik']",
            "a[href*='electronics']",
            
            # Text-based selectors (daha stabil)
            "//a[contains(text(), 'Elektronik')]",
            "//a[contains(text(), 'Electronics')]",
            "//a[contains(text(), 'Elektrik')]",
            "//a[contains(text(), 'ELEKTRONİK')]",
            "//a[contains(text(), 'ELECTRONICS')]",
            
            # Data attributes (genellikle stabil)
            "[data-testid*='elektronik']",
            "[data-testid*='electronics']",
            "[data-testid*='category']",
            "[data-testid*='menu']",
            
            # Class patterns (Hepsiburada'nın genel yapısı)
            "a[class*='category'][href*='elektronik']",
            "a[class*='menu'][href*='elektronik']",
            "a[class*='nav'][href*='elektronik']",
            "a[class*='link'][href*='elektronik']",
            
            # Title attributes
            "a[title*='Elektronik']",
            "a[title*='Electronics']",
            "a[title*='ELEKTRONİK']",
            
            # Genel link arama
            "a[href*='kategori'][href*='elektronik']",
            "a[href*='category'][href*='elektronik']",
            
            # Daha geniş arama
            "//a[contains(@href, 'elektronik')]",
            "//a[contains(@title, 'Elektronik')]",
            "//a[contains(@class, 'menu') and contains(text(), 'Elektronik')]"
        ]
        
        for selector in stable_selectors:
            try:
                if selector.startswith("/html"):
                    # Full XPath selector - Öncelikli
                    print(f"🎯 Doğru XPath deneniyor: {selector}")
                    element = self.driver.find_element(By.XPATH, selector)
                    if element.is_displayed() and element.is_enabled():
                        print(f"✅ Elektronik menüsü bulundu (DOĞRU XPath): {selector}")
                        return element
                elif selector.startswith("//"):
                    # XPath selector
                    elements = self.driver.find_elements(By.XPATH, selector)
                else:
                    # CSS selector
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                
                if not selector.startswith("/html"):
                    for element in elements:
                        if element.is_displayed() and element.is_enabled():
                            href = element.get_attribute("href") or ""
                            text = element.text or ""
                            title = element.get_attribute("title") or ""
                            
                            # URL, text ve title kontrolü
                            if any(keyword.lower() in href.lower() or 
                                   keyword.lower() in text.lower() or 
                                   keyword.lower() in title.lower()
                                   for keyword in ["elektronik", "electronics", "elektrik"]):
                                print(f"✅ Elektronik menüsü bulundu: {selector}")
                                return element
                            
            except Exception as e:
                print(f"⚠️ Selector hatası: {selector} - {e}")
                continue
        
        # Fallback: Tüm linkleri bul ve içinde "elektronik" geçenleri ara
        print("🔍 Fallback: Tüm linklerde elektronik aranıyor...")
        try:
            all_links = self.driver.find_elements(By.TAG_NAME, "a")
            for link in all_links:
                try:
                    href = link.get_attribute("href") or ""
                    text = link.text or ""
                    title = link.get_attribute("title") or ""
                    
                    if any(keyword.lower() in href.lower() or 
                           keyword.lower() in text.lower() or 
                           keyword.lower() in title.lower()
                           for keyword in ["elektronik", "electronics", "elektrik"]):
                        if link.is_displayed() and link.is_enabled():
                            print(f"✅ Elektronik menüsü bulundu (fallback): {text}")
                            return link
                except:
                    continue
        except:
            pass
        
        print("❌ Elektronik menüsü bulunamadı")
        return None
    
    def find_elektronik_menu(self):
        """Elektronik menüsünü bulur - Legacy method"""
        return self.find_elektronik_menu_optimized()
    
    def find_bilgisayar_submenu_optimized(self):
        """Bilgisayar alt menüsünü bulur - Optimized & Fast"""
        print("🔍 Bilgisayar alt menüsü aranıyor...")
        
        # Stabil selector'lar - Hepsiburada'nın değişmeyen yapıları
        stable_selectors = [
            # URL pattern'leri (en stabil)
            "a[href*='/bilgisayar']",
            "a[href*='/computer']",
            "a[href*='/laptop']",
            "a[href*='/notebook']",
            
            # Text-based selectors (daha stabil)
            "//a[contains(text(), 'Bilgisayar')]",
            "//a[contains(text(), 'Computer')]",
            "//a[contains(text(), 'Laptop')]",
            "//a[contains(text(), 'Dizüstü')]",
            "//a[contains(text(), 'Notebook')]",
            
            # Data attributes (genellikle stabil)
            "[data-testid*='bilgisayar']",
            "[data-testid*='computer']",
            "[data-testid*='laptop']",
            "[data-testid*='notebook']",
            
            # Class patterns (Hepsiburada'nın genel yapısı)
            "a[class*='submenu'][href*='bilgisayar']",
            "a[class*='category'][href*='computer']",
            "a[class*='menu'][href*='laptop']",
            "a[class*='nav'][href*='notebook']",
            
            # Title attributes
            "a[title*='Bilgisayar']",
            "a[title*='Computer']",
            "a[title*='Laptop']",
            "a[title*='Dizüstü']"
        ]
        
        for selector in stable_selectors:
            try:
                if selector.startswith("//"):
                    # XPath selector
                    elements = self.driver.find_elements(By.XPATH, selector)
                else:
                    # CSS selector
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                
                for element in elements:
                    if element.is_displayed() and element.is_enabled():
                        href = element.get_attribute("href") or ""
                        text = element.text or ""
                        title = element.get_attribute("title") or ""
                        
                        # URL, text ve title kontrolü
                        if any(keyword.lower() in href.lower() or 
                               keyword.lower() in text.lower() or 
                               keyword.lower() in title.lower()
                               for keyword in ["bilgisayar", "computer", "laptop", "notebook", "dizüstü"]):
                            print(f"✅ Bilgisayar alt menüsü bulundu: {selector}")
                            return element
                            
            except Exception as e:
                continue
        
        print("❌ Bilgisayar alt menüsü bulunamadı")
        return None
    
    def find_bilgisayar_submenu(self):
        """Bilgisayar alt menüsünü bulur - Legacy method"""
        return self.find_bilgisayar_submenu_optimized()
    
    def find_dizustu_bilgisayar_link_optimized(self):
        """Dizüstü bilgisayar linkini bulur - Optimized & Fast"""
        print("🔍 Dizüstü bilgisayar linki aranıyor...")
        
        # Stabil selector'lar - Hepsiburada'nın değişmeyen yapıları
        stable_selectors = [
            # URL pattern'leri (en stabil)
            "a[href*='/dizustu-bilgisayarlar']",
            "a[href*='/dizustu-bilgisayar']",
            "a[href*='/laptop']",
            "a[href*='/notebook']",
            "a[href*='/bilgisayar']",
            
            # Text-based selectors (daha stabil)
            "//a[contains(text(), 'Dizüstü Bilgisayar')]",
            "//a[contains(text(), 'Dizüstü')]",
            "//a[contains(text(), 'Laptop')]",
            "//a[contains(text(), 'Notebook')]",
            "//a[contains(text(), 'Laptop Bilgisayar')]",
            
            # Data attributes (genellikle stabil)
            "[data-testid*='laptop']",
            "[data-testid*='dizustu']",
            "[data-testid*='notebook']",
            "[data-testid*='bilgisayar']",
            
            # Class patterns (Hepsiburada'nın genel yapısı)
            "a[class*='submenu'][href*='dizustu']",
            "a[class*='category'][href*='laptop']",
            "a[class*='menu'][href*='notebook']",
            "a[class*='nav'][href*='bilgisayar']",
            
            # Title attributes
            "a[title*='Dizüstü']",
            "a[title*='Laptop']",
            "a[title*='Notebook']",
            "a[title*='Bilgisayar']"
        ]
        
        for selector in stable_selectors:
            try:
                if selector.startswith("//"):
                    # XPath selector
                    elements = self.driver.find_elements(By.XPATH, selector)
                else:
                    # CSS selector
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                
                for element in elements:
                    if element.is_displayed() and element.is_enabled():
                        href = element.get_attribute("href") or ""
                        text = element.text or ""
                        title = element.get_attribute("title") or ""
                        
                        # URL, text ve title kontrolü
                        if any(keyword.lower() in href.lower() or 
                               keyword.lower() in text.lower() or 
                               keyword.lower() in title.lower()
                               for keyword in ["dizustu", "laptop", "notebook", "bilgisayar"]):
                            print(f"✅ Dizüstü bilgisayar linki bulundu: {selector}")
                            return element
                            
            except Exception as e:
                continue
        
        print("❌ Dizüstü bilgisayar linki bulunamadı")
        return None
    
    def find_dizustu_bilgisayar_link(self):
        """Dizüstü bilgisayar linkini bulur - Legacy method"""
        return self.find_dizustu_bilgisayar_link_optimized()
    
    def wait_for_submenu_to_appear(self):
        """Alt menünün görünmesini bekler - Optimized"""
        try:
            # Kısa bekleme süresi - hızlı işlem için
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".submenu, .dropdown-menu, [class*='submenu'], [class*='dropdown']"))
            )
            time.sleep(0.3)  # Çok kısa bekleme
        except TimeoutException:
            pass
    
    def wait_for_laptop_submenu_to_appear(self):
        """Dizüstü bilgisayar alt menüsünün görünmesini bekler - Optimized"""
        try:
            # Kısa bekleme süresi - hızlı işlem için
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='dizustu'], a[href*='laptop'], a[href*='notebook']"))
            )
            time.sleep(0.3)  # Çok kısa bekleme
        except TimeoutException:
            pass
    
    def click_first_filtered_product(self):
        """İlk filtrelenmiş ürünün 'Sepete Ekle' butonuna tıklar - Filtreleme sonrası"""
        print("🎯 İlk filtrelenmiş ürünün 'Sepete Ekle' butonuna tıklanıyor...")
        
        # Filtreleme yapıldıktan sonra sayfada kalmamız gerekiyor
        # URL kontrolü yapmadan direkt "Sepete Ekle" butonunu aramaya başla
        print("🔍 Filtrelenmiş sayfada ilk ürünün 'Sepete Ekle' butonu aranıyor...")
        
        # Loading wrapper'ın kaybolmasını bekle
        print("⏳ Loading wrapper'ın kaybolması bekleniyor...")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "moria-LoadingWrapper-jLotpB"))
            )
            print("✅ Loading wrapper kayboldu")
        except TimeoutException:
            print("⚠️ Loading wrapper hala görünür, devam ediliyor...")
        
        # Kısa bir bekleme daha
        time.sleep(1)
        
        # 1. Kullanıcının verdiği spesifik XPath ile "Sepete Ekle" butonunu bul
        try:
            print("🎯 Kullanıcının verdiği XPath ile 'Sepete Ekle' butonu aranıyor...")
            xpath = "/html/body/div[1]/main/div/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div/div/div/div/ul/li[1]/article/a/div/div[3]"
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            
            # JavaScript ile tıklama - loading wrapper'ı bypass eder
            print("🖱️ JavaScript ile tıklama yapılıyor...")
            self.driver.execute_script("arguments[0].click();", element)
            print("✅ İlk ürünün 'Sepete Ekle' butonuna tıklandı (JavaScript)")
            time.sleep(3)
            return True
        except TimeoutException:
            print("⚠️ Kullanıcı XPath ile bulunamadı, alternatif yöntemler deneniyor...")
        except Exception as e:
            print(f"❌ Kullanıcı XPath hatası: {e}")
        
        # 2. Filtrelenmiş sayfada ilk ürünün "Sepete Ekle" butonunu bul (alternatif)
        try:
            # Önce ürün listesi container'ını bul
            product_container_selectors = [
                ".product-list",
                ".product-grid", 
                ".product-items",
                "[data-testid*='product-list']",
                ".product-container",
                "ul[class*='product']",
                "div[class*='product-list']"
            ]
            
            product_container = None
            for selector in product_container_selectors:
                try:
                    product_container = self.driver.find_element(By.CSS_SELECTOR, selector)
                    if product_container.is_displayed():
                        print(f"✅ Ürün listesi bulundu: {selector}")
                        break
                except:
                    continue
            
            if product_container:
                # Container içindeki ilk ürünün "Sepete Ekle" butonunu bul
                add_to_cart_selectors = [
                    "li:first-child [data-test-id*='add-to-cart']",
                    "li:first-child [data-testid*='add-to-cart']",
                    "li:first-child button[class*='add']",
                    "li:first-child div[role='button']",
                    "li:first-child .price-area",
                    "li:first-child [class*='price']"
                ]
                
                for selector in add_to_cart_selectors:
                    try:
                        element = product_container.find_element(By.CSS_SELECTOR, selector)
                        if element.is_displayed():
                            element.click()
                            print(f"✅ İlk ürünün 'Sepete Ekle' butonuna tıklandı: {selector}")
                            time.sleep(3)
                            return True
                    except:
                        continue
            
            # Fallback: XPath ile ilk ürünü seç
            xpath = "/html/body/div[1]/main/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div/div/div/div/ul/li[1]"
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            print("✅ İlk ürün seçildi (XPath fallback)")
            time.sleep(3)
            return True
            
        except TimeoutException:
            print("⚠️ XPath ile ürün bulunamadı, alternatif yöntemler deneniyor...")
        except Exception as e:
            print(f"❌ XPath ürün seçimi hatası: {e}")
        
        # 2. Laptop-specific ürün selector'ları
        laptop_selectors = [
            "a[href*='dizustu-bilgisayar']",
            "a[href*='laptop']",
            "a[href*='notebook']",
            ".product-item a[href*='dizustu']",
            ".product-card a[href*='laptop']",
            "[data-testid*='product'] a[href*='dizustu']"
        ]
        
        for selector in laptop_selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    for element in elements:
                        if element.is_displayed():
                            href = element.get_attribute("href") or ""
                            if "dizustu" in href.lower() or "laptop" in href.lower() or "notebook" in href.lower():
                                element.click()
                                print(f"✅ Laptop ürünü seçildi: {selector}")
                                time.sleep(3)
                                return True
            except Exception as e:
                print(f"❌ Laptop ürün seçimi hatası: {e}")
                continue
        
        # 3. Genel ürün selector'ları (fallback)
        product_selectors = [
            ".product-item",
            "[data-testid*='product']",
            ".product-card",
            ".product-box",
            "a[href*='product']",
            ".product",
            "[class*='product']"
        ]
        
        for selector in product_selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    for element in elements:
                        if element.is_displayed():
                            # Ürün metnini kontrol et
                            text = element.text.lower()
                            if any(keyword in text for keyword in ["laptop", "dizüstü", "bilgisayar", "notebook"]):
                                element.click()
                                print(f"✅ Laptop ürünü seçildi (text kontrolü): {selector}")
                                time.sleep(3)
                                return True
            except Exception as e:
                print(f"❌ Ürün seçimi hatası: {e}")
                continue
        
        # 4. Link tabanlı arama
        try:
            all_links = self.driver.find_elements(By.TAG_NAME, "a")
            for link in all_links:
                try:
                    href = link.get_attribute("href") or ""
                    if "dizustu" in href.lower() or "laptop" in href.lower() or "notebook" in href.lower():
                        if link.is_displayed():
                            link.click()
                            print("✅ Laptop ürünü seçildi (link arama)")
                            time.sleep(3)
                            return True
                except:
                    continue
        except:
            pass
        
        print("❌ Laptop ürünü bulunamadı")
        return False
    
    def get_filtered_product_count(self):
        """Filtrelenmiş ürün sayısını alır"""
        try:
            count_selectors = [
                ".product-count",
                "[data-testid*='count']",
                ".filtered-count",
                ".result-count"
            ]
            
            for selector in count_selectors:
                try:
                    element = self.driver.find_element(By.CSS_SELECTOR, selector)
                    count_text = element.text
                    print(f"📊 Filtrelenmiş ürün sayısı: {count_text}")
                    return count_text
                except:
                    continue
            
            print("⚠️ Ürün sayısı bulunamadı")
            return "Bilinmiyor"
            
        except Exception as e:
            print(f"❌ Ürün sayısı alma hatası: {e}")
            return "Hata"
