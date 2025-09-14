# pages/driver_manager.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time


class DriverManager:
    """WebDriver'ı singleton pattern ile yönetir - tek seferde kurup yeniden kullanır"""
    
    _instance = None
    _lock = threading.Lock()
    _driver = None
    _is_initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DriverManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._is_initialized:
            self._is_initialized = True
    
    def get_driver(self, force_restart=False):
        """WebDriver'ı döndürür - eğer yoksa oluşturur"""
        with self._lock:
            if self._driver is None or force_restart:
                if self._driver is not None:
                    try:
                        self._driver.quit()
                    except:
                        pass
                
                print("🚀 WebDriver kuruluyor... (tek seferlik)")
                self._driver = self._create_driver()
                print("✅ WebDriver hazır!")
            
            return self._driver
    
    def _create_driver(self):
        """Chrome WebDriver'ı oluşturur"""
        chrome_options = Options()
        
        # Anti-detection ayarları
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Performans ve görünüm ayarları - Yavaş mod için
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-notifications")
        
        # Yavaş mod ayarları - Hover işlemlerini görmek için
        chrome_options.add_argument("--disable-background-timer-throttling")
        chrome_options.add_argument("--disable-backgrounding-occluded-windows")
        chrome_options.add_argument("--disable-renderer-backgrounding")
        chrome_options.add_argument("--disable-features=TranslateUI")
        chrome_options.add_argument("--disable-ipc-flooding-protection")
        
        # GPU ve WebGL optimizasyonları
        chrome_options.add_argument("--enable-unsafe-swiftshader")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--disable-gpu-sandbox")
        chrome_options.add_argument("--disable-gpu-process-crash-limit")
        chrome_options.add_argument("--disable-background-timer-throttling")
        chrome_options.add_argument("--disable-backgrounding-occluded-windows")
        chrome_options.add_argument("--disable-renderer-backgrounding")
        
        # Log seviyesini azalt
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--silent")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        
        # Memory ve performans
        chrome_options.add_argument("--memory-pressure-off")
        chrome_options.add_argument("--max_old_space_size=4096")
        
        try:
            # Manuel ChromeDriver 140 yolu kullan
            service = Service("C:/Users/eserh/hepsiburada_test_automation/drivers/chromedriver.exe")
            driver = webdriver.Chrome(service=service, options=chrome_options)
            print("✅ Chrome WebDriver 140 başarıyla kuruldu")
            return driver
        except Exception as e:
            print(f"❌ ChromeDriver 140 hatası: {e}")
            print("💡 ChromeDriver 140'ın doğru yerde olduğundan emin olun:")
            print("   C:/Users/eserh/hepsiburada_test_automation/drivers/chromedriver.exe")
            # Fallback: WebDriver Manager dene
            try:
                driver_path = ChromeDriverManager().install()
                service = Service(driver_path)
                driver = webdriver.Chrome(service=service, options=chrome_options)
                print("✅ WebDriver Manager ile hazır!")
                return driver
            except Exception as e2:
                print(f"❌ WebDriver Manager hatası: {e2}")
                driver = webdriver.Chrome(options=chrome_options)
                print("✅ WebDriver hazır (son fallback)!")
                return driver
    
    def restart_driver(self):
        """WebDriver'ı yeniden başlatır"""
        print("🔄 WebDriver yeniden başlatılıyor...")
        return self.get_driver(force_restart=True)
    
    def quit_driver(self):
        """WebDriver'ı kapatır"""
        with self._lock:
            if self._driver is not None:
                try:
                    self._driver.quit()
                    print("🔒 WebDriver kapatıldı")
                except:
                    pass
                finally:
                    self._driver = None
    
    def is_driver_alive(self):
        """WebDriver'ın çalışıp çalışmadığını kontrol eder"""
        if self._driver is None:
            return False
        try:
            # Basit bir test yaparak driver'ın çalışıp çalışmadığını kontrol et
            self._driver.current_url
            return True
        except:
            return False
    
    def get_driver_safely(self):
        """Güvenli şekilde WebDriver döndürür - eğer ölüyse yeniden oluşturur"""
        if not self.is_driver_alive():
            print("⚠️ WebDriver ölü, yeniden oluşturuluyor...")
            return self.get_driver(force_restart=True)
        return self.get_driver()


# Global instance
driver_manager = DriverManager()
