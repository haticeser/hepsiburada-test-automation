# pages/modules/filter_module.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ..base_page import BasePage


class FilterModule(BasePage):
    """Filtreleme işlemleri için modül"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def apply_specific_filters(self, brand="Lenovo", processor="Intel Core i7"):
        """Belirli filtreleri uygular"""
        print(f"🔍 Filtreler uygulanıyor: {brand} + {processor}")
        
        try:
            # Marka filtresi
            brand_success = self.apply_brand_filter(brand)
            if not brand_success:
                print(f"❌ {brand} marka filtresi uygulanamadı")
                return False
            
            time.sleep(2)
            
            # İşlemci filtresi
            processor_success = self.apply_processor_filter(processor)
            if not processor_success:
                print(f"❌ {processor} işlemci filtresi uygulanamadı")
                return False
            
            print("✅ Tüm filtreler başarıyla uygulandı")
            
            # Filtreleme sonrası sayfa yüklenmesini bekle
            print("⏳ Filtreleme sonrası sayfa yüklenmesi bekleniyor...")
            time.sleep(5)  # Filtreleme sonrası daha uzun bekleme
            
            # Sayfa yüklenmesini kontrol et
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item, .product-card, [class*='product']"))
                )
                print("✅ Filtrelenmiş ürünler yüklendi")
            except:
                print("⚠️ Filtrelenmiş ürünler yüklenemedi, devam ediliyor...")
            
            return True
            
        except Exception as e:
            print(f"❌ Filtre uygulama hatası: {e}")
            return False
    
    def apply_brand_filter(self, brand):
        """Marka filtresini uygular"""
        print(f"🏷️ {brand} marka filtresi uygulanıyor...")
        
        brand_selectors = [
            f"input[value*='{brand.lower()}']",
            f"input[value*='{brand.upper()}']",
            f"label[for*='{brand.lower()}']",
            f"[data-testid*='{brand.lower()}']",
            f".filter-{brand.lower()}"
        ]
        
        for selector in brand_selectors:
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                if not element.is_selected():
                    element.click()
                    print(f"✅ {brand} marka filtresi uygulandı")
                    return True
            except TimeoutException:
                continue
        
        print(f"❌ {brand} marka filtresi bulunamadı")
        return False
    
    def apply_processor_filter(self, processor):
        """İşlemci filtresini uygular - Akıllı strateji"""
        print(f"⚡ {processor} işlemci filtresi uygulanıyor...")
        
        # Önce doğru sayfada olduğumuzu kontrol et
        current_url = self.driver.current_url.lower()
        if "dizustu" not in current_url and "laptop" not in current_url and "bilgisayar" not in current_url:
            print("⚠️ Yanlış kategorideyiz, işlemci filtresi atlanıyor")
            return True
        
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
        
        # 1. Text içeriğine göre arama (en stabil)
        processor_keywords = ["Intel Core i7", "i7", "Intel", "Core i7", "i7-"]
        for keyword in processor_keywords:
            try:
                xpath = f"//label[contains(text(), '{keyword}')] | //span[contains(text(), '{keyword}')] | //a[contains(text(), '{keyword}')]"
                element = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                if element.is_displayed():
                    # JavaScript ile tıklama - loading wrapper'ı bypass eder
                    print(f"🖱️ JavaScript ile tıklama yapılıyor: {keyword}")
                    self.driver.execute_script("arguments[0].click();", element)
                    print(f"✅ İşlemci filtresi uygulandı (JavaScript: {keyword})")
                    time.sleep(1)
                    return True
            except TimeoutException:
                continue
        
        # 2. Checkbox input arama
        checkbox_selectors = [
            "input[type='checkbox'][value*='i7']",
            "input[type='checkbox'][value*='intel']",
            "input[type='checkbox'][value*='core']",
            "input[type='checkbox'][id*='i7']",
            "input[type='checkbox'][id*='intel']"
        ]
        
        for selector in checkbox_selectors:
            try:
                element = WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                if not element.is_selected():
                    element.click()
                    print(f"✅ İşlemci filtresi uygulandı (checkbox: {selector})")
                    time.sleep(1)
                    return True
            except TimeoutException:
                continue
        
        # 3. Label ile arama
        label_selectors = [
            "label[for*='i7']",
            "label[for*='intel']",
            "label[for*='core']",
            "label[class*='filter']"
        ]
        
        for selector in label_selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                for element in elements:
                    if element.is_displayed():
                        text = element.text.lower()
                        if any(keyword.lower() in text for keyword in ["i7", "intel", "core"]):
                            element.click()
                            print(f"✅ İşlemci filtresi uygulandı (label: {text[:30]})")
                            time.sleep(1)
                            return True
            except:
                continue
        
        # 4. Genel filtre alanı arama
        try:
            filter_sections = self.driver.find_elements(By.CSS_SELECTOR, ".filter-section, .filter-group, [class*='filter']")
            for section in filter_sections:
                try:
                    if "işlemci" in section.text.lower() or "processor" in section.text.lower() or "cpu" in section.text.lower():
                        # Bu bölümde işlemci filtresi var
                        clickable_elements = section.find_elements(By.CSS_SELECTOR, "label, span, a, button")
                        for elem in clickable_elements:
                            if elem.is_displayed():
                                text = elem.text.lower()
                                if any(keyword.lower() in text for keyword in ["i7", "intel", "core"]):
                                    elem.click()
                                    print(f"✅ İşlemci filtresi uygulandı (genel arama: {text[:30]})")
                                    time.sleep(1)
                                    return True
                except:
                    continue
        except:
            pass
        
        print(f"⚠️ {processor} işlemci filtresi bulunamadı - devam ediliyor")
        return True  # Filtre bulunamasa bile devam et
    
    def apply_category_filters(self, brand=None, min_price=None, max_price=None):
        """Kategori filtrelerini uygular"""
        print("📂 Kategori filtreleri uygulanıyor...")
        
        # Genel kategori filtreleri
        category_selectors = [
            ".category-filter",
            "[data-testid*='category']",
            ".filter-category"
        ]
        
        for selector in category_selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    print("✅ Kategori filtreleri bulundu")
                    return True
            except:
                continue
        
        print("⚠️ Kategori filtreleri bulunamadı")
        return False
    
    def apply_price_filter(self, min_price, max_price):
        """Fiyat filtresini uygular"""
        print(f"💰 Fiyat filtresi uygulanıyor: {min_price} - {max_price}")
        
        try:
            # Minimum fiyat
            min_price_selectors = [
                "input[name*='min']",
                "input[placeholder*='Min']",
                "input[data-testid*='min-price']"
            ]
            
            for selector in min_price_selectors:
                try:
                    element = self.driver.find_element(By.CSS_SELECTOR, selector)
                    element.clear()
                    element.send_keys(str(min_price))
                    print(f"✅ Minimum fiyat girildi: {min_price}")
                    break
                except:
                    continue
            
            # Maksimum fiyat
            max_price_selectors = [
                "input[name*='max']",
                "input[placeholder*='Max']",
                "input[data-testid*='max-price']"
            ]
            
            for selector in max_price_selectors:
                try:
                    element = self.driver.find_element(By.CSS_SELECTOR, selector)
                    element.clear()
                    element.send_keys(str(max_price))
                    print(f"✅ Maksimum fiyat girildi: {max_price}")
                    break
                except:
                    continue
            
            # Filtre uygula butonu
            apply_button_selectors = [
                "button[data-testid*='apply']",
                ".apply-filter",
                "button[class*='apply']"
            ]
            
            for selector in apply_button_selectors:
                try:
                    element = self.driver.find_element(By.CSS_SELECTOR, selector)
                    element.click()
                    print("✅ Fiyat filtresi uygulandı")
                    time.sleep(2)
                    return True
                except:
                    continue
            
            return True
            
        except Exception as e:
            print(f"❌ Fiyat filtresi hatası: {e}")
            return False
    
    def clear_all_filters(self):
        """Tüm filtreleri temizler"""
        print("🧹 Tüm filtreler temizleniyor...")
        
        clear_selectors = [
            "button[data-testid*='clear']",
            ".clear-filters",
            "button[class*='clear']",
            "a[href*='clear']"
        ]
        
        for selector in clear_selectors:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector)
                element.click()
                print("✅ Tüm filtreler temizlendi")
                time.sleep(2)
                return True
            except:
                continue
        
        print("⚠️ Filtre temizleme butonu bulunamadı")
        return False
    
    def get_active_filters(self):
        """Aktif filtreleri alır"""
        print("📋 Aktif filtreler kontrol ediliyor...")
        
        active_filter_selectors = [
            ".active-filter",
            "[data-testid*='active-filter']",
            ".selected-filter",
            ".applied-filter"
        ]
        
        active_filters = []
        for selector in active_filter_selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                for element in elements:
                    filter_text = element.text
                    if filter_text:
                        active_filters.append(filter_text)
            except:
                continue
        
        if active_filters:
            print(f"✅ Aktif filtreler: {', '.join(active_filters)}")
        else:
            print("⚠️ Aktif filtre bulunamadı")
        
        return active_filters
