# test_webdriver.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_webdriver_connection():
    """WebDriver bağlantısını test eder"""
    print("🔍 WebDriver bağlantı testi başlatılıyor...")
    
    try:
        # Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        print("🚀 Chrome WebDriver başlatılıyor...")
        driver = webdriver.Chrome(options=chrome_options)
        
        print("✅ WebDriver başarıyla başlatıldı")
        print(f"📱 Tarayıcı: {driver.name}")
        print(f"🌐 Versiyon: {driver.capabilities['browserVersion']}")
        
        # Basit sayfa testi
        print("🌐 Hepsiburada sayfasına gidiliyor...")
        driver.get("https://www.hepsiburada.com")
        time.sleep(5)
        
        print(f"📄 Sayfa başlığı: {driver.title}")
        print(f"🔗 URL: {driver.current_url}")
        
        # Başarılı
        print("✅ WebDriver testi başarılı!")
        driver.quit()
        return True
        
    except Exception as e:
        print(f"❌ WebDriver hatası: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_webdriver_connection()
    if success:
        print("\n🎉 WebDriver çalışıyor, ana test çalıştırılabilir!")
    else:
        print("\n💥 WebDriver sorunu var, önce bu çözülmeli!")
