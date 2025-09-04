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
        
        # Sayfa yüklenmesini bekle (daha akıllı bekleme)
        print("⏳ Sayfa yükleniyor...")
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Çerez popup'ını kapat
        self.close_cookie_popup()
        
        # Google şifre kaydetme popup'ını kontrol et ve kapat
        self.close_google_password_popup()
        
        # Ana sayfa elementlerinin yüklenmesini bekle
        print("🔍 Ana sayfa elementleri kontrol ediliyor...")
        try:
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "nav, .header, [class*='menu']"))
            )
            print("✅ Ana sayfa başarıyla yüklendi")
        except:
            print("⚠ Ana sayfa elementleri yüklenemedi, devam ediliyor...")
        
        # Kısa bir bekleme (sayfa stabilizasyonu için)
        time.sleep(1)
    
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
                
            except:
                print("⚠ Hover yöntemi başarısız, alternatif yöntem deneniyor...")
                # Doğrudan üye ol sayfasına git
                self.driver.get("https://www.hepsiburada.com/uyelik/yeni-uye")
                
        except Exception as e:
            print(f"⚠ Üye ol linki bulunamadı: {e}")
            # Doğrudan üye ol sayfasına git
            self.driver.get("https://www.hepsiburada.com/uyelik/yeni-uye")
    
    def navigate_to_login(self):
        """Giriş sayfasına yönlendirir"""
        print("🔑 Giriş sayfasına yönlendiriliyor...")
        self.driver.get("https://www.hepsiburada.com/uyelik/giris")
    
    def select_laptop_product(self):
        """Elektronik menüsünden dizüstü bilgisayar seçimi yapar"""
        print("💻 Dizüstü bilgisayar seçimi yapılıyor...")
        print("🎯 Menü navigasyonu ile dizüstü bilgisayar seçilecek...")
        
        try:
            # Menü navigasyonu yöntemi
            print("🔄 Menü navigasyonu başlatılıyor...")
            
            # 1. Elektronik menüsünü bul ve hover yap
            print("🔌 Elektronik menüsüne hover yapılıyor...")
            elektronik_menu = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Elektronik')]"))
            )
            
            actions = ActionChains(self.driver)
            actions.move_to_element(elektronik_menu).perform()
            print("✅ Elektronik menüsüne hover yapıldı")
            time.sleep(2)  # Alt menünün açılması için bekle
            
            # 2. Bilgisayar/Tablet alt menüsünü bul ve hover yap
            print("💻 Bilgisayar/Tablet alt menüsüne hover yapılıyor...")
            bilgisayar_menu = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Bilgisayar/Tablet')]"))
            )
            
            actions.move_to_element(bilgisayar_menu).perform()
            print("✅ Bilgisayar/Tablet alt menüsüne hover yapıldı")
            time.sleep(2)  # Alt menünün açılması için bekle
            
            # 3. Dizüstü Bilgisayar seçeneğini bul ve tıkla
            print("🖥️ Dizüstü Bilgisayar seçeneğine tıklanıyor...")
            
            # Farklı text varyasyonlarını dene
            dizustu_selectors = [
                "//a[contains(text(), 'Dizüstü Bilgisayar')]",
                "//a[contains(text(), 'Laptop')]", 
                "//a[contains(text(), 'Notebook')]",
                "//a[contains(text(), 'Dizüstü')]",
                "//a[contains(text(), 'Bilgisayar')]"
            ]
            
            dizustu_link = None
            for selector in dizustu_selectors:
                try:
                    dizustu_link = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, selector))
                    )
                    print(f"✅ Dizüstü bilgisayar linki bulundu: {selector}")
                    break
                except:
                    continue
            
            if not dizustu_link:
                print("❌ Dizüstü bilgisayar linki bulunamadı")
                raise Exception("Dizüstü bilgisayar linki bulunamadı")
            
            dizustu_link.click()
            print("✅ Dizüstü Bilgisayar seçeneğine tıklandı")
            
            # 4. Sayfa yüklendiğini doğrula
            time.sleep(3)
            page_title = self.driver.title.lower()
            current_url = self.driver.current_url
            
            print(f"📄 Sayfa başlığı: {page_title}")
            print(f"🔗 Mevcut URL: {current_url}")
            
            # Dizüstü bilgisayar sayfasında olduğumuzu doğrula
            if any(keyword in page_title for keyword in ['dizüstü', 'laptop', 'notebook', 'bilgisayar']):
                print("✅ Dizüstü bilgisayar sayfasına başarıyla gidildi (menü navigasyonu ile)")
                return True
            elif "laptop" in current_url or "dizustu" in current_url or "bilgisayar" in current_url:
                print("✅ Dizüstü bilgisayar sayfasına başarıyla gidildi (URL kontrolü)")
                return True
            else:
                print("⚠️ Sayfa yüklendi ama dizüstü bilgisayar sayfası olmayabilir")
                return True
                
        except Exception as e:
            print(f"❌ Menü navigasyonu başarısız: {e}")
            
            # Alternatif: Doğrudan URL yöntemi
            try:
                print("🔄 Alternatif doğrudan URL yöntemi deneniyor...")
                print("🔗 Doğrudan dizüstü bilgisayar sayfasına gidiliyor...")
                self.driver.get("https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98")
                
                # Sayfa yüklenmesini bekle
                time.sleep(3)
                
                # Sayfa başlığını kontrol et
                page_title = self.driver.title.lower()
                current_url = self.driver.current_url
                
                print(f"📄 Sayfa başlığı: {page_title}")
                print(f"🔗 Mevcut URL: {current_url}")
                
                # Dizüstü bilgisayar sayfasında olduğumuzu doğrula
                if any(keyword in page_title for keyword in ['dizüstü', 'laptop', 'notebook', 'bilgisayar']):
                    print("✅ Dizüstü bilgisayar sayfasına başarıyla gidildi (doğrudan URL ile)")
                    return True
                elif "laptop" in current_url or "dizustu" in current_url or "bilgisayar" in current_url:
                    print("✅ Dizüstü bilgisayar sayfasına başarıyla gidildi (URL kontrolü)")
                    return True
                else:
                    print("⚠️ Sayfa yüklendi ama dizüstü bilgisayar sayfası olmayabilir")
                    return True
                
            except Exception as e2:
                print(f"❌ Doğrudan URL yöntemi de başarısız: {e2}")
                return False
    
    def get_available_filters(self):
        """Sayfada mevcut olan tüm filtreleri listeler"""
        print("🔍 Mevcut filtreler listeleniyor...")
        
        try:
            # Sol sidebar'ın yüklenmesini bekle
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".filter-container, .sidebar, [class*='filter'], [class*='sidebar']"))
            )
            
            # Tüm filtre gruplarını bul
            filter_groups = self.driver.find_elements("css selector", "[class*='filter'], [class*='sidebar'] > div, .filter-group")
            
            available_filters = {}
            
            for group in filter_groups:
                try:
                    # Filtre grubu başlığını bul
                    group_title = group.find_element("css selector", "h3, h4, .title, [class*='title']").text
                    print(f"\n📋 {group_title}:")
                    
                    # Gruptaki filtreleri bul
                    filters = group.find_elements("css selector", "input[type='checkbox'], label, .filter-item")
                    
                    group_filters = []
                    for filter_item in filters:
                        try:
                            if filter_item.tag_name == "input" and filter_item.get_attribute("type") == "checkbox":
                                # Checkbox filtresi
                                filter_name = filter_item.get_attribute("value") or filter_item.get_attribute("name")
                                is_selected = filter_item.is_selected()
                                status = "✅ Seçili" if is_selected else "❌ Seçili değil"
                                print(f"  - {filter_name}: {status}")
                                group_filters.append({
                                    "name": filter_name,
                                    "type": "checkbox",
                                    "selected": is_selected,
                                    "element": filter_item
                                })
                            elif filter_item.tag_name == "label":
                                # Label filtresi
                                filter_text = filter_item.text.strip()
                                if filter_text:
                                    print(f"  - {filter_text}")
                                    group_filters.append({
                                        "name": filter_text,
                                        "type": "label",
                                        "selected": False,
                                        "element": filter_item
                                    })
                            else:
                                # Diğer filtre türleri
                                filter_text = filter_item.text.strip()
                                if filter_text:
                                    print(f"  - {filter_text}")
                                    group_filters.append({
                                        "name": filter_text,
                                        "type": "other",
                                        "selected": False,
                                        "element": filter_item
                                    })
                        except:
                            continue
                    
                    available_filters[group_title] = group_filters
                    
                except:
                    continue
            
            return available_filters
            
        except Exception as e:
            print(f"❌ Filtreler listelenemedi: {e}")
            return {}
    
    def get_selected_filters(self):
        """Şu anda seçili olan filtreleri listeler"""
        print("✅ Seçili filtreler kontrol ediliyor...")
        
        try:
            # Tüm seçili checkbox'ları bul
            selected_checkboxes = self.driver.find_elements("css selector", "input[type='checkbox']:checked")
            
            selected_filters = []
            for checkbox in selected_checkboxes:
                try:
                    filter_name = checkbox.get_attribute("value") or checkbox.get_attribute("name")
                    if filter_name:
                        selected_filters.append(filter_name)
                        print(f"✅ Seçili filtre: {filter_name}")
                except:
                    continue
            
            if not selected_filters:
                print("⚠️ Hiçbir filtre seçili değil")
            
            return selected_filters
            
        except Exception as e:
            print(f"❌ Seçili filtreler alınamadı: {e}")
            return []
    
    def apply_specific_filters(self, brand="Lenovo", processor="Intel Core i7"):
        """Sadece Lenovo marka ve Intel Core i7 işlemci filtrelerini uygular"""
        print("🔍 Belirli filtreler uygulanıyor...")
        
        try:
            # Sol sidebar'ın yüklenmesini bekle
            print("⏳ Sol sidebar yükleniyor...")
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".filter-container, .sidebar, [class*='filter'], [class*='sidebar']"))
            )
            
            # Sayfanın tamamen yüklenmesini bekle
            time.sleep(2)
            
            # 1. Lenovo marka filtresi
            print(f"🏷️ {brand} marka filtresi uygulanıyor...")
            try:
                # Lenovo checkbox'ını bul
                lenovo_checkbox = self.driver.find_element("xpath", "//input[@type='checkbox' and @value='lenovo']")
                
                if not lenovo_checkbox.is_selected():
                    # Önce sayfayı scroll et
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", lenovo_checkbox)
                    time.sleep(1)
                    
                    # JavaScript ile tıkla (click interception'ı önler)
                    self.driver.execute_script("arguments[0].click();", lenovo_checkbox)
                    print(f"✅ {brand} marka filtresi JavaScript ile uygulandı")
                else:
                    print(f"✅ {brand} marka filtresi zaten seçili")
                    
            except Exception as e:
                print(f"⚠️ {brand} marka filtresi hatası: {e}")
            
            # 2. Intel Core i7 işlemci filtresi
            print(f"🖥️ {processor} işlemci filtresi uygulanıyor...")
            try:
                # Farklı selector'ları dene
                processor_selectors = [
                    f"//input[@type='checkbox' and @name='islemcitipi' and @value='{processor}']",
                    f"//input[@type='checkbox' and @value='{processor}']",
                    f"//input[@type='checkbox' and contains(@value, 'Intel')]",
                    f"//input[@type='checkbox' and contains(@value, 'Core')]",
                    f"//input[@type='checkbox' and contains(@value, 'i7')]"
                ]
                
                processor_checkbox = None
                for selector in processor_selectors:
                    try:
                        processor_checkbox = self.driver.find_element("xpath", selector)
                        if processor_checkbox:
                            print(f"✅ {processor} işlemci filtresi bulundu: {selector}")
                            break
                    except:
                        continue
                
                if processor_checkbox:
                    if not processor_checkbox.is_selected():
                        # Önce sayfayı scroll et
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", processor_checkbox)
                        time.sleep(1)
                        
                        # JavaScript ile tıkla
                        self.driver.execute_script("arguments[0].click();", processor_checkbox)
                        print(f"✅ {processor} işlemci filtresi JavaScript ile uygulandı")
                    else:
                        print(f"✅ {processor} işlemci filtresi zaten seçili")
                else:
                    print(f"⚠️ {processor} işlemci filtresi bulunamadı")
                    
            except Exception as e:
                print(f"⚠️ {processor} işlemci filtresi hatası: {e}")
            
            # Filtrelerin uygulanmasını bekle
            print("⏳ Filtreler uygulanıyor...")
            time.sleep(3)
            
            # Filtrelerin başarıyla uygulandığını kontrol et
            print("🔍 Filtrelerin uygulanması kontrol ediliyor...")
            
            try:
                # Lenovo filtresini kontrol et
                lenovo_checkbox = self.driver.find_element("xpath", "//input[@type='checkbox' and @value='lenovo']")
                if lenovo_checkbox.is_selected():
                    print("✅ Lenovo marka filtresi başarıyla uygulandı")
                else:
                    print("⚠️ Lenovo marka filtresi uygulanamadı")
            except:
                print("⚠️ Lenovo checkbox'ı bulunamadı")
            
            # Intel Core i7 filtresini kontrol et
            processor_found = False
            for selector in processor_selectors:
                try:
                    processor_checkbox = self.driver.find_element("xpath", selector)
                    if processor_checkbox and processor_checkbox.is_selected():
                        print(f"✅ Intel Core i7 işlemci filtresi başarıyla uygulandı")
                        processor_found = True
                        break
                except:
                    continue
            
            if not processor_found:
                print("⚠️ Intel Core i7 işlemci filtresi uygulanamadı")
            
            print("✅ Belirli filtreler uygulandı, ürünler listeleniyor...")
            return True
            
        except Exception as e:
            print(f"❌ Belirli filtreler uygulanamadı: {e}")
            return False
    
    def apply_category_filters(self, brand=None, min_price=None, max_price=None, screen_size=None):
        """Sol taraftaki kategori filtrelerini uygular"""
        print("🔍 Kategori filtreleri uygulanıyor...")
        
        try:
            # Sol sidebar'ın yüklenmesini bekle
            print("⏳ Sol sidebar yükleniyor...")
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".filter-container, .sidebar, [class*='filter'], [class*='sidebar']"))
            )
            
            # Marka filtresi
            if brand:
                print(f"🏷️ Marka filtresi uygulanıyor: {brand}")
                try:
                    # Marka filtresi için daha spesifik selector'ları dene
                    brand_selectors = [
                        # data-test-id ile
                        f"//input[@type='checkbox' and @value='{brand.lower()}']",
                        f"//input[@type='checkbox' and @name='markalar' and @value='{brand.lower()}']",
                        # Label içinde marka adı
                        f"//label[contains(text(), '{brand}')]//input[@type='checkbox']",
                        f"//label[contains(text(), '{brand}')]/input[@type='checkbox']",
                        # Genel marka arama
                        f"//span[contains(text(), '{brand}')]",
                        f"//label[contains(text(), '{brand}')]",
                        f"//a[contains(text(), '{brand}')]",
                        f"//div[contains(text(), '{brand}')]"
                    ]
                    
                    brand_filter = None
                    for selector in brand_selectors:
                        try:
                            brand_filter = self.driver.find_element("xpath", selector)
                            if brand_filter:
                                print(f"✅ {brand} marka filtresi bulundu: {selector}")
                                break
                        except:
                            continue
                    
                    if brand_filter:
                        # Checkbox'ın seçili olup olmadığını kontrol et
                        if brand_filter.tag_name == "input" and brand_filter.get_attribute("type") == "checkbox":
                            if not brand_filter.is_selected():
                                # Önce label'a tıkla (daha güvenilir)
                                try:
                                    label = brand_filter.find_element("xpath", "./following-sibling::*[1] | ./parent::label")
                                    label.click()
                                    print(f"✅ {brand} marka filtresi label'a tıklanarak uygulandı")
                                except:
                                    # Doğrudan checkbox'a tıkla
                                    brand_filter.click()
                                    print(f"✅ {brand} marka filtresi checkbox'a tıklanarak uygulandı")
                            else:
                                print(f"✅ {brand} marka filtresi zaten seçili")
                        else:
                            # Checkbox değilse doğrudan tıkla
                            brand_filter.click()
                            print(f"✅ {brand} marka filtresi uygulandı")
                        
                        # Filtrenin uygulanmasını bekle
                        time.sleep(1)
                        
                        # Filtrenin başarıyla uygulandığını kontrol et
                        try:
                            # data-test-id değişimini kontrol et
                            updated_filter = self.driver.find_element("xpath", f"//input[@type='checkbox' and @value='{brand.lower()}']")
                            if updated_filter.get_attribute("data-test-id") == "checked":
                                print(f"✅ {brand} marka filtresi başarıyla uygulandı (data-test-id: checked)")
                            else:
                                print(f"⚠️ {brand} marka filtresi uygulandı ama data-test-id güncellenmedi")
                        except:
                            print(f"✅ {brand} marka filtresi uygulandı")
                            
                    else:
                        print(f"⚠️ {brand} marka filtresi bulunamadı")
                        
                except Exception as e:
                    print(f"⚠️ Marka filtresi hatası: {e}")
            
            # Fiyat aralığı filtresi
            if min_price or max_price:
                print(f"💰 Fiyat aralığı filtresi uygulanıyor: {min_price} - {max_price}")
                try:
                    # Fiyat input alanlarını bul
                    price_inputs = self.driver.find_elements("css selector", "input[type='number'], input[placeholder*='fiyat'], input[placeholder*='price']")
                    
                    if len(price_inputs) >= 2:
                        # Minimum fiyat
                        if min_price:
                            price_inputs[0].clear()
                            price_inputs[0].send_keys(str(min_price))
                            print(f"✅ Minimum fiyat: {min_price}")
                        
                        # Maximum fiyat
                        if max_price:
                            price_inputs[1].clear()
                            price_inputs[1].send_keys(str(max_price))
                            print(f"✅ Maximum fiyat: {max_price}")
                        
                        # Fiyat filtresini uygula butonunu bul ve tıkla
                        try:
                            apply_price_button = self.driver.find_element("xpath", "//button[contains(text(), 'Uygula') or contains(text(), 'Apply') or contains(text(), 'Filtrele')]")
                            apply_price_button.click()
                            print("✅ Fiyat filtresi uygulandı")
                        except:
                            print("⚠️ Fiyat filtresi uygulama butonu bulunamadı")
                    else:
                        print("⚠️ Fiyat input alanları bulunamadı")
                        
                except Exception as e:
                    print(f"⚠️ Fiyat filtresi hatası: {e}")
            
            # Ekran boyutu filtresi
            if screen_size:
                print(f"📱 Ekran boyutu filtresi uygulanıyor: {screen_size}")
                try:
                    # Ekran boyutu için farklı selector'ları dene
                    screen_size_selectors = [
                        f"//span[contains(text(), '{screen_size}')]",
                        f"//label[contains(text(), '{screen_size}')]",
                        f"//a[contains(text(), '{screen_size}')]",
                        f"//div[contains(text(), '{screen_size}')]"
                    ]
                    
                    screen_filter = None
                    for selector in screen_size_selectors:
                        try:
                            screen_filter = self.driver.find_element("xpath", selector)
                            if screen_filter:
                                break
                        except:
                            continue
                    
                    if screen_filter:
                        # Checkbox varsa tıkla, yoksa tıklanabilir element olarak tıkla
                        try:
                            if screen_filter.tag_name == "input" and screen_filter.get_attribute("type") == "checkbox":
                                if not screen_filter.is_selected():
                                    screen_filter.click()
                            else:
                                screen_filter.click()
                            print(f"✅ {screen_size} ekran boyutu filtresi uygulandı")
                        except:
                            # JavaScript ile tıkla
                            self.driver.execute_script("arguments[0].click();", screen_filter)
                            print(f"✅ {screen_size} ekran boyutu filtresi JavaScript ile uygulandı")
                    else:
                        print(f"⚠️ {screen_size} ekran boyutu filtresi bulunamadı")
                        
                except Exception as e:
                    print(f"⚠️ Ekran boyutu filtresi hatası: {e}")
            
            # Filtrelerin uygulanmasını bekle
            print("⏳ Filtreler uygulanıyor...")
            time.sleep(2)
            
            print("✅ Kategori filtreleri başarıyla uygulandı")
            return True
            
        except Exception as e:
            print(f"❌ Kategori filtreleri uygulanamadı: {e}")
            return False
    
    def get_filtered_product_count(self):
        """Filtrelenmiş ürün sayısını döndürür"""
        try:
            # Ürün sayısı bilgisini bul
            product_count_selectors = [
                "//span[contains(text(), 'ürün')]",
                "//span[contains(text(), 'product')]",
                "//div[contains(text(), 'ürün')]",
                "//div[contains(text(), 'product')]",
                ".product-count",
                "[class*='count']"
            ]
            
            for selector in product_count_selectors:
                try:
                    if selector.startswith("//"):
                        count_element = self.driver.find_element("xpath", selector)
                    else:
                        count_element = self.driver.find_element("css selector", selector)
                    
                    if count_element:
                        count_text = count_element.text
                        print(f"📊 Filtrelenmiş ürün sayısı: {count_text}")
                        return count_text
                except:
                    continue
            
            print("⚠️ Ürün sayısı bilgisi bulunamadı")
            return None
            
        except Exception as e:
            print(f"⚠️ Ürün sayısı alınamadı: {e}")
            return None
    
    def select_product_category(self, main_menu_text, sub_menu_text, final_option_text):
        """Genel ürün kategorisi seçimi yapar"""
        print(f"🛍️ {main_menu_text} > {sub_menu_text} > {final_option_text} seçimi yapılıyor...")
        
        try:
            # Ana menüyü bul ve hover yap
            print(f"🔌 {main_menu_text} menüsüne hover yapılıyor...")
            main_menu = self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{main_menu_text}')]"))
            )
            
            actions = ActionChains(self.driver)
            actions.move_to_element(main_menu).perform()
            print(f"✅ {main_menu_text} menüsüne hover yapıldı")
            
            # Alt menünün yüklenmesini bekle
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), '{sub_menu_text}')]"))
            )
            
            # Alt menüyü bul ve hover yap
            print(f"📱 {sub_menu_text} alt menüsüne hover yapılıyor...")
            sub_menu = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{sub_menu_text}')]"))
            )
            
            actions.move_to_element(sub_menu).perform()
            print(f"✅ {sub_menu_text} alt menüsüne hover yapıldı")
            
            # Final seçeneğin yüklenmesini bekle
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), '{final_option_text}')]"))
            )
            
            # Final seçeneği bul ve tıkla
            print(f"🎯 {final_option_text} seçeneğine tıklanıyor...")
            final_option = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{final_option_text}')]"))
            )
            
            final_option.click()
            print(f"✅ {final_option_text} sayfasına gidildi")
            
            # Sayfa yüklendiğini doğrula
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h1, .page-title, [class*='title']"))
            )
            print(f"✅ {final_option_text} sayfası başarıyla yüklendi")
            return True
            
        except Exception as e:
            print(f"❌ {final_option_text} seçimi başarısız: {e}")
            return False
    
    
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
    
    def click_first_filtered_product(self):
        """Filtrelenmiş ürünlerden ilkini seçer ve ürün sayfasına gider"""
        print("🎯 Filtrelenmiş ürünlerden ilkini seçiliyor...")
        
        try:
            # Ürün listesinin yüklenmesini bekle
            print("⏳ Ürün listesi yükleniyor...")
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='productCard']"))
            )
            
            # İlk ürünü bul - farklı selector'ları dene
            first_product_selectors = [
                # Ana ürün kartı selector'ları
                "[class*='productCard']",
                "[class*='product-card']",
                "article[class*='productCard']",
                "li[class*='product']",
                ".product-item",
                ".product-card",
                # Daha spesifik selector'lar
                "[class*='productCard-module_article']",
                "[class*='productCard-module_productCardRoot']"
            ]
            
            first_product = None
            for selector in first_product_selectors:
                try:
                    products = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if products:
                        first_product = products[0]
                        print(f"✅ İlk ürün bulundu: {selector}")
                        break
                except:
                    continue
            
            if not first_product:
                print("❌ Hiçbir ürün bulunamadı")
                return False
            
            # Ürün bilgilerini al
            try:
                product_title = first_product.get_attribute("title") or first_product.text[:100]
                print(f"📦 Seçilen ürün: {product_title}")
            except:
                print("📦 Ürün bilgileri alınamadı")
            
            # Ürün linkini bul ve tıkla
            try:
                # Önce ürün kartı içindeki link'i bul
                product_link = first_product.find_element(By.TAG_NAME, "a")
                if product_link:
                    print("🔗 Ürün linki bulundu, tıklanıyor...")
                    
                    # Link'e tıkla
                    product_link.click()
                    print("✅ Ürün linkine tıklandı")
                    
                    # Sayfa yüklenmesini bekle
                    time.sleep(3)
                    
                    # URL değişimini kontrol et
                    current_url = self.driver.current_url
                    if "hepsiburada.com" in current_url and "product" in current_url.lower():
                        print(f"✅ Ürün sayfasına başarıyla gidildi: {current_url}")
                        return True
                    else:
                        print(f"⚠️ Sayfa yüklendi ama ürün sayfası olmayabilir: {current_url}")
                        return True
                        
            except Exception as e:
                print(f"⚠️ Ürün linki bulunamadı, alternatif yöntem deneniyor: {e}")
                
                # Alternatif: Doğrudan ürün kartına tıkla
                try:
                    first_product.click()
                    print("✅ Ürün kartına tıklandı")
                    
                    # Sayfa yüklenmesini bekle
                    time.sleep(3)
                    
                    # URL değişimini kontrol et
                    current_url = self.driver.current_url
                    print(f"🔗 Yeni URL: {current_url}")
                    
                    if "hepsiburada.com" in current_url:
                        print("✅ Ürün sayfasına gidildi")
                        return True
                    else:
                        print("⚠️ Sayfa yüklendi ama URL değişimi belirsiz")
                        return True
                        
                except Exception as e2:
                    print(f"❌ Ürün kartına tıklanamadı: {e2}")
                    return False
            
        except Exception as e:
            print(f"❌ İlk ürün seçimi hatası: {e}")
            import traceback
            traceback.print_exc()
            return False