# pages/hepsiburada_automation.py
from .workflow_manager import WorkflowManager


class HepsiburadaAutomation:
    """Hepsiburada tam otomasyon sınıfı - Sadeleştirilmiş versiyon"""
    
    def __init__(self, driver):
        self.driver = driver
        self.workflow_manager = WorkflowManager(driver)
        
        # Workflow manager'dan bilgileri al
        self.password = self.workflow_manager.password
        self.first_name = self.workflow_manager.first_name
        self.last_name = self.workflow_manager.last_name
    
    
    def run_full_automation(self):
        """Tam otomasyon sürecini çalıştırır"""
        return self.workflow_manager.run_full_automation()
    
    def run_login_test(self):
        """Sadece giriş testini çalıştırır"""
        return self.workflow_manager.run_login_test()
    
    def select_laptop_after_registration(self):
        """Üye kaydı sonrası dizüstü bilgisayar seçimi yapar"""
        return self.workflow_manager._run_product_automation()
    
    def run_product_selection_test(self):
        """Ürün seçimi testini çalıştırır"""
        return self.workflow_manager.run_product_selection_test()
    
    def select_and_click_first_product(self):
        """Filtrelenmiş ürünlerden ilkini seçer ve ürün sayfasına gider"""
        return self.workflow_manager.select_and_click_first_product()
    
    def run_add_to_cart_test(self):
        """Sepete ekleme testini çalıştırır"""
        return self.workflow_manager.run_add_to_cart_test()
    
    def run_cart_operations_test(self):
        """Sadece sepet sayfasındaki işlemleri test eder"""
        return self.workflow_manager.run_cart_operations_test()
    
    def run_direct_login_test(self, email="viva.vista000@gmail.com", password="123456aA"):
        """Sabit email ve şifre ile direkt giriş testini çalıştırır"""
        return self.workflow_manager.run_direct_login_test(email, password)
    
    def run_step_by_step_test(self):
        """Adım adım test - sadece navigasyon"""
        return self.workflow_manager.run_step_by_step_test()
    
    def run_full_login_test(self):
        """Tam giriş testi - tüm adımlar"""
        return self.workflow_manager.run_full_login_test()