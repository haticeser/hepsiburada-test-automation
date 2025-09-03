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
        
        continue_selectors = [
            "#btnSignUpSubmit",
            "button[type='submit']",
            ".submit-btn",
            "input[type='submit']"
        ]
        
        for selector in continue_selectors:
            try:
                continue_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                continue_button.click()
                print("✅ 'Devam et' butonuna tıklandı")
                time.sleep(5)
                return True
            except:
                continue
        
        print("❌ Devam et butonu bulunamadı")
        return False
    
    def enter_password(self, password):
        """Şifre alanını doldurur"""
        print("🔒 Şifre giriliyor...")
        
        # Şifre alanı için çeşitli selector'ları dene
        password_selectors = [
            "#txtPassword",
            "input[name='password']",
            "input[type='password']",
            "input[placeholder*='şifre']",
            "input[placeholder*='password']",
            "input[placeholder*='Şifre']",
            "input[placeholder*='Password']",
            "input[id*='password']",
            "input[id*='Password']",
            "input[class*='password']",
            "input[class*='Password']"
        ]
        
        for selector in password_selectors:
            try:
                password_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                password_input.clear()
                password_input.send_keys(password)
                print(f"✅ Şifre girildi: {selector}")
                return True
            except Exception as e:
                print(f"⚠ {selector} selector'ı başarısız: {e}")
                continue
        
        print("⚠ Şifre alanı bulunamadı")
        return False
    
    def submit_registration_form(self):
        """Üye kaydı formunu gönderir"""
        print("📝 Üye kaydı formu gönderiliyor...")
        
        # Submit butonu için çeşitli selector'ları dene
        submit_selectors = [
            "#btnSignUpSubmit",
            "button[type='submit']",
            "input[type='submit']",
            ".submit-btn",
            ".btn-submit",
            "button[class*='submit']",
            "button[class*='Submit']",
            "button[class*='btn']",
            "button:contains('Üye Ol')",
            "button:contains('Kayıt Ol')",
            "button:contains('Submit')",
            "button:contains('Sign Up')",
            "a[class*='submit']",
            "a[class*='btn']"
        ]
        
        for selector in submit_selectors:
            try:
                submit_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                submit_button.click()
                print(f"✅ Üye kaydı formu gönderildi: {selector}")
                time.sleep(5)
                return True
            except Exception as e:
                print(f"⚠ {selector} selector'ı başarısız: {e}")
                continue
        
        print("❌ Submit butonu bulunamadı")
        return False
    
    def enter_verification_code(self, verification_code):
        """Doğrulama kodunu girer"""
        print(f"🔐 Doğrulama kodu giriliyor: {verification_code}")
        
        # Doğrulama kodu alanı için çeşitli selector'ları dene
        code_selectors = [
            "#txtCode",
            "input[name='code']",
            "input[placeholder*='Kodu Gir']",
            "input[placeholder*='Enter Code']",
            "input[placeholder*='kod']",
            "input[placeholder*='code']",
            "input[maxlength='6']",
            "input[data-testid*='code']",
            "input[data-testid*='Code']",
            "input[aria-label*='kod']",
            "input[aria-label*='code']",
            "input[data-cy*='code']",
            "input[data-cy*='Code']"
        ]
        
        for selector in code_selectors:
            try:
                print(f"🔍 {selector} selector'ı deneniyor...")
                code_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                code_input.clear()
                code_input.send_keys(verification_code)
                print(f"✅ Doğrulama kodu girildi: {selector}")
                return True
            except Exception as e:
                print(f"⚠ {selector} selector'ı başarısız: {e}")
                continue
        
        # Tüm input alanlarını listele
        print("🔍 Sayfadaki tüm input alanları listeleniyor...")
        all_inputs = self.driver.find_elements(By.TAG_NAME, "input")
        for i, input_elem in enumerate(all_inputs):
            try:
                input_type = input_elem.get_attribute("type")
                input_id = input_elem.get_attribute("id")
                input_name = input_elem.get_attribute("name")
                input_placeholder = input_elem.get_attribute("placeholder")
                input_class = input_elem.get_attribute("class")
                input_maxlength = input_elem.get_attribute("maxlength")
                print(f"Input {i}: type={input_type}, id={input_id}, name={input_name}, placeholder={input_placeholder}, class={input_class}, maxlength={input_maxlength}")
            except:
                pass
        
        print("⚠ Doğrulama kodu alanı bulunamadı")
        return False
    
    def click_verify_email_button(self):
        """E-posta adresini doğrula butonuna tıklar"""
        print("🔐 E-posta doğrulama butonuna tıklanıyor...")
        
        verify_selectors = [
            "button[type='submit']",
            "input[type='submit']",
            "button:contains('E-posta adresini doğrula')",
            "button:contains('Verify email address')",
            "button:contains('Doğrula')",
            "button:contains('Verify')",
            ".verify-button",
            ".submit-button",
            "[data-testid*='verify']",
            "[data-testid*='submit']"
        ]
        
        for selector in verify_selectors:
            try:
                print(f"🔍 {selector} selector'ı deneniyor...")
                verify_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                verify_button.click()
                print(f"✅ E-posta doğrulama butonuna tıklandı: {selector}")
                time.sleep(5)
                return True
            except Exception as e:
                print(f"⚠ {selector} selector'ı başarısız: {e}")
                continue
        
        print("⚠ E-posta doğrulama butonu bulunamadı")
        return False
    
    def click_verify_button(self):
        """Doğrula/Onayla butonuna tıklar"""
        print("✅ Doğrulama butonuna tıklanıyor...")
        
        verify_selectors = [
            "#btnVerify",
            "#btnConfirm",
            "button[type='submit']",
            ".verify-btn",
            ".confirm-btn",
            "input[type='submit']"
        ]
        
        for selector in verify_selectors:
            try:
                verify_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                verify_button.click()
                print("✅ Doğrulama butonuna tıklandı")
                time.sleep(5)
                return True
            except:
                continue
        
        print("❌ Doğrulama butonu bulunamadı")
        return False
    
    def fill_personal_info(self, first_name, last_name, password):
        """Kişisel bilgileri doldurur: Ad, Soyad, Şifre"""
        print("📝 Kişisel bilgiler dolduruluyor...")
        
        # Ad (First Name) alanını doldur
        try:
            first_name_selectors = [
                "#txtName",
                "input[name='firstName']",
                "input[name='first_name']",
                "input[name='name']",
                "input[placeholder*='Ad']",
                "input[placeholder*='First Name']",
                "input[placeholder*='İsim']",
                "input[id*='name']",
                "input[id*='Name']"
            ]
            
            first_name_input = None
            for selector in first_name_selectors:
                try:
                    print(f"🔍 {selector} selector'ı deneniyor...")
                    first_name_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                    first_name_input.clear()
                    first_name_input.send_keys(first_name)
                    print(f"✅ Ad alanı dolduruldu: {first_name}")
                    break
                except Exception as e:
                    print(f"⚠ {selector} selector'ı başarısız: {e}")
                    continue
            
            if not first_name_input:
                print("❌ Ad alanı bulunamadı")
                return False
                
        except Exception as e:
            print(f"❌ Ad alanı hatası: {e}")
            return False
        
        # Soyad (Last Name) alanını doldur
        try:
            last_name_selectors = [
                "#txtSurname",
                "input[name='lastName']",
                "input[name='last_name']",
                "input[name='surname']",
                "input[placeholder*='Soyad']",
                "input[placeholder*='Last Name']",
                "input[placeholder*='Surname']",
                "input[id*='surname']",
                "input[id*='Surname']",
                "input[id*='lastName']"
            ]
            
            last_name_input = None
            for selector in last_name_selectors:
                try:
                    print(f"🔍 {selector} selector'ı deneniyor...")
                    last_name_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                    last_name_input.clear()
                    last_name_input.send_keys(last_name)
                    print(f"✅ Soyad alanı dolduruldu: {last_name}")
                    break
                except Exception as e:
                    print(f"⚠ {selector} selector'ı başarısız: {e}")
                    continue
            
            if not last_name_input:
                print("❌ Soyad alanı bulunamadı")
                return False
                
        except Exception as e:
            print(f"❌ Soyad alanı hatası: {e}")
            return False
        
        # Şifre alanını doldur
        try:
            password_selectors = [
                "#txtNewPassEmail",
                "input[name='password']",
                "input[name='newPassword']",
                "input[type='password']",
                "input[placeholder*='Şifre']",
                "input[placeholder*='Password']",
                "input[placeholder*='Yeni Şifre']",
                "input[placeholder*='New Password']",
                "input[id*='password']",
                "input[id*='Password']"
            ]
            
            password_input = None
            for selector in password_selectors:
                try:
                    print(f"🔍 {selector} selector'ı deneniyor...")
                    password_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                    password_input.clear()
                    password_input.send_keys(password)
                    print(f"✅ Şifre alanı dolduruldu: {password}")
                    break
                except Exception as e:
                    print(f"⚠ {selector} selector'ı başarısız: {e}")
                    continue
            
            if not password_input:
                print("❌ Şifre alanı bulunamadı")
                return False
                
        except Exception as e:
            print(f"❌ Şifre alanı hatası: {e}")
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
            signup_button_selectors = [
                "#btnSignUpSub",
                "button[id*='btnSignUp']",
                "button[type='submit']",
                "button:contains('Üye ol')",
                "button:contains('Sign Up')",
                "button:contains('Kayıt ol')",
                ".submit-btn",
                ".signup-btn",
                "[data-testid*='signup']",
                "[data-testid*='submit']"
            ]
            
            signup_button = None
            for selector in signup_button_selectors:
                try:
                    print(f"🔍 {selector} selector'ı deneniyor...")
                    if "contains" in selector:
                        # Text içeren buton ara
                        buttons = self.driver.find_elements(By.TAG_NAME, "button")
                        for btn in buttons:
                            if any(keyword in btn.text.lower() for keyword in ['üye ol', 'sign up', 'kayıt ol']):
                                signup_button = btn
                                break
                        if signup_button:
                            break
                    else:
                        signup_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                        if signup_button:
                            break
                except Exception as e:
                    print(f"⚠ {selector} selector'ı başarısız: {e}")
                    continue
            
            if signup_button:
                signup_button.click()
                print("✅ Üye ol butonuna tıklandı")
                time.sleep(3)
                return True
            else:
                print("❌ Üye ol butonu bulunamadı")
                return False
                
        except Exception as e:
            print(f"❌ Üye ol butonuna tıklama hatası: {e}")
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