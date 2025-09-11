# pages/workflow_manager.py
import time
from .hepsiburada_page import HepsiburadaPage
from .registration_page import RegistrationPage
from .login_page import LoginPage


class Timer:
    """Süre ölçme sınıfı"""
    
    def __init__(self):
        self.start_time = None
        self.step_times = {}
    
    def start(self, step_name):
        """Adımı başlat"""
        self.start_time = time.time()
        print(f"⏱️ {step_name} başlatılıyor...")
    
    def end(self, step_name):
        """Adımı bitir ve süreyi kaydet"""
        if self.start_time:
            duration = time.time() - self.start_time
            self.step_times[step_name] = duration
            print(f"✅ {step_name} tamamlandı - Süre: {duration:.2f} saniye")
            return duration
        return 0
    
    def get_total_time(self):
        """Toplam süreyi al"""
        return sum(self.step_times.values())
    
    def print_summary(self):
        """Süre özetini yazdır"""
        print("\n" + "="*60)
        print("⏱️ SÜRE ÖZETİ")
        print("="*60)
        for step, duration in self.step_times.items():
            print(f"📊 {step}: {duration:.2f} saniye")
        print(f"🏁 TOPLAM SÜRE: {self.get_total_time():.2f} saniye")
        print("="*60)


class WorkflowManager:
    """İş akışı yönetimi için ayrı sınıf"""
    
    def __init__(self, driver):
        self.driver = driver
        self.hepsiburada_page = HepsiburadaPage(driver)
        self.registration_page = RegistrationPage(driver)
        self.login_page = LoginPage(driver)
        
        # Sabit bilgiler
        self.password = "123456aA"
        self.first_name = "Kıymetli"
        self.last_name = "Stajyer"
    
    def run_full_automation(self):
        """Tam otomasyon sürecini çalıştırır"""
        print("🚀 Hepsiburada Tam Otomasyon Başlatılıyor...")
        print("=" * 60)
        print("📋 Süreç: Giriş Yap → Kategori Seç → Filtreleme → Ürün Seç → Sepete Ekle → Sepetim'e Git → Ürün Sayısını Arttır → Alışverişi Tamamla → Yeni Adres Ekle → Adres Formu Doldur → Kart Bilgilerini Gir → Kart Formu Doldur")
        print("=" * 60)
        
        total_start_time = time.time()
        
        try:
            # 1. Ana sayfaya git
            step_start = time.time()
            if not self.hepsiburada_page.go_to_hepsiburada():
                print("❌ Ana sayfaya gidilemedi")
                return False
            step_duration = time.time() - step_start
            print(f"🏠 Ana sayfaya gidildi ⏱️ {step_duration:.1f}s")
            
            # 2. Giriş yap
            step_start = time.time()
            if not self._run_login_flow():
                print("❌ Giriş yapılamadı")
                return False
            step_duration = time.time() - step_start
            print(f"🔑 Giriş yapıldı ⏱️ {step_duration:.1f}s")
            
            # 3. Ürün otomasyonu
            step_start = time.time()
            if not self._run_product_automation():
                print("⚠️ Ürün otomasyonu başarısız")
                return False
            step_duration = time.time() - step_start
            print(f"🛍️ Ürün otomasyonu tamamlandı ⏱️ {step_duration:.1f}s")
            
            # 4. Sepetim butonuna tıkla
            step_start = time.time()
            if not self.hepsiburada_page.click_sepetim_button():
                print("⚠️ Sepetim butonuna tıklanamadı")
                return False
            step_duration = time.time() - step_start
            print(f"🛒 Sepetim sayfasına gidildi ⏱️ {step_duration:.1f}s")
            
            # 5. Ürün sayısını arttır
            step_start = time.time()
            if not self.hepsiburada_page.increase_product_quantity():
                print("⚠️ Ürün sayısı arttırılamadı")
                return False
            step_duration = time.time() - step_start
            print(f"➕ Ürün sayısı arttırıldı ⏱️ {step_duration:.1f}s")
            
            # 6. Alışverişi tamamla butonuna bas
            step_start = time.time()
            if not self.hepsiburada_page.click_complete_shopping_button():
                print("⚠️ Alışverişi tamamla butonuna basılamadı")
                return False
            step_duration = time.time() - step_start
            print(f"🛒 Alışverişi tamamla butonuna basıldı ⏱️ {step_duration:.1f}s")
            
            # 7. Yeni adres ekle butonuna tıkla
            step_start = time.time()
            if not self.hepsiburada_page.click_add_new_address_button():
                print("⚠️ Yeni adres ekle butonuna tıklanamadı")
                return False
            step_duration = time.time() - step_start
            print(f"📍 Yeni adres ekle butonuna tıklandı ⏱️ {step_duration:.1f}s")
            
            # 8. Adres formunu doldur
            step_start = time.time()
            if not self.hepsiburada_page.fill_address_form():
                print("⚠️ Adres formu doldurulamadı")
                return False
            step_duration = time.time() - step_start
            print(f"📝 Adres formu dolduruldu ⏱️ {step_duration:.1f}s")
            
            # 9. Kart bilgilerini gir butonuna tıkla
            step_start = time.time()
            if not self.hepsiburada_page.click_enter_card_details_button():
                print("⚠️ Kart bilgilerini gir butonuna tıklanamadı")
                return False
            step_duration = time.time() - step_start
            print(f"💳 Kart bilgilerini gir butonuna tıklandı ⏱️ {step_duration:.1f}s")
            
            # 10. Kart formunu doldur
            step_start = time.time()
            if not self.hepsiburada_page.fill_card_form():
                print("⚠️ Kart formu doldurulamadı")
                return False
            step_duration = time.time() - step_start
            print(f"💳 Kart formu dolduruldu ⏱️ {step_duration:.1f}s")
            
            # 11. Siparişi onayla
            step_start = time.time()
            if not self.hepsiburada_page.confirm_order():
                print("⚠️ Sipariş onaylanamadı")
                return False
            step_duration = time.time() - step_start
            print(f"✅ Sipariş onaylandı ⏱️ {step_duration:.1f}s")
            
            total_duration = time.time() - total_start_time
            print("🎉 TAM OTOMASYON BAŞARILI!")
            print(f"⏱️ TOPLAM SÜRE: {total_duration:.1f} saniye")
            return True
            
        except Exception as e:
            print(f"❌ Otomasyon hatası: {e}")
            import traceback
            traceback.print_exc()
            return False
        
        finally:
            print("=" * 60)
            print("🏁 Otomasyon tamamlandı")
    
    def run_login_test(self):
        """Sadece giriş testini çalıştırır"""
        print("🔑 Hepsiburada Giriş Testi Başlatılıyor...")
        print("=" * 60)
        print("⚠️ Bu test artık TempMail kullanmıyor - sabit email ile test yapın")
        return False
    
    def run_product_selection_test(self):
        """Ürün seçimi testini çalıştırır"""
        print("🛍️ Hepsiburada Ürün Seçimi Testi Başlatılıyor...")
        print("=" * 60)
        
        try:
            # Ana sayfaya git
            self.hepsiburada_page.go_to_hepsiburada()
            
            # Dizüstü bilgisayar seçimi yap
            if self.hepsiburada_page.select_laptop_product():
                print("✅ Ürün seçimi testi başarılı!")
                return True
            else:
                print("❌ Ürün seçimi testi başarısız!")
                return False
                
        except Exception as e:
            print(f"❌ Ürün seçimi testi hatası: {e}")
            return False
    
    def run_add_to_cart_test(self):
        """Sepete ekleme testini çalıştırır"""
        print("🛒 Hepsiburada Sepete Ekleme Testi Başlatılıyor...")
        print("=" * 60)
        
        try:
            # Ana sayfaya git
            self.hepsiburada_page.go_to_hepsiburada()
            
            # Dizüstü bilgisayar seçimi yap
            if not self.hepsiburada_page.select_laptop_product():
                return False
            
            # Filtreleri uygula
            self.hepsiburada_page.apply_specific_filters(
                brand="Lenovo",
                processor="Intel Core i7"
            )
            
            # İlk ürünü seç
            if not self.hepsiburada_page.click_first_filtered_product():
                return False
            
            # Ürünü sepete ekle
            if self.hepsiburada_page.add_product_to_cart():
                print("✅ Sepete ekleme testi başarılı!")
                return True
            else:
                print("❌ Sepete ekleme testi başarısız!")
                return False
                
        except Exception as e:
            print(f"❌ Sepete ekleme testi hatası: {e}")
            return False
    
    def select_and_click_first_product(self):
        """Filtrelenmiş ürünlerden ilkini seçer"""
        print("🎯 Filtrelenmiş Ürün Seçimi Testi Başlatılıyor...")
        print("=" * 60)
        
        try:
            # Ana sayfaya git
            self.hepsiburada_page.go_to_hepsiburada()
            
            # Dizüstü bilgisayar seçimi yap
            if not self.hepsiburada_page.select_laptop_product():
                return False
            
            # Filtreleri uygula
            if not self.hepsiburada_page.apply_specific_filters(
                brand="Lenovo",
                processor="Intel Core i7"
            ):
                return False
            
            # İlk ürünü seç
            if self.hepsiburada_page.click_first_filtered_product():
                print("✅ İlk ürün başarıyla seçildi!")
                return True
            else:
                print("❌ İlk ürün seçilemedi")
                return False
                
        except Exception as e:
            print(f"❌ Ürün seçimi hatası: {e}")
            return False
    
    def run_cart_operations_test(self):
        """Sadece sepet sayfasındaki işlemleri test eder"""
        print("🛒 Hepsiburada Sepet İşlemleri Testi Başlatılıyor...")
        print("=" * 60)
        
        try:
            # Doğrudan sepet sayfasına git
            self.driver.get("https://www.hepsiburada.com/sepetim")
            time.sleep(3)
            
            # Sepet sayfasında olduğumuzu kontrol et
            current_url = self.driver.current_url.lower()
            if "cart" not in current_url and "sepet" not in current_url:
                print("❌ Sepet sayfasına gidilemedi")
                return False
            
            # Sepet işlemlerini yap
            if self.hepsiburada_page.handle_cart_page_operations():
                print("✅ Sepet işlemleri başarılı!")
                return True
            else:
                print("❌ Sepet işlemleri başarısız!")
                return False
                
        except Exception as e:
            print(f"❌ Sepet işlemleri testi hatası: {e}")
            return False
    
    def run_direct_login_test(self, email="viva.vista000@gmail.com", password="123456aA"):
        """Sabit email ve şifre ile direkt giriş testini çalıştırır"""
        print("🔑 Hepsiburada Direkt Giriş Testi Başlatılıyor...")
        print("=" * 60)
        print(f"📧 Email: {email}")
        print(f"🔒 Şifre: {password}")
        
        try:
            # 1. Ana sayfaya git
            if not self.hepsiburada_page.go_to_hepsiburada():
                return False
            
            # 2. XPath ile giriş sayfasına git
            if not self.hepsiburada_page.navigate_to_login_with_xpath():
                return False
            
            # 3. Giriş yap
            if not self._direct_login_to_hepsiburada(email, password):
                return False
            
            print("🎉 DİREKT GİRİŞ TESTİ BAŞARILI!")
            return True
            
        except Exception as e:
            print(f"❌ Direkt giriş testi hatası: {e}")
            return False
    
    def run_step_by_step_test(self):
        """Adım adım test - sadece navigasyon"""
        print("🎯 Adım Adım Test Başlatılıyor...")
        print("=" * 60)
        print("1️⃣ Hepsiburada ana sayfasına gidiliyor...")
        print("2️⃣ Çerezler kabul ediliyor...")
        print("3️⃣ Giriş Yap butonuna hover yapılıyor...")
        print("4️⃣ Submenüden Giriş Yap'a tıklanıyor...")
        print("=" * 60)
        
        try:
            # 1. Ana sayfaya git
            print("🏠 Adım 1: Hepsiburada ana sayfasına gidiliyor...")
            if not self.hepsiburada_page.go_to_hepsiburada():
                print("❌ Ana sayfaya gidilemedi")
                return False
            print("✅ Ana sayfaya gidildi")
            
            # 2. XPath ile giriş sayfasına git
            print("🔑 Adım 2-4: Giriş sayfasına yönlendiriliyor...")
            if not self.hepsiburada_page.navigate_to_login_with_xpath():
                print("❌ Giriş sayfasına yönlendirilemedi")
                return False
            print("✅ Giriş sayfasına yönlendirildi")
            
            print("🎉 ADIM ADIM TEST BAŞARILI!")
            print("✅ Tüm adımlar başarıyla tamamlandı")
            return True
            
        except Exception as e:
            print(f"❌ Adım adım test hatası: {e}")
            return False
    
    def run_full_login_test(self):
        """Tam giriş testi - tüm adımlar"""
        print("🔑 Tam Giriş Testi Başlatılıyor...")
        print("=" * 60)
        print("1️⃣ Hepsiburada ana sayfasına git")
        print("2️⃣ Çerezleri kabul et")
        print("3️⃣ Giriş Yap butonuna hover yap")
        print("4️⃣ Submenüden Giriş Yap'a tıkla")
        print("5️⃣ Email adresini gir (viva.vista000@gmail.com)")
        print("6️⃣ Şifreyi gir (123456aA)")
        print("7️⃣ Giriş yap butonuna tıkla")
        print("=" * 60)
        
        try:
            # 1. Ana sayfaya git
            print("🏠 Adım 1: Hepsiburada ana sayfasına gidiliyor...")
            if not self.hepsiburada_page.go_to_hepsiburada():
                print("❌ Ana sayfaya gidilemedi")
                return False
            print("✅ Ana sayfaya gidildi")
            
            # 2-4. XPath ile giriş sayfasına git
            print("🔑 Adım 2-4: Giriş sayfasına yönlendiriliyor...")
            if not self.hepsiburada_page.navigate_to_login_with_xpath():
                print("❌ Giriş sayfasına yönlendirilemedi")
                return False
            print("✅ Giriş sayfasına yönlendirildi")
            
            # 5-7. XPath ile giriş yap
            print("🔐 Adım 5-7: Giriş bilgileri giriliyor...")
            if not self.login_page.login_with_xpath("viva.vista000@gmail.com", "123456aA"):
                print("❌ Giriş yapılamadı")
                return False
            print("✅ Giriş yapıldı")
            
            # Google popup'ını kapat
            self.hepsiburada_page.close_google_password_popup()
            
            print("🎉 TAM GİRİŞ TESTİ BAŞARILI!")
            print("✅ Tüm adımlar başarıyla tamamlandı")
            return True
            
        except Exception as e:
            print(f"❌ Tam giriş testi hatası: {e}")
            return False
    
    # Private helper methods
    
    def _run_login_flow(self):
        """Giriş akışını çalıştırır"""
        print("🔑 Giriş akışı başlatılıyor...")
        
        try:
            # 1. XPath ile giriş sayfasına git
            if not self.hepsiburada_page.navigate_to_login_with_xpath():
                print("❌ Giriş sayfasına yönlendirilemedi")
                return False
            
            # 2. XPath ile giriş yap
            if not self.login_page.login_with_xpath("viva.vista000@gmail.com", "123456aA"):
                print("❌ Giriş yapılamadı")
                return False
            
            # 3. Google popup'ını kapat
            self.hepsiburada_page.close_google_password_popup()
            
            # 4. Fare imlecini sayfanın başka bir yerine taşı (hover sorununu önlemek için)
            self._move_cursor_away_from_login_button()
            
            print("✅ Giriş akışı tamamlandı")
            return True
            
        except Exception as e:
            print(f"❌ Giriş akışı hatası: {e}")
            return False
    
    def _direct_login_to_hepsiburada(self, email, password):
        """Sabit email ve şifre ile Hepsiburada'ya direkt giriş yapar"""
        print(f"🔑 Hepsiburada'ya direkt giriş yapılıyor... (Email: {email})")
        
        try:
            # XPath ile giriş yap
            if not self.login_page.login_with_xpath(email, password):
                return False
            
            # Google şifre kaydetme popup'ını kapat
            self.hepsiburada_page.close_google_password_popup()
            
            # Fare imlecini sayfanın başka bir yerine taşı (hover sorununu önlemek için)
            self._move_cursor_away_from_login_button()
            
            return True
            
        except Exception as e:
            print(f"❌ Direkt giriş hatası: {e}")
            return False
    
    
    def _run_product_automation(self):
        """Ürün otomasyonu çalıştırır"""
        print("🛍️ Ürün otomasyonu başlatılıyor...")
        
        try:
            # Ana sayfaya dön ve sayfa durumunu kontrol et
            step_start = time.time()
            self.hepsiburada_page.go_to_hepsiburada()
            
            # Sayfa yüklenmesini bekle
            time.sleep(3)
            
            # Mevcut URL'yi kontrol et
            current_url = self.driver.current_url
            print(f"📍 Mevcut URL: {current_url}")
            
            step_duration = time.time() - step_start
            print(f"🏠 Ana sayfaya gidildi ⏱️ {step_duration:.1f}s")
            
            # Dizüstü bilgisayar kategorisine git
            step_start = time.time()
            if not self.hepsiburada_page.select_laptop_product():
                return False
            step_duration = time.time() - step_start
            print(f"💻 Laptop kategorisi seçildi ⏱️ {step_duration:.1f}s")
            
            # Filtreleri uygula
            step_start = time.time()
            self.hepsiburada_page.apply_specific_filters(
                brand="Lenovo",
                processor="Intel Core i7"
            )
            step_duration = time.time() - step_start
            print(f"🔍 Filtreler uygulandı ⏱️ {step_duration:.1f}s")
            
            # İlk ürünün "Sepete Ekle" butonuna tıkla (direkt checkout'a gider)
            step_start = time.time()
            if not self.hepsiburada_page.click_first_filtered_product():
                return False
            step_duration = time.time() - step_start
            print(f"🎯 İlk ürünün 'Sepete Ekle' butonuna tıklandı ⏱️ {step_duration:.1f}s")
            
            # Checkout sayfasında olduğumuzu kontrol et
            step_start = time.time()
            current_url = self.driver.current_url
            if "checkout" in current_url.lower():
                step_duration = time.time() - step_start
                print(f"✅ Direkt checkout sayfasına gidildi! ⏱️ {step_duration:.1f}s")
                print(f"🎉 TAM OTOMASYON BAŞARILI - ÖDEME SAYFASINDA: {current_url}")
                return True
            else:
                step_duration = time.time() - step_start
                print(f"⚠️ Checkout sayfasına gidilemedi, mevcut URL: {current_url} ⏱️ {step_duration:.1f}s")
                return True
                
        except Exception as e:
            print(f"❌ Ürün otomasyonu hatası: {e}")
            return False
    
    def _move_cursor_away_from_login_button(self):
        """Giriş işleminden sonra fare imlecini sayfanın başka bir yerine taşır"""
        print("🖱️ Fare imleci giriş butonundan uzaklaştırılıyor...")
        
        try:
            from selenium.webdriver.common.action_chains import ActionChains
            from selenium.webdriver.common.by import By
            
            # Sayfanın logo alanına fare imlecini taşı
            actions = ActionChains(self.driver)
            
            # Logo alanını bul ve oraya taşı
            try:
                # Hepsiburada logosunu bul
                logo_element = self.driver.find_element(By.CSS_SELECTOR, "a[href='/']")
                actions.move_to_element(logo_element).perform()
                print("✅ Fare imleci logo alanına taşındı")
            except:
                # Logo bulunamazsa sayfanın sol üst köşesine taşı
                actions.move_by_offset(100, 100).perform()
                print("✅ Fare imleci sayfanın sol üst köşesine taşındı")
            
            # Kısa bir bekleme
            time.sleep(1)
            
            return True
            
        except Exception as e:
            print(f"⚠️ Fare imleci taşıma hatası (devam ediliyor): {e}")
            return True  # Bu hata kritik değil, devam edebiliriz
