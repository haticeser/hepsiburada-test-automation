# pages/registration_page.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class RegistrationPage(BasePage):
    """Hepsiburada üye kaydı sayfası için Page Object Model"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_email(self, email):
        """Email adresini girer"""
        print(f"📧 Email giriliyor: {email}")
        
        email_selectors = [
            "#txtUserName",
            "input[name='email']",
            "input[type='email']",
            "input[placeholder*='email']"
        ]
        
        email_input = None
        for selector in email_selectors:
            try:
                email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                break
            except:
                continue
        
        if email_input:
            email_input.clear()
            email_input.send_keys(email)
            print(f"✅ Email girildi: {email}")
            return True
        else:
            print("❌ Email input bulunamadı")
            return False
    
    def click_continue_button(self):
        """Devam et butonuna tıklar"""
        print("⏭️ 'Devam et' butonuna tıklanıyor...")
        
        try:
            # Önce en yaygın selector'ı dene (hızlı)
            continue_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#btnSignUpSubmit"))
            )
            continue_button.click()
            print("✅ 'Devam et' butonuna tıklandı (#btnSignUpSubmit)")
            time.sleep(3)
            return True
        except:
            pass
        
        try:
            # Alternatif selector'ları hızlıca dene
            continue_selectors = [
                "button[type='submit']",
                ".submit-btn",
                "input[type='submit']"
            ]
            
            for selector in continue_selectors:
                try:
                    continue_button = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    continue_button.click()
                    print(f"✅ 'Devam et' butonuna tıklandı ({selector})")
                    time.sleep(3)
                    return True
                except:
                    continue
        except:
            pass
        
        print("❌ Devam et butonu bulunamadı")
        return False
    
    def enter_password(self, password):
        """Şifre alanını doldurur"""
        print("🔒 Şifre giriliyor...")
        
        try:
            # En yaygın selector'ı dene (hızlı)
            password_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#txtPassword"))
            )
            password_input.clear()
            password_input.send_keys(password)
            print("✅ Şifre girildi (#txtPassword)")
            return True
        except:
            pass
        
        try:
            # Alternatif selector'ları hızlıca dene
            password_selectors = [
                "input[name='password']",
                "input[type='password']",
                "input[placeholder*='şifre']",
                "input[placeholder*='password']"
            ]
            
            for selector in password_selectors:
                try:
                    password_input = WebDriverWait(self.driver, 2).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    password_input.clear()
                    password_input.send_keys(password)
                    print(f"✅ Şifre girildi ({selector})")
                    return True
                except:
                    continue
        except:
            pass
        
        print("⚠ Şifre alanı bulunamadı")
        return False
    
    def submit_registration_form(self):
        """Üye kaydı formunu gönderir"""
        print("📝 Üye kaydı formu gönderiliyor...")
        
        try:
            # En yaygın selector'ı dene (hızlı)
            submit_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#btnSignUpSubmit"))
            )
            submit_button.click()
            print("✅ Üye kaydı formu gönderildi (#btnSignUpSubmit)")
            time.sleep(3)
            return True
        except:
            pass
        
        try:
            # Alternatif selector'ları hızlıca dene
            submit_selectors = [
                "button[type='submit']",
                "input[type='submit']",
                ".submit-btn"
            ]
            
            for selector in submit_selectors:
                try:
                    submit_button = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    submit_button.click()
                    print(f"✅ Üye kaydı formu gönderildi ({selector})")
                    time.sleep(3)
                    return True
                except:
                    continue
        except:
            pass
        
        print("❌ Submit butonu bulunamadı")
        return False
    
    def enter_verification_code(self, verification_code):
        """Doğrulama kodunu girer"""
        print(f"🔐 Doğrulama kodu giriliyor: {verification_code}")
        
        try:
            # En yaygın selector'ı dene (hızlı)
            print("🔍 #txtCode selector'ı deneniyor...")
            code_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#txtCode"))
            )
            code_input.clear()
            code_input.send_keys(verification_code)
            print("✅ Doğrulama kodu girildi: #txtCode")
            return True
        except:
            pass
        
        try:
            # Alternatif selector'ları hızlıca dene
            code_selectors = [
                "input[name='code']",
                "input[placeholder*='Kodu Gir']",
                "input[placeholder*='Enter Code']",
                "input[maxlength='6']"
            ]
            
            for selector in code_selectors:
                try:
                    print(f"🔍 {selector} selector'ı deneniyor...")
                    code_input = WebDriverWait(self.driver, 2).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    code_input.clear()
                    code_input.send_keys(verification_code)
                    print(f"✅ Doğrulama kodu girildi: {selector}")
                    return True
                except:
                    continue
        except:
            pass
        
        print("⚠ Doğrulama kodu alanı bulunamadı")
        return False
    
    def click_verify_email_button(self):
        """E-posta adresini doğrula butonuna tıklar"""
        print("🔐 E-posta doğrulama butonuna tıklanıyor...")
        
        try:
            # En yaygın selector'ı dene (hızlı)
            print("🔍 button[type='submit'] selector'ı deneniyor...")
            verify_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            verify_button.click()
            print("✅ E-posta doğrulama butonuna tıklandı (button[type='submit'])")
            time.sleep(3)
            return True
        except:
            pass
        
        try:
            # Alternatif selector'ları hızlıca dene
            verify_selectors = [
                "input[type='submit']",
                ".verify-button",
                ".submit-button"
            ]
            
            for selector in verify_selectors:
                try:
                    print(f"🔍 {selector} selector'ı deneniyor...")
                    verify_button = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    verify_button.click()
                    print(f"✅ E-posta doğrulama butonuna tıklandı ({selector})")
                    time.sleep(3)
                    return True
                except:
                    continue
        except:
            pass
        
        print("⚠ E-posta doğrulama butonu bulunamadı")
        return False
    
    def click_verify_button(self):
        """Doğrula/Onayla butonuna tıklar"""
        print("✅ Doğrulama butonuna tıklanıyor...")
        
        try:
            # En yaygın selector'ı dene (hızlı)
            verify_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#btnVerify"))
            )
            verify_button.click()
            print("✅ Doğrulama butonuna tıklandı (#btnVerify)")
            time.sleep(3)
            return True
        except:
            pass
        
        try:
            # Alternatif selector'ları hızlıca dene
            verify_selectors = [
                "#btnConfirm",
                "button[type='submit']",
                ".verify-btn"
            ]
            
            for selector in verify_selectors:
                try:
                    verify_button = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    verify_button.click()
                    print(f"✅ Doğrulama butonuna tıklandı ({selector})")
                    time.sleep(3)
                    return True
                except:
                    continue
        except:
            pass
        
        print("❌ Doğrulama butonu bulunamadı")
        return False
    
    def fill_personal_info(self, first_name, last_name, password):
        """Kişisel bilgileri doldurur: Ad, Soyad, Şifre"""
        print("📝 Kişisel bilgiler dolduruluyor...")
        
        # Ad (First Name) alanını doldur
        try:
            print("🔍 #txtName selector'ı deneniyor...")
            first_name_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#txtName"))
            )
            first_name_input.clear()
            first_name_input.send_keys(first_name)
            print(f"✅ Ad alanı dolduruldu: {first_name}")
        except:
            print("❌ Ad alanı bulunamadı")
            return False
        
        # Soyad (Last Name) alanını doldur
        try:
            print("🔍 #txtSurname selector'ı deneniyor...")
            last_name_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#txtSurname"))
            )
            last_name_input.clear()
            last_name_input.send_keys(last_name)
            print(f"✅ Soyad alanı dolduruldu: {last_name}")
        except:
            print("❌ Soyad alanı bulunamadı")
            return False
        
        # Şifre alanını doldur
        try:
            print("🔍 #txtNewPassEmail selector'ı deneniyor...")
            password_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#txtNewPassEmail"))
            )
            password_input.clear()
            password_input.send_keys(password)
            print(f"✅ Şifre alanı dolduruldu: {password}")
        except:
            print("❌ Şifre alanı bulunamadı")
            return False
        
        print("✅ Tüm kişisel bilgiler başarıyla dolduruldu")
        return True
    
    def check_email_subscription(self):
        """Elektronik ileti checkbox'ını işaretler"""
        print("📧 Elektronik ileti checkbox'ı işaretleniyor...")
        
        try:
            checkbox_selectors = [
                "#checkSubscribeEmail",
                "input[name='subscribeEmail']",
                "input[name='emailSubscription']",
                "input[name='newsletter']",
                "input[type='checkbox']",
                "input[value='true']",
                "input[value='1']",
                "input[data-testid*='subscribe']",
                "input[data-testid*='newsletter']"
            ]
            
            checkbox = None
            for selector in checkbox_selectors:
                try:
                    print(f"🔍 {selector} selector'ı deneniyor...")
                    checkbox = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                    break
                except Exception as e:
                    print(f"⚠ {selector} selector'ı başarısız: {e}")
                    continue
            
            if checkbox:
                if not checkbox.is_selected():
                    checkbox.click()
                    print("✅ Elektronik ileti checkbox'ı işaretlendi")
                else:
                    print("✅ Elektronik ileti checkbox'ı zaten işaretli")
                return True
            else:
                print("⚠ Elektronik ileti checkbox'ı bulunamadı")
                return False
                
        except Exception as e:
            print(f"⚠ Checkbox işaretleme hatası: {e}")
            return False
    
    def click_final_signup_button(self):
        """Üye ol butonuna tıklar"""
        print("🔐 Üye ol butonuna tıklanıyor...")
        
        try:
            # En yaygın selector'ı dene (hızlı)
            print("🔍 #btnSignUpSub selector'ı deneniyor...")
            signup_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#btnSignUpSub"))
            )
            signup_button.click()
            print("✅ Üye ol butonuna tıklandı (#btnSignUpSub)")
            time.sleep(3)
            return True
        except:
            pass
        
        try:
            # Alternatif selector'ları hızlıca dene
            signup_button_selectors = [
                "button[id*='btnSignUp']",
                "button[type='submit']",
                ".submit-btn"
            ]
            
            for selector in signup_button_selectors:
                try:
                    print(f"🔍 {selector} selector'ı deneniyor...")
                    signup_button = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    signup_button.click()
                    print(f"✅ Üye ol butonuna tıklandı ({selector})")
                    time.sleep(3)
                    return True
                except:
                    continue
        except:
            pass
        
        try:
            # Text içeren buton ara (son çare)
            print("🔍 Text içeren buton aranıyor...")
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            for btn in buttons:
                if any(keyword in btn.text.lower() for keyword in ['üye ol', 'sign up', 'kayıt ol']):
                    btn.click()
                    print("✅ Üye ol butonuna tıklandı (text ile bulundu)")
                    time.sleep(3)
                    return True
        except:
            pass
        
        print("❌ Üye ol butonu bulunamadı")
        return False
    
    def check_extra_verification_needed(self):
        """Ek doğrulama kodu alanı var mı kontrol eder"""
        print("🔍 Ek doğrulama kodu alanı kontrol ediliyor...")
        
        try:
            extra_code_selectors = [
                "#txtVerificationCode",
                "#txtCode", 
                "input[name='verificationCode']",
                "input[name='code']",
                "input[placeholder*='kod']",
                "input[maxlength='6']"
            ]
            
            for selector in extra_code_selectors:
                try:
                    extra_code_input = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    if extra_code_input:
                        print("⚠ Ek doğrulama kodu alanı bulundu!")
                        return extra_code_input
                except:
                    continue
            
            print("✅ Ek doğrulama kodu alanı bulunamadı")
            return None
            
        except Exception as e:
            print(f"⚠ Ek doğrulama kontrol hatası: {e}")
            return None
    
    def enter_extra_verification_code(self, verification_code):
        """Ek doğrulama kodunu girer"""
        print(f"🔐 Ek doğrulama kodu giriliyor: {verification_code}")
        
        try:
            extra_code_selectors = [
                "#txtVerificationCode",
                "#txtCode", 
                "input[name='verificationCode']",
                "input[name='code']",
                "input[placeholder*='kod']",
                "input[maxlength='6']"
            ]
            
            for selector in extra_code_selectors:
                try:
                    print(f"🔍 {selector} selector'ı deneniyor...")
                    extra_code_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                    extra_code_input.clear()
                    extra_code_input.send_keys(verification_code)
                    print(f"✅ Ek doğrulama kodu girildi: {selector}")
                    return True
                except Exception as e:
                    print(f"⚠ {selector} selector'ı başarısız: {e}")
                    continue
            
            print("⚠ Ek doğrulama kodu alanı bulunamadı")
            return False
            
        except Exception as e:
            print(f"❌ Ek doğrulama kodu girme hatası: {e}")
            return False
    
    def click_extra_verify_button(self):
        """Ek doğrulama butonuna tıklar"""
        print("🔐 Ek doğrulama butonuna tıklanıyor...")
        
        try:
            extra_verify_selectors = [
                "#btnVerify",
                "#btnConfirm",
                "button[type='submit']",
                ".verify-btn",
                ".confirm-btn",
                "input[type='submit']"
            ]
            
            for selector in extra_verify_selectors:
                try:
                    print(f"🔍 {selector} selector'ı deneniyor...")
                    extra_verify_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                    extra_verify_button.click()
                    print(f"✅ Ek doğrulama butonuna tıklandı: {selector}")
                    time.sleep(5)
                    return True
                except Exception as e:
                    print(f"⚠ {selector} selector'ı başarısız: {e}")
                    continue
            
            print("⚠ Ek doğrulama butonu bulunamadı")
            return False
            
        except Exception as e:
            print(f"❌ Ek doğrulama butonuna tıklama hatası: {e}")
            return False