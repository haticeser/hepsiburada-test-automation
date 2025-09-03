# pages/hepsiburada_automation.py
import time
from .tempail_page import TempailPage
from .hepsiburada_page import HepsiburadaPage
from .registration_page import RegistrationPage
from .login_page import LoginPage
from selenium.webdriver.common.by import By


class HepsiburadaAutomation:
    """Hepsiburada tam otomasyon sınıfı"""
    
    def __init__(self, driver):
        self.driver = driver
        self.tempail_page = TempailPage(driver)
        self.hepsiburada_page = HepsiburadaPage(driver)
        self.registration_page = RegistrationPage(driver)
        self.login_page = LoginPage(driver)
        
        # Sabit bilgiler
        self.password = "123456aA"
        self.first_name = "Kıymetli"
        self.last_name = "Stajyer"
        self.temp_email = None
    
    def get_temp_email(self):
        """Tempail'den geçici email alır"""
        # Yeni sekme aç ve Tempail'e git
        self.driver.execute_script("window.open('', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        email = self.tempail_page.get_temp_email()
        
        # Ana sekmeye geri dön
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        return email
    
    def wait_for_email_with_code(self, timeout=120):
        """Doğrulama kodu içeren email bekler"""
        # Tempail sekmesine geç
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        
        code = self.tempail_page.wait_for_email_with_code(timeout)
        
        # Ana sekmeye geri dön
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        return code
    
    def register_on_hepsiburada(self):
        """Hepsiburada'da yeni üye kaydı formunu doldurur"""
        print("🚀 Hepsiburada üye kaydı formu dolduruluyor...")
        
        try:
            # Hepsiburada ana sayfasına git
            self.hepsiburada_page.go_to_hepsiburada()
            
            # Üye ol sayfasına yönlendir
            self.hepsiburada_page.navigate_to_registration()
            
            # Email adresini gir
            if not self.registration_page.enter_email(self.temp_email):
                print("❌ Email girilemedi")
                return False
            
            # Devam et butonuna tıkla
            if not self.registration_page.click_continue_button():
                print("❌ Devam et butonuna tıklanamadı")
                return False
            
            # Şifre adımını atla - doğrudan doğrulama kodu beklemeye geç
            print("⏭️ Şifre adımı atlanıyor, doğrulama kodu bekleniyor...")
            
            # Doğrulama kodu alanının yüklenmesini bekle
            time.sleep(5)
            
            # Doğrulama kodu alanı var mı kontrol et
            try:
                code_input = self.driver.find_element(By.CSS_SELECTOR, "#txtCode")
                if code_input:
                    print("✅ Doğrulama kodu alanı bulundu, şifre adımı atlandı")
                    return True
            except:
                print("⚠ Doğrulama kodu alanı henüz yüklenmedi, bekleniyor...")
            
            print("✅ Üye kaydı formu başarıyla dolduruldu")
            print("📧 Şimdi Tempail sekmesinde doğrulama emaili bekleniyor...")
            
            return True
            
        except Exception as e:
            print(f"❌ Üye kaydı hatası: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def complete_registration_with_code(self, verification_code):
        """Doğrulama kodu ile üye kaydını tamamlar"""
        print(f"🔐 Doğrulama kodu ile üye kaydı tamamlanıyor: {verification_code}")
        
        try:
            # Hepsiburada sekmesine geri dön
            print("🔄 Hepsiburada sekmesine geçiliyor...")
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            
            # Doğrulama kodunu gir
            if not self.registration_page.enter_verification_code(verification_code):
                print("❌ Doğrulama kodu girilemedi")
                return False
            
            # E-posta doğrulama butonuna tıkla
            if not self.registration_page.click_verify_email_button():
                print("❌ E-posta doğrulama butonuna tıklanamadı")
                return False
            
            print("✅ E-posta doğrulama tamamlandı!")
            
            # Kişisel bilgileri doldur
            print("📝 Kişisel bilgiler dolduruluyor...")
            if not self.registration_page.fill_personal_info(self.first_name, self.last_name, self.password):
                print("❌ Kişisel bilgiler doldurulamadı")
                return False
            
            # Elektronik ileti checkbox'ını işaretle
            self.registration_page.check_email_subscription()
            
            # Üye ol butonuna tıkla
            if not self.registration_page.click_final_signup_button():
                print("❌ Üye ol butonuna tıklanamadı")
                return False
            
            print("✅ Üye ol butonuna tıklandı!")
            
            # Google şifre kaydetme popup'ını kapat
            self.hepsiburada_page.close_google_password_popup()
            
            # Üye ol sonrası ek doğrulama kodu kontrolü
            print("🔍 Üye ol sonrası ek doğrulama kontrol ediliyor...")
            extra_code_input = self.registration_page.check_extra_verification_needed()
            
            if extra_code_input:
                print("📧 Ek doğrulama kodu bekleniyor...")
                
                # Ek doğrulama kodunu bekle
                extra_verification_code = self.wait_for_email_with_code(120)
                
                if extra_verification_code:
                    # Ek kodu gir
                    if not self.registration_page.enter_extra_verification_code(extra_verification_code):
                        print("❌ Ek doğrulama kodu girilemedi")
                        return False
                    
                    # Ek doğrulama butonuna tıkla
                    if not self.registration_page.click_extra_verify_button():
                        print("❌ Ek doğrulama butonuna tıklanamadı")
                        return False
                else:
                    print("❌ Ek doğrulama kodu bulunamadı")
                    return False
            else:
                print("✅ Ek doğrulama kodu alanı bulunamadı, devam ediliyor...")
            
            # Başarı kontrolü
            return self.hepsiburada_page.check_registration_success()
                
        except Exception as e:
            print(f"❌ Doğrulama kodu ile üye kaydı hatası: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def login_to_hepsiburada(self):
        """Hepsiburada'ya giriş yapar"""
        print("🔑 Hepsiburada'ya giriş yapılıyor...")
        
        try:
            # Giriş sayfasına git
            self.hepsiburada_page.navigate_to_login()
            
            # Email gir
            if not self.login_page.enter_email(self.temp_email):
                print("❌ Email girilemedi")
                return False
            
            # Şifre gir
            if not self.login_page.enter_password(self.password):
                print("❌ Şifre girilemedi")
                return False
            
            # Giriş yap
            if not self.login_page.click_login_button():
                print("❌ Giriş butonuna tıklanamadı")
                return False
            
            # Google şifre kaydetme popup'ını kapat
            self.hepsiburada_page.close_google_password_popup()
            
            print("📧 Giriş doğrulama kodu bekleniyor...")
            return True
            
        except Exception as e:
            print(f"❌ Giriş hatası: {e}")
            return False
    
    def complete_login_with_code(self, verification_code):
        """Doğrulama kodu ile girişi tamamlar"""
        print(f"🔐 Giriş doğrulama kodu giriliyor: {verification_code}")
        
        try:
            # Doğrulama kodu gir
            if not self.login_page.enter_verification_code(verification_code):
                print("❌ Doğrulama kodu girilemedi")
                return False
            
            # Doğrula
            if not self.login_page.click_verify_button():
                print("❌ Doğrulama butonuna tıklanamadı")
                return False
            
            # Giriş başarı kontrolü
            return self.hepsiburada_page.check_login_success()
                
        except Exception as e:
            print(f"❌ Giriş doğrulama hatası: {e}")
            return False
    
    def run_full_automation(self):
        """Tam otomasyon sürecini çalıştırır"""
        print("🚀 Hepsiburada Tam Otomasyon Başlatılıyor...")
        print("=" * 60)
        
        try:
            # 1. Tempail'den geçici email al (yeni sekmede)
            self.temp_email = self.get_temp_email()
            if not self.temp_email:
                print("❌ Geçici email alınamadı, test durduruluyor")
                return False
            
            print(f"📧 Tempail sekmesi açık tutuldu: {self.temp_email}")
            print("⚠️ Tempail sekmesini kapatmayın - doğrulama kodu gelecek!")
            
            # 2. Hepsiburada'da üye ol
            print("📝 Hepsiburada'da üye kaydı formu dolduruluyor...")
            if not self.register_on_hepsiburada():
                print("❌ Üye kaydı başlatılamadı")
                return False
            
            # 3. Tempail'den doğrulama kodunu bekle
            print("📧 Tempail'den doğrulama kodu bekleniyor...")
            print("⚠️ Tempail sekmesinde yeni email gelene kadar bekleyin...")
            print("💡 Email geldiğinde otomatik olarak açılacak ve kod alınacak...")
            
            registration_code = self.wait_for_email_with_code(120)
            if not registration_code:
                print("❌ Doğrulama kodu alınamadı")
                return False
            
            print(f"✅ Doğrulama kodu alındı: {registration_code}")
            print("🔄 Şimdi Hepsiburada sekmesine geri dönülüyor...")
            
            # 4. Hepsiburada'ya geri dön ve kodu gir
            if not self.complete_registration_with_code(registration_code):
                print("❌ Üye kaydı tamamlanamadı")
                return False
            
            print("🎉 TAM OTOMASYON BAŞARILI!")
            print("✅ Hesap oluşturuldu ve giriş yapıldı!")
            return True
            
        except Exception as e:
            print(f"❌ Otomasyon hatası: {e}")
            import traceback
            traceback.print_exc()
            return False
        
        finally:
            print("=" * 60)
            print("🏁 Otomasyon tamamlandı")
            print("💡 Tempail sekmesi hala açık - doğrulama kodunu kontrol edebilirsiniz")
    
    def run_login_test(self):
        """Sadece giriş testini çalıştırır"""
        print("🔑 Hepsiburada Giriş Testi Başlatılıyor...")
        print("=" * 60)
        
        try:
            # 1. Tempail'den geçici email al (yeni sekmede)
            self.temp_email = self.get_temp_email()
            if not self.temp_email:
                print("❌ Geçici email alınamadı, test durduruluyor")
                return False
            
            print(f"📧 Tempail sekmesi açık tutuldu: {self.temp_email}")
            print("⚠️ Tempail sekmesini kapatmayın - doğrulama kodu gelecek!")
            
            # 2. Hepsiburada'ya giriş yap
            if not self.login_to_hepsiburada():
                print("❌ Giriş başlatılamadı")
                return False
            
            # 3. Doğrulama kodunu bekle
            verification_code = self.wait_for_email_with_code(120)
            if not verification_code:
                print("❌ Giriş doğrulama kodu alınamadı")
                return False
            
            # 4. Girişi tamamla
            if not self.complete_login_with_code(verification_code):
                print("❌ Giriş tamamlanamadı")
                return False
            
            print("🎉 GİRİŞ TESTİ BAŞARILI!")
            return True
            
        except Exception as e:
            print(f"❌ Giriş testi hatası: {e}")
            import traceback
            traceback.print_exc()
            return False
