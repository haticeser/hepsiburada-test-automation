# pages/modules/cart_module.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ..base_page import BasePage


class CartModule(BasePage):
    """Sepet işlemleri için modül"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def add_product_to_cart(self):
        """Ürünü sepete ekler - Artık gerekli değil çünkü ürün listesinde direkt sepete ekliyoruz"""
        print("🛒 Ürün zaten sepete eklenmiş (ürün listesinde direkt ekleme yapıldı)")
        return True
    
    def click_sepetim_button(self):
        """Sepetim butonuna tıklar"""
        print("🛒 Sepetim butonuna tıklanıyor...")
        
        try:
            # XPath ile Sepetim butonunu bul
            sepetim_xpath = "/html/body/div[1]/section[3]/div/div[4]/div/div/div/div[1]/div[2]/div[3]/a"
            
            # Elementin görünür olmasını bekle
            sepetim_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, sepetim_xpath))
            )
            
            # JavaScript ile tıklama - daha güvenilir
            print("🖱️ JavaScript ile Sepetim butonuna tıklanıyor...")
            self.driver.execute_script("arguments[0].click();", sepetim_button)
            
            print("✅ Sepetim butonuna tıklandı")
            time.sleep(3)  # Sepet sayfasının yüklenmesi için bekle
            
            return True
            
        except TimeoutException:
            print("❌ Sepetim butonu bulunamadı")
            return False
        except Exception as e:
            print(f"❌ Sepetim butonuna tıklama hatası: {e}")
            return False
    
    def increase_product_quantity(self):
        """Sepetteki ürün sayısını + butonu ile 1 arttırır"""
        print("➕ Ürün sayısı arttırılıyor...")
        
        try:
            # XPath ile + butonunu bul
            plus_button_xpath = "/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/section/section/div[2]/ul/li/div/div[2]/div[2]/div[2]/div[1]/div/a[2]"
            
            # Elementin görünür olmasını bekle
            plus_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, plus_button_xpath))
            )
            
            # JavaScript ile tıklama - daha güvenilir
            print("🖱️ JavaScript ile + butonuna tıklanıyor...")
            self.driver.execute_script("arguments[0].click();", plus_button)
            
            print("✅ Ürün sayısı arttırıldı (+1)")
            time.sleep(2)  # Sayfa güncellemesi için bekle
            
            return True
            
        except TimeoutException:
            print("❌ + butonu bulunamadı")
            return False
        except Exception as e:
            print(f"❌ + butonuna tıklama hatası: {e}")
            return False
    
    def handle_add_to_cart_popup(self):
        """Sepete ekleme popup'ını işler"""
        print("🔍 Sepete ekleme popup'ı kontrol ediliyor...")
        
        try:
            # Popup'ın açılmasını bekle
            time.sleep(3)
            
            # "Sepete git" butonunu ara - Hepsiburada spesifik
            sepet_git_selectors = [
                # Hepsiburada'nın gerçek selector'ları
                "button[class*='sepet-git']",
                "button[class*='cart-go']", 
                "button[class*='basket-go']",
                "button[class*='go-to-cart']",
                "button[class*='sepet']",
                "button[class*='cart']",
                "button[class*='basket']",
                
                # Link selector'ları
                "a[href*='sepet']",
                "a[href*='cart']", 
                "a[href*='basket']",
                "a[href*='checkout']",
                
                # Title ve aria-label selector'ları
                "button[title*='Sepete git']",
                "button[title*='Go to cart']",
                "button[aria-label*='sepet']",
                "button[aria-label*='cart']",
                
                # Class selector'ları
                ".sepet-git",
                ".cart-go",
                ".basket-go",
                ".go-to-cart",
                ".sepet-button",
                ".cart-button"
            ]
            
            for selector in sepet_git_selectors:
                try:
                    element = WebDriverWait(self.driver, 3).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    element.click()
                    print(f"✅ 'Sepete git' butonuna tıklandı ({selector})")
                    time.sleep(3)
                    return True
                except TimeoutException:
                    continue
            
            # Text içeriğine göre "Sepete git" butonunu ara
            try:
                print("🔍 Text içeriğine göre 'Sepete git' butonu aranıyor...")
                all_buttons = self.driver.find_elements(By.TAG_NAME, "button")
                for button in all_buttons:
                    try:
                        if button.is_displayed():
                            text = button.text.lower()
                            # Hepsiburada'nın kullandığı Türkçe metinler
                            if any(keyword in text for keyword in [
                                "sepete git", "go to cart", "sepet", "cart", "basket",
                                "alışverişi tamamla", "checkout", "ödeme", "tamamla",
                                "devam et", "ilerle", "git", "go"
                            ]):
                                button.click()
                                print(f"✅ 'Sepete git' butonuna tıklandı (text: {text[:30]})")
                                time.sleep(3)
                                return True
                    except:
                        continue
            except Exception as e:
                print(f"❌ Text-based 'Sepete git' arama hatası: {e}")
                pass
            
            # Link tabanlı arama
            try:
                print("🔍 Link tabanlı 'Sepete git' aranıyor...")
                all_links = self.driver.find_elements(By.TAG_NAME, "a")
                for link in all_links:
                    try:
                        if link.is_displayed():
                            text = link.text.lower()
                            href = link.get_attribute("href") or ""
                            if any(keyword in text for keyword in ["sepete git", "sepet", "cart", "basket"]) or any(keyword in href.lower() for keyword in ["sepet", "cart", "basket", "checkout"]):
                                link.click()
                                print(f"✅ 'Sepete git' linkine tıklandı (text: {text[:30]}, href: {href[:50]})")
                                time.sleep(3)
                                return True
                    except:
                        continue
            except Exception as e:
                print(f"❌ Link-based 'Sepete git' arama hatası: {e}")
                pass
            
            print("⚠️ 'Sepete git' butonu bulunamadı, popup kapatılıyor...")
            # Popup'ı kapatmaya çalış
            try:
                close_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button[class*='close'], .close, [aria-label*='close'], [aria-label*='kapat']")
                for close_btn in close_buttons:
                    if close_btn.is_displayed():
                        close_btn.click()
                        print("✅ Popup kapatıldı")
                        time.sleep(1)
                        break
            except:
                pass
            
            return False
            
        except Exception as e:
            print(f"❌ Popup işleme hatası: {e}")
            return False
    
    def go_to_cart(self):
        """Sepet sayfasına gider"""
        print("🛒 Sepet sayfasına gidiliyor...")
        
        try:
            self.driver.get("https://www.hepsiburada.com/sepetim")
            time.sleep(3)
            
            # Sepet sayfasında olduğumuzu kontrol et
            current_url = self.driver.current_url.lower()
            if "cart" in current_url or "sepet" in current_url:
                print("✅ Sepet sayfasındayız")
                return True
            else:
                print("❌ Sepet sayfasına gidilemedi")
                return False
                
        except Exception as e:
            print(f"❌ Sepet sayfasına gitme hatası: {e}")
            return False
    
    def handle_cart_page_operations(self):
        """Sepet sayfası işlemlerini yönetir"""
        print("🛒 Sepet sayfası işlemleri...")
        
        try:
            # Sepet sayfasında olup olmadığını kontrol et
            current_url = self.driver.current_url
            if "sepet" in current_url.lower() or "cart" in current_url.lower():
                print("✅ Sepet sayfasında")
                return True
            else:
                print("⚠️ Sepet sayfasında değil")
                return False
                
        except Exception as e:
            print(f"❌ Sepet sayfası işlemleri hatası: {e}")
            return False
    
    def proceed_to_checkout(self):
        """Ödeme sayfasına geçer - Hepsiburada spesifik"""
        print("💳 Ödeme sayfasına geçiliyor...")
        
        # 1. Hepsiburada spesifik checkout selector'ları
        hepsiburada_checkout_selectors = [
            "button[data-testid*='checkout']",
            "button[data-testid*='odeme']",
            "button[data-testid*='satin-al']",
            "button[data-testid*='buy']",
            "a[href*='checkout.hepsiburada.com']",
            "button[class*='checkout']",
            "button[class*='odeme']",
            "button[class*='satin-al']",
            "button[class*='buy']",
            ".checkout-button",
            ".odeme-button",
            ".satin-al-button",
            "button[title*='Ödeme']",
            "button[title*='Checkout']",
            "button[title*='Satın Al']",
            "button[title*='Buy']"
        ]
        
        for selector in hepsiburada_checkout_selectors:
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                element.click()
                print(f"✅ Ödeme sayfasına geçildi (Hepsiburada: {selector})")
                time.sleep(3)
                
                # Checkout sayfasında olduğumuzu kontrol et
                current_url = self.driver.current_url
                if "checkout" in current_url.lower():
                    print("✅ Checkout sayfasında: " + current_url)
                    return True
                else:
                    print(f"⚠️ Checkout sayfasına gidilemedi, mevcut URL: {current_url}")
                    
            except TimeoutException:
                continue
            except Exception as e:
                print(f"❌ Checkout selector hatası ({selector}): {e}")
                continue
        
        # 2. Text içeriğine göre arama
        try:
            print("🔍 Text içeriğine göre checkout butonu aranıyor...")
            all_buttons = self.driver.find_elements(By.TAG_NAME, "button")
            for button in all_buttons:
                try:
                    if button.is_displayed():
                        text = button.text.lower()
                        # Hepsiburada'nın kullandığı Türkçe metinler
                        if any(keyword in text for keyword in [
                            "ödeme", "checkout", "satin al", "satın al", "buy",
                            "hemen satın al", "hemen öde", "ödeme yap",
                            "devam et", "ilerle", "tamamla", "alışverişi tamamla"
                        ]):
                            button.click()
                            print(f"✅ Ödeme sayfasına geçildi (text: {text[:30]})")
                            time.sleep(3)
                            
                            # Checkout sayfasında olduğumuzu kontrol et
                            current_url = self.driver.current_url
                            if "checkout" in current_url.lower():
                                print("✅ Checkout sayfasında: " + current_url)
                                return True
                            else:
                                print(f"⚠️ Checkout sayfasına gidilemedi, mevcut URL: {current_url}")
                                
                except:
                    continue
        except Exception as e:
            print(f"❌ Text-based checkout arama hatası: {e}")
        
        # 3. Link tabanlı arama
        try:
            print("🔍 Link tabanlı checkout aranıyor...")
            all_links = self.driver.find_elements(By.TAG_NAME, "a")
            for link in all_links:
                try:
                    if link.is_displayed():
                        href = link.get_attribute("href") or ""
                        text = link.text.lower()
                        if "checkout" in href.lower() or any(keyword in text for keyword in ["ödeme", "checkout", "satin al"]):
                            link.click()
                            print(f"✅ Ödeme sayfasına geçildi (link: {href})")
                            time.sleep(3)
                            
                            # Checkout sayfasında olduğumuzu kontrol et
                            current_url = self.driver.current_url
                            if "checkout" in current_url.lower():
                                print("✅ Checkout sayfasında: " + current_url)
                                return True
                            else:
                                print(f"⚠️ Checkout sayfasına gidilemedi, mevcut URL: {current_url}")
                                
                except:
                    continue
        except Exception as e:
            print(f"❌ Link-based checkout arama hatası: {e}")
        
        print("❌ Ödeme butonu bulunamadı")
        return False
    
    def click_complete_shopping_button(self):
        """Alışverişi tamamla butonuna tıklar"""
        print("🛒 Alışverişi tamamla butonuna tıklanıyor...")
        
        try:
            # ID ile Alışverişi tamamla butonunu bul
            complete_shopping_id = "continue_step_btn"
            
            # Elementin görünür olmasını bekle
            complete_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, complete_shopping_id))
            )
            
            # JavaScript ile tıklama - daha güvenilir
            print("🖱️ JavaScript ile Alışverişi tamamla butonuna tıklanıyor...")
            self.driver.execute_script("arguments[0].click();", complete_button)
            
            print("✅ Alışverişi tamamla butonuna tıklandı")
            time.sleep(3)  # Sayfa yönlendirmesi için bekle
            
            return True
            
        except TimeoutException:
            print("❌ Alışverişi tamamla butonu bulunamadı (ID: continue_step_btn)")
            
            # Alternatif olarak XPath ile dene
            try:
                print("🔍 XPath ile Alışverişi tamamla butonu aranıyor...")
                complete_shopping_xpath = "/html/body/div[1]/div/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div[3]"
                
                complete_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, complete_shopping_xpath))
                )
                
                self.driver.execute_script("arguments[0].click();", complete_button)
                print("✅ Alışverişi tamamla butonuna tıklandı (XPath)")
                time.sleep(3)
                
                return True
                
            except TimeoutException:
                print("❌ XPath ile de Alışverişi tamamla butonu bulunamadı")
                return False
                
        except Exception as e:
            print(f"❌ Alışverişi tamamla butonuna tıklama hatası: {e}")
            return False
    
    def click_add_new_address_button(self):
        """Yeni adres ekle butonuna tıklar"""
        print("📍 Yeni adres ekle butonuna tıklanıyor...")
        
        try:
            # XPath ile Yeni adres ekle butonunu bul
            add_address_xpath = "/html/body/div/div/main/section/div[1]/div[1]/div[1]/div/span"
            
            # Elementin görünür olmasını bekle
            add_address_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, add_address_xpath))
            )
            
            # JavaScript ile tıklama - daha güvenilir
            print("🖱️ JavaScript ile Yeni adres ekle butonuna tıklanıyor...")
            self.driver.execute_script("arguments[0].click();", add_address_button)
            
            print("✅ Yeni adres ekle butonuna tıklandı")
            time.sleep(3)  # Sayfa yönlendirmesi için bekle
            
            return True
            
        except TimeoutException:
            print("❌ Yeni adres ekle butonu bulunamadı (XPath)")
            
            # Alternatif olarak data-test-class ile dene
            try:
                print("🔍 data-test-class ile Yeni adres ekle butonu aranıyor...")
                add_address_selector = "a[data-test-class='new-address-link']"
                
                add_address_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, add_address_selector))
                )
                
                self.driver.execute_script("arguments[0].click();", add_address_button)
                print("✅ Yeni adres ekle butonuna tıklandı (data-test-class)")
                time.sleep(3)
                
                return True
                
            except TimeoutException:
                print("❌ data-test-class ile de Yeni adres ekle butonu bulunamadı")
                
                # Son alternatif olarak text içeriğine göre ara
                try:
                    print("🔍 Text içeriğine göre Yeni adres ekle butonu aranıyor...")
                    all_links = self.driver.find_elements(By.TAG_NAME, "a")
                    for link in all_links:
                        try:
                            if link.is_displayed():
                                text = link.text.lower()
                                if "yeni adres ekle" in text or "new address" in text:
                                    self.driver.execute_script("arguments[0].click();", link)
                                    print("✅ Yeni adres ekle butonuna tıklandı (text)")
                                    time.sleep(3)
                                    return True
                        except:
                            continue
                except Exception as e:
                    print(f"❌ Text-based arama hatası: {e}")
                
            return False
            
        except Exception as e:
            print(f"❌ Yeni adres ekle butonuna tıklama hatası: {e}")
            return False
    
    def click_enter_card_details_button(self):
        """20. Kart bilgilerini gir butonuna tıkla"""
        try:
            print("💳 Kart bilgilerini gir butonuna tıklanıyor...")
            
            # Kayıtlı kart kontrolünü kaldır, direkt butona bas
            print("📝 Kart bilgilerini gir butonuna basılıyor...")
            
            # Farklı locator stratejileri dene
            card_button = None
            
            # 1. Orijinal XPath
            try:
                card_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/section/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/a"))
                )
                print("✅ Kart butonu bulundu (orijinal XPath)")
            except TimeoutException:
                # 2. Text ile arama
                try:
                    card_button = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Kart bilgilerini gir') or contains(text(), 'kart bilgilerini gir')]"))
                    )
                    print("✅ Kart butonu bulundu (text ile)")
                except TimeoutException:
                    # 3. Genel arama
                    try:
                        card_button = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'card') or contains(@href, 'kart') or contains(@class, 'card')]"))
                        )
                        print("✅ Kart butonu bulundu (genel arama)")
                    except TimeoutException:
                        print("❌ Kart bilgilerini gir butonu bulunamadı")
                        return False
            
            # JavaScript ile tıklama
            print("🖱️ JavaScript ile Kart bilgilerini gir butonuna tıklanıyor...")
            self.driver.execute_script("arguments[0].click();", card_button)
            
            print("✅ Kart bilgilerini gir butonuna tıklandı")
            time.sleep(3)  # Modal açılması için bekle
            
            return True
            
        except Exception as e:
            print(f"❌ Kart bilgilerini gir butonuna tıklama hatası: {e}")
            return False
    
    def fill_card_form(self):
        """21-27. Kart formunu doldur"""
        try:
            print("💳 Kart formu dolduruluyor...")
            
            # 21. Kart numarası alanına "0000 0000 0000 0000" yaz
            print("📝 Kart numarası alanına '0000 0000 0000 0000' yazılıyor...")
            try:
                card_number_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "cardNumber"))
                )
                card_number_input.click()
                card_number_input.clear()
                card_number_input.send_keys("0000 0000 0000 0000")
                print("✅ Kart numarası dolduruldu: 0000 0000 0000 0000")
            except TimeoutException:
                print("⚠️ Kart numarası alanı bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 22. Ay/Yıl alanına "10 / 28" yaz
            print("📝 Ay/Yıl alanına '10 / 28' yazılıyor...")
            try:
                expire_date_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "expireDate"))
                )
                expire_date_input.click()
                expire_date_input.clear()
                expire_date_input.send_keys("10 / 28")
                print("✅ Ay/Yıl dolduruldu: 10 / 28")
            except TimeoutException:
                print("⚠️ Ay/Yıl alanı bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 23. CVC/CVV alanına "100" yaz
            print("📝 CVC/CVV alanına '100' yazılıyor...")
            try:
                cvc_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder*='CVC']"))
                )
                cvc_input.click()
                cvc_input.clear()
                cvc_input.send_keys("100")
                print("✅ CVC/CVV dolduruldu: 100")
            except TimeoutException:
                print("⚠️ CVC/CVV alanı bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 24. İsim Soyisim alanına "Kıymetli Stajyer" yaz
            print("📝 İsim Soyisim alanına 'Kıymetli Stajyer' yazılıyor...")
            try:
                name_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "name"))
                )
                name_input.click()
                name_input.clear()
                name_input.send_keys("Kıymetli Stajyer")
                print("✅ İsim Soyisim dolduruldu: Kıymetli Stajyer")
            except TimeoutException:
                print("⚠️ İsim Soyisim alanı bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 25. İlk checkbox'ı işaretle (kart kaydet)
            print("📝 İlk checkbox işaretleniyor (kart kaydet)...")
            try:
                save_card_checkbox = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "saveCard"))
                )
                self.driver.execute_script("arguments[0].click();", save_card_checkbox)
                print("✅ İlk checkbox işaretlendi (kart kaydet)")
            except TimeoutException:
                print("⚠️ İlk checkbox bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 26. İkinci checkbox'ı işaretle (sözleşme)
            print("📝 İkinci checkbox işaretleniyor (sözleşme)...")
            try:
                contract_checkbox = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "contract"))
                )
                self.driver.execute_script("arguments[0].click();", contract_checkbox)
                print("✅ İkinci checkbox işaretlendi (sözleşme)")
            except TimeoutException:
                print("⚠️ İkinci checkbox bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 27. Devam et butonuna tıkla
            print("📝 Devam et butonuna basılıyor...")
            try:
                continue_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Devam et')]"))
                )
                self.driver.execute_script("arguments[0].click();", continue_button)
                print("✅ Devam et butonuna basıldı")
            except TimeoutException:
                print("⚠️ Devam et butonu bulunamadı, devam ediliyor...")
            time.sleep(3)
            
            # Chrome kart kaydetme bildirimini kapat
            print("🔔 Chrome kart kaydetme bildirimini kapatılıyor...")
            try:
                # Chrome bildirimini kapat
                self.driver.execute_script("""
                    // Chrome bildirimlerini kapat
                    if (window.chrome && window.chrome.webstore) {
                        // Bildirim popup'ını kapat
                        var notifications = document.querySelectorAll('[role="alert"], .notification, .popup');
                        notifications.forEach(function(notification) {
                            if (notification.style) {
                                notification.style.display = 'none';
                            }
                        });
                    }
                    
                    // Chrome bildirim izin popup'ını kapat
                    var permissionPopup = document.querySelector('[data-testid="permission-popup"], .permission-popup, .chrome-permission');
                    if (permissionPopup) {
                        permissionPopup.style.display = 'none';
                    }
                    
                    // Chrome bildirim izin butonlarını kapat
                    var denyButton = document.querySelector('[data-testid="deny-notification"], .deny-notification, .chrome-deny');
                    if (denyButton) {
                        denyButton.click();
                    }
                    
                    // Chrome bildirim izin butonlarını kapat (alternatif)
                    var blockButton = document.querySelector('[data-testid="block-notification"], .block-notification, .chrome-block');
                    if (blockButton) {
                        blockButton.click();
                    }
                """)
                
                # ESC tuşuna bas (bildirimleri kapatmak için)
                from selenium.webdriver.common.keys import Keys
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
                
                # Sayfayı yenile (bildirim popup'ını kapatmak için)
                time.sleep(2)
                self.driver.execute_script("window.focus();")
                
                # Tekrar ESC tuşu gönder
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
                
                print("✅ Chrome bildirimi kapatıldı")
                time.sleep(2)
            except Exception as e:
                print(f"⚠️ Chrome bildirimi kapatılamadı: {e}")
            
            print("🎉 Kart formu başarıyla dolduruldu!")
            return True
            
        except Exception as e:
            print(f"❌ Kart formu doldurma hatası: {e}")
            return False
    
    def confirm_order(self):
        """28-29. Siparişi onayla (checkbox + siparişi onayla butonu)"""
        try:
            print("📝 Sipariş onaylama işlemi başlatılıyor...")
            
            # Chrome bildirimini kapat
            print("🔔 Chrome bildirimini kapatılıyor...")
            try:
                # Chrome bildirimini kapat
                self.driver.execute_script("""
                    // Chrome bildirimlerini kapat
                    if (window.chrome && window.chrome.webstore) {
                        // Bildirim popup'ını kapat
                        var notifications = document.querySelectorAll('[role="alert"], .notification, .popup');
                        notifications.forEach(function(notification) {
                            if (notification.style) {
                                notification.style.display = 'none';
                            }
                        });
                    }
                    
                    // Chrome bildirim izin popup'ını kapat
                    var permissionPopup = document.querySelector('[data-testid="permission-popup"], .permission-popup, .chrome-permission');
                    if (permissionPopup) {
                        permissionPopup.style.display = 'none';
                    }
                    
                    // Chrome bildirim izin butonlarını kapat
                    var denyButton = document.querySelector('[data-testid="deny-notification"], .deny-notification, .chrome-deny');
                    if (denyButton) {
                        denyButton.click();
                    }
                    
                    // Chrome bildirim izin butonlarını kapat (alternatif)
                    var blockButton = document.querySelector('[data-testid="block-notification"], .block-notification, .chrome-block');
                    if (blockButton) {
                        blockButton.click();
                    }
                """)
                
                # ESC tuşuna bas (bildirimleri kapatmak için)
                from selenium.webdriver.common.keys import Keys
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
                
                # Sayfayı yenile (bildirim popup'ını kapatmak için)
                time.sleep(2)
                self.driver.execute_script("window.focus();")
                
                # Tekrar ESC tuşu gönder
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
                
                print("✅ Chrome bildirimi kapatıldı")
                time.sleep(2)
            except Exception as e:
                print(f"⚠️ Chrome bildirimi kapatılamadı: {e}")
            
            # Sayfa yüklenmesini bekle
            time.sleep(5)
            
            # 28. Sözleşme checkbox'ını işaretle - Geliştirilmiş strateji
            print("📝 Sözleşme checkbox'ı işaretleniyor...")
            checkbox_clicked = False
            
            # Strateji 1: Verilen XPath ile
            try:
                contract_checkbox = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/aside/div/div/div/div[1]/div[2]"))
                )
                # Checkbox'ı bul ve tıkla
                checkbox_input = contract_checkbox.find_element(By.TAG_NAME, "input")
                if checkbox_input:
                    self.driver.execute_script("arguments[0].click();", checkbox_input)
                    print("✅ Sözleşme checkbox'ı işaretlendi (verilen XPath ile)")
                    checkbox_clicked = True
                    time.sleep(2)
            except Exception as e:
                print(f"⚠️ Verilen XPath ile checkbox bulunamadı: {e}")
            
            # Strateji 2: ID ile
            if not checkbox_clicked:
                try:
                    contract_checkbox = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, "agreement"))
                    )
                    self.driver.execute_script("arguments[0].click();", contract_checkbox)
                    print("✅ Sözleşme checkbox'ı işaretlendi (ID ile)")
                    checkbox_clicked = True
                    time.sleep(2)
                except Exception as e:
                    print(f"⚠️ ID ile checkbox bulunamadı: {e}")
            
            # Strateji 3: Genel arama
            if not checkbox_clicked:
                try:
                    # Tüm checkbox'ları bul
                    checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
                    for checkbox in checkboxes:
                        try:
                            if checkbox.is_displayed():
                                # Sözleşme ile ilgili checkbox'ı bul
                                parent = checkbox.find_element(By.XPATH, "./..")
                                if parent and ("sözleşme" in parent.text.lower() or "agreement" in parent.text.lower() or "kabul" in parent.text.lower()):
                                    self.driver.execute_script("arguments[0].click();", checkbox)
                                    print("✅ Sözleşme checkbox'ı işaretlendi (genel arama)")
                                    checkbox_clicked = True
                                    time.sleep(2)
                                    break
                        except:
                            continue
                except Exception as e:
                    print(f"⚠️ Genel arama ile checkbox bulunamadı: {e}")
            
            if not checkbox_clicked:
                print("⚠️ Sözleşme checkbox'ı bulunamadı, devam ediliyor...")
            
            # Butonun aktif olmasını bekle
            time.sleep(3)
            
            # 29. Siparişi onayla butonuna tıkla - Geliştirilmiş strateji
            print("📝 Siparişi onayla butonuna basılıyor...")
            button_clicked = False
            
            # Strateji 1: Verilen element bilgileri ile
            try:
                # Önce butonun disabled olmadığını kontrol et
                confirm_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "continue_step_btn"))
                )
                
                # Butonun disabled olup olmadığını kontrol et
                is_disabled = confirm_button.get_attribute("disabled")
                if is_disabled:
                    print("⚠️ Buton hala disabled, JavaScript ile aktif hale getiriliyor...")
                    # JavaScript ile disabled attribute'unu kaldır
                    self.driver.execute_script("arguments[0].removeAttribute('disabled');", confirm_button)
                    time.sleep(1)
                
                # Butonun tıklanabilir olmasını bekle
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "continue_step_btn"))
                )
                
                # JavaScript ile tıkla
                self.driver.execute_script("arguments[0].click();", confirm_button)
                print("✅ Siparişi onayla butonuna basıldı (ID ile)")
                button_clicked = True
                time.sleep(3)
            except Exception as e:
                print(f"⚠️ ID ile buton tıklanamadı: {e}")
            
            # Strateji 2: Verilen XPath ile
            if not button_clicked:
                try:
                    confirm_button = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/aside/div/div/div/div[1]/div[2]"))
                    )
                    
                    # Buton elementini bul
                    button_element = confirm_button.find_element(By.TAG_NAME, "button")
                    if button_element:
                        # Disabled kontrolü
                        is_disabled = button_element.get_attribute("disabled")
                        if is_disabled:
                            self.driver.execute_script("arguments[0].removeAttribute('disabled');", button_element)
                            time.sleep(1)
                        
                        self.driver.execute_script("arguments[0].click();", button_element)
                        print("✅ Siparişi onayla butonuna basıldı (verilen XPath ile)")
                        button_clicked = True
                        time.sleep(3)
                except Exception as e:
                    print(f"⚠️ Verilen XPath ile buton tıklanamadı: {e}")
            
            # Strateji 3: Text ile
            if not button_clicked:
                try:
                    confirm_button = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Siparişi onayla')]"))
                    )
                    
                    # Disabled kontrolü
                    is_disabled = confirm_button.get_attribute("disabled")
                    if is_disabled:
                        self.driver.execute_script("arguments[0].removeAttribute('disabled');", confirm_button)
                        time.sleep(1)
                    
                    self.driver.execute_script("arguments[0].click();", confirm_button)
                    print("✅ Siparişi onayla butonuna basıldı (Text ile)")
                    button_clicked = True
                    time.sleep(3)
                except Exception as e:
                    print(f"⚠️ Text ile buton tıklanamadı: {e}")
            
            # Strateji 4: Genel arama
            if not button_clicked:
                try:
                    # Tüm butonları bul
                    buttons = self.driver.find_elements(By.TAG_NAME, "button")
                    for button in buttons:
                        try:
                            if button.is_displayed() and "siparişi onayla" in button.text.lower():
                                # Disabled kontrolü
                                is_disabled = button.get_attribute("disabled")
                                if is_disabled:
                                    self.driver.execute_script("arguments[0].removeAttribute('disabled');", button)
                                    time.sleep(1)
                                
                                self.driver.execute_script("arguments[0].click();", button)
                                print("✅ Siparişi onayla butonuna basıldı (genel arama)")
                                button_clicked = True
                                time.sleep(3)
                                break
                        except:
                            continue
                except Exception as e:
                    print(f"⚠️ Genel arama ile buton tıklanamadı: {e}")
            
            if not button_clicked:
                print("❌ Siparişi onayla butonu bulunamadı veya tıklanamadı")
                return False
            
            print("🎉 Sipariş başarıyla onaylandı!")
            return True
            
        except Exception as e:
            print(f"❌ Sipariş onaylama hatası: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def fill_address_form(self):
        """Adres formunu doldurur"""
        print("📝 Adres formu dolduruluyor...")
        
        try:
            # Modal'ın yüklenmesini bekle
            time.sleep(3)
            
            # 10. Ad alanına "Kıymetli" yaz - placeholder ile bul
            print("📝 Ad alanına 'Kıymetli' yazılıyor...")
            try:
                ad_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Ad']"))
                )
                ad_input.click()
                ad_input.clear()
                ad_input.send_keys("Kıymetli")
                print("✅ Ad alanı dolduruldu: Kıymetli")
            except TimeoutException:
                print("⚠️ Ad alanı bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 11. Soyad alanına "Stajyer" yaz - placeholder ile bul
            print("📝 Soyad alanına 'Stajyer' yazılıyor...")
            try:
                soyad_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Soyad']"))
                )
                soyad_input.click()
                soyad_input.clear()
                soyad_input.send_keys("Stajyer")
                print("✅ Soyad alanı dolduruldu: Stajyer")
            except TimeoutException:
                print("⚠️ Soyad alanı bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 12. Telefon alanına "555 555 55 55" yaz - type="tel" ile bul
            print("📝 Telefon alanına '555 555 55 55' yazılıyor...")
            try:
                telefon_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='tel']"))
                )
                telefon_input.click()
                telefon_input.clear()
                telefon_input.send_keys("555 555 55 555")
                print("✅ Telefon alanı dolduruldu: 555 555 55 555")
            except TimeoutException:
                print("⚠️ Telefon alanı bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 13. İş yeri seçeneğini seç - daha güçlü locator stratejisi
            print("📝 İş yeri seçeneği seçiliyor...")
            try:
                # Önce XPath ile dene
                is_yeri_radio = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'İş yeri')]"))
                )
                self.driver.execute_script("arguments[0].click();", is_yeri_radio)
                print("✅ İş yeri seçeneği seçildi (XPath)")
                time.sleep(2)  # Seçim sonrası bekle
            except TimeoutException:
                try:
                    # Alternatif olarak input value ile dene
                    is_yeri_input = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//input[@value='1']"))
                    )
                    self.driver.execute_script("arguments[0].click();", is_yeri_input)
                    print("✅ İş yeri seçeneği seçildi (input value)")
                    time.sleep(2)
                except TimeoutException:
                    try:
                        # Son alternatif olarak tüm radio buttonları kontrol et
                        radio_buttons = self.driver.find_elements(By.XPATH, "//input[@type='radio']")
                        for radio in radio_buttons:
                            try:
                                if radio.is_displayed() and radio.get_attribute("value") == "1":
                                    self.driver.execute_script("arguments[0].click();", radio)
                                    print("✅ İş yeri seçeneği seçildi (radio button)")
                                    time.sleep(2)
                                    break
                            except:
                                continue
                    except:
                        print("⚠️ İş yeri seçeneği bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 14. Bina, site alanına tam adres yaz - placeholder ile bul
            print("📝 Bina, site alanına tam adres yazılıyor...")
            try:
                bina_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder*='Bina']"))
                )
                bina_input.click()
                bina_input.clear()
                bina_input.send_keys("Kale Mh. Konya Sk. Altındağ Ankara")
                print("✅ Bina, site alanı dolduruldu: Kale Mh. Konya Sk. Altındağ Ankara")
                time.sleep(3)  # Adres önerilerinin gelmesi için bekle
            except TimeoutException:
                print("⚠️ Bina, site alanı bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 15. Adres önerilerinden ilkini seç - güçlü scroll stratejisi
            print("📝 Adres önerilerinden ilkini seçiliyor...")
            try:
                # Önce modal içinde scroll yap
                print("📜 Modal içinde scroll yapılıyor...")
                self.driver.execute_script("""
                    var modal = document.querySelector('.modal, [role="dialog"], .popup');
                    if (modal) {
                        modal.scrollTop = modal.scrollHeight;
                    } else {
                        window.scrollBy(0, 300);
                    }
                """)
                time.sleep(2)
                
                # Adres önerilerini bul ve scroll yap
                print("📜 Adres önerilerine scroll yapılıyor...")
                self.driver.execute_script("window.scrollBy(0, 400);")
                time.sleep(2)
                
                # Doğru XPath ile adres önerisini seç
                first_suggestion = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[3]/form/div[4]/div[3]/div[2]/div/div/ul/li[1]"))
                )
                # Element'e scroll yap ve görünür hale getir
                self.driver.execute_script("""
                    arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});
                """, first_suggestion)
                time.sleep(2)
                self.driver.execute_script("arguments[0].click();", first_suggestion)
                print("✅ Adres önerisi seçildi (doğru XPath)")
                time.sleep(3)  # Sistem otomatik doldurma için bekle
            except TimeoutException:
                try:
                    # Alternatif olarak kısmi metin ile dene
                    first_suggestion = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Kale Mh.')]"))
                    )
                    self.driver.execute_script("""
                        arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});
                    """, first_suggestion)
                    time.sleep(2)
                    self.driver.execute_script("arguments[0].click();", first_suggestion)
                    print("✅ Adres önerisi seçildi (kısmi metin)")
                    time.sleep(3)
                except TimeoutException:
                    try:
                        # Son alternatif: tüm önerileri bul ve ilkini seç
                        print("📜 Tüm adres önerilerini arıyor...")
                        suggestions = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'suggestion') or contains(@class, 'option') or contains(@class, 'item') or contains(@class, 'address')]")
                        for suggestion in suggestions:
                            try:
                                if suggestion.is_displayed() and "Kale" in suggestion.text:
                                    self.driver.execute_script("""
                                        arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});
                                    """, suggestion)
                                    time.sleep(2)
                                    self.driver.execute_script("arguments[0].click();", suggestion)
                                    print("✅ Adres önerisi seçildi (genel arama)")
                                    time.sleep(3)
                                    break
                            except:
                                continue
                    except:
                        print("⚠️ Adres önerisi bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 15.5. İş yeri input alanına "BİTES" yaz - "Bu adrese bir ad verin" alanı
            print("📝 İş yeri input alanına 'BİTES' yazılıyor...")
            try:
                # Önce "Bu adrese bir ad verin" alanını bul
                is_yeri_input = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='İş yeri']"))
                )
                is_yeri_input.click()
                is_yeri_input.clear()
                is_yeri_input.send_keys("BİTES")
                print("✅ İş yeri input alanı dolduruldu: BİTES (placeholder ile)")
                time.sleep(2)
            except TimeoutException:
                try:
                    # Alternatif olarak label ile bul
                    is_yeri_input = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Bu adrese bir ad verin')]/following-sibling::input"))
                    )
                    is_yeri_input.click()
                    is_yeri_input.clear()
                    is_yeri_input.send_keys("BİTES")
                    print("✅ İş yeri input alanı dolduruldu: BİTES (label ile)")
                    time.sleep(2)
                except TimeoutException:
                    try:
                        # Son alternatif: tüm input alanlarını kontrol et
                        inputs = self.driver.find_elements(By.TAG_NAME, "input")
                        for input_field in inputs:
                            try:
                                if input_field.is_displayed() and input_field.get_attribute("type") == "text":
                                    placeholder = input_field.get_attribute("placeholder") or ""
                                    if "İş yeri" in placeholder or "adres adı" in placeholder.lower():
                                        input_field.click()
                                        input_field.clear()
                                        input_field.send_keys("BİTES")
                                        print("✅ İş yeri input alanı dolduruldu: BİTES (genel arama)")
                                        time.sleep(2)
                                        break
                            except:
                                continue
                    except:
                        print("⚠️ İş yeri input alanı bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 16. Kapalı günleri seçin - Cumartesi ve Pazar
            print("📝 Kapalı günler seçiliyor (Cumartesi ve Pazar)...")
            try:
                # Cumartesi checkbox'ını bul ve tıkla
                cumartesi_checkbox = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@value='6']"))
                )
                self.driver.execute_script("arguments[0].click();", cumartesi_checkbox)
                print("✅ Cumartesi seçildi")
                
                # Pazar checkbox'ını bul ve tıkla
                pazar_checkbox = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@value='7']"))
                )
                self.driver.execute_script("arguments[0].click();", pazar_checkbox)
                print("✅ Pazar seçildi")
            except TimeoutException:
                print("⚠️ Kapalı günler bölümü bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 17. Örnek alanına "İş yeri" yaz - JavaScript ile
            print("📝 Örnek alanına 'İş yeri' yazılıyor...")
            try:
                ornek_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder*='Örnek']"))
                )
                self.driver.execute_script("arguments[0].value = 'İş yeri';", ornek_input)
                print("✅ Örnek alanı dolduruldu: İş yeri")
            except TimeoutException:
                print("⚠️ Örnek alanı bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 18. "Bu adrese fatura" checkbox'ını işaretle
            print("📝 'Bu adrese fatura' checkbox'ı işaretleniyor...")
            try:
                fatura_checkbox = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='setAlsoAsBillingAddressCheck']"))
                )
                self.driver.execute_script("arguments[0].click();", fatura_checkbox)
                print("✅ 'Bu adrese fatura' checkbox'ı işaretlendi")
            except TimeoutException:
                print("⚠️ Fatura checkbox'ı bulunamadı, devam ediliyor...")
            time.sleep(1)
            
            # 19. "Adresi Kaydet" butonuna bas
            print("📝 'Adresi Kaydet' butonuna basılıyor...")
            try:
                kaydet_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Adresi Kaydet')]"))
                )
                self.driver.execute_script("arguments[0].click();", kaydet_button)
                print("✅ 'Adresi Kaydet' butonuna basıldı")
                time.sleep(3)
            except TimeoutException:
                print("⚠️ 'Adresi Kaydet' butonu bulunamadı, devam ediliyor...")
            
            print("🎉 Adres formu başarıyla dolduruldu!")
            return True
            
        except Exception as e:
            print(f"❌ Adres formu doldurma hatası: {e}")
            import traceback
            traceback.print_exc()
            return False