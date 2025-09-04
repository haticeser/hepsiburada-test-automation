# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """Chrome WebDriver oluşturur"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")
    
    try:
        # WebDriver Manager ile otomatik indirme
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        print(f"WebDriver Manager hatası: {e}")
        # Fallback: Sistem PATH'inde chromedriver aranır
        driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    """WebDriverWait instance döner"""
    return WebDriverWait(driver, 30)


@pytest.fixture(scope="session")
def test_credentials():
    """Test için kullanılacak sabit bilgileri döner"""
    return {
        "password": "123456aA",
        "first_name": "Kıymetli",
        "last_name": "Stajyer"
    }