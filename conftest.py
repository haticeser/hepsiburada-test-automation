# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="session")
def browser_options():
    """Chrome tarayıcı seçeneklerini yapılandırır"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    return chrome_options


@pytest.fixture(scope="function")
def driver(browser_options):
    """WebDriver instance oluşturur ve her test sonrasında kapatır"""
    driver = webdriver.Chrome(options=browser_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    """WebDriverWait instance döner"""
    return WebDriverWait(driver, 20)


@pytest.fixture(scope="session")
def test_credentials():
    """Test için kullanılacak sabit bilgileri döner"""
    return {
        "password": "123456aA",
        "first_name": "Kıymetli",
        "last_name": "Stajyer"
    }