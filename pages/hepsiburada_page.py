# pages/hepsiburada_page.py
from .modules.navigation_module import NavigationModule
from .modules.product_module import ProductModule
from .modules.filter_module import FilterModule
from .modules.cart_module import CartModule
from .modules.auth_module import AuthModule


class HepsiburadaPage:
    """Hepsiburada ana sayfa işlemleri - Modüler versiyon"""
    
    def __init__(self, driver):
        self.driver = driver
        
        # Modülleri başlat
        self.navigation = NavigationModule(driver)
        self.product = ProductModule(driver)
        self.filter = FilterModule(driver)
        self.cart = CartModule(driver)
        self.auth = AuthModule(driver)
    
    # Navigation işlemleri
    def go_to_hepsiburada(self):
        """Hepsiburada ana sayfasına gider"""
        return self.navigation.go_to_hepsiburada()
    
    def navigate_to_registration(self):
        """Kayıt sayfasına yönlendirir"""
        return self.navigation.navigate_to_registration()
    
    def navigate_to_login(self):
        """Giriş sayfasına yönlendirir"""
        return self.navigation.navigate_to_login()
    
    def navigate_to_login_with_xpath(self):
        """Belirli XPath'lerle giriş sayfasına yönlendirir"""
        return self.navigation.navigate_to_login_with_specific_xpath()
    
    # Product işlemleri
    def select_laptop_product(self):
        """Dizüstü bilgisayar kategorisini seçer"""
        return self.product.select_laptop_product()
    
    def find_elektronik_menu(self):
        """Elektronik menüsünü bulur"""
        return self.product.find_elektronik_menu()
    
    def find_bilgisayar_submenu(self):
        """Bilgisayar alt menüsünü bulur"""
        return self.product.find_bilgisayar_submenu()
    
    def find_dizustu_bilgisayar_link(self):
        """Dizüstü bilgisayar linkini bulur"""
        return self.product.find_dizustu_bilgisayar_link()
    
    def wait_for_submenu_to_appear(self):
        """Alt menünün görünmesini bekler"""
        return self.product.wait_for_submenu_to_appear()
    
    def wait_for_laptop_submenu_to_appear(self):
        """Dizüstü bilgisayar alt menüsünün görünmesini bekler"""
        return self.product.wait_for_laptop_submenu_to_appear()
    
    def click_first_filtered_product(self):
        """İlk filtrelenmiş ürünü tıklar"""
        return self.product.click_first_filtered_product()
    
    def get_filtered_product_count(self):
        """Filtrelenmiş ürün sayısını alır"""
        return self.product.get_filtered_product_count()
    
    # Filter işlemleri
    def apply_specific_filters(self, brand="Lenovo", processor="Intel Core i7"):
        """Belirli filtreleri uygular"""
        return self.filter.apply_specific_filters(brand, processor)
    
    def apply_brand_filter(self, brand):
        """Marka filtresini uygular"""
        return self.filter.apply_brand_filter(brand)
    
    def apply_processor_filter(self, processor):
        """İşlemci filtresini uygular"""
        return self.filter.apply_processor_filter(processor)
    
    def apply_category_filters(self, brand=None, min_price=None, max_price=None):
        """Kategori filtrelerini uygular"""
        return self.filter.apply_category_filters(brand, min_price, max_price)
    
    def apply_price_filter(self, min_price, max_price):
        """Fiyat filtresini uygular"""
        return self.filter.apply_price_filter(min_price, max_price)
    
    def clear_all_filters(self):
        """Tüm filtreleri temizler"""
        return self.filter.clear_all_filters()
    
    def get_active_filters(self):
        """Aktif filtreleri alır"""
        return self.filter.get_active_filters()
    
    # Cart işlemleri
    def add_product_to_cart(self):
        """Ürünü sepete ekler"""
        return self.cart.add_product_to_cart()
    
    def go_to_cart(self):
        """Sepet sayfasına gider"""
        return self.cart.go_to_cart()
    
    def handle_cart_page_operations(self):
        """Sepet sayfası işlemlerini yönetir"""
        return self.cart.handle_cart_page_operations()
    
    def get_cart_item_count(self):
        """Sepetteki ürün sayısını alır"""
        return self.cart.get_cart_item_count()
    
    def remove_item_from_cart(self, item_index=0):
        """Sepetten ürün çıkarır"""
        return self.cart.remove_item_from_cart(item_index)
    
    def update_item_quantity(self, item_index=0, new_quantity=1):
        """Ürün miktarını günceller"""
        return self.cart.update_item_quantity(item_index, new_quantity)
    
    def proceed_to_checkout(self):
        """Ödeme sayfasına geçer"""
        return self.cart.proceed_to_checkout()
    
    def get_cart_total(self):
        """Sepet toplamını alır"""
        return self.cart.get_cart_total()
    
    def is_cart_empty(self):
        """Sepet boş mu kontrol eder"""
        return self.cart.is_cart_empty()
    
    # Auth işlemleri
    def check_registration_success(self):
        """Kayıt başarılı mı kontrol eder"""
        return self.auth.check_registration_success()
    
    def check_login_success(self):
        """Giriş başarılı mı kontrol eder"""
        return self.auth.check_login_success()
    
    def check_user_logged_in(self):
        """Kullanıcı giriş yapmış mı kontrol eder"""
        return self.auth.check_user_logged_in()
    
    def logout_user(self):
        """Kullanıcıyı çıkış yapar"""
        return self.auth.logout_user()
    
    def get_user_info(self):
        """Kullanıcı bilgilerini alır"""
        return self.auth.get_user_info()
    
    def check_verification_required(self):
        """Doğrulama gerekli mi kontrol eder"""
        return self.auth.check_verification_required()
    
    def wait_for_verification_success(self, timeout=30):
        """Doğrulama başarısını bekler"""
        return self.auth.wait_for_verification_success(timeout)
    
    # BasePage metodlarını erişilebilir yap
    def close_cookie_popup(self):
        """Çerez popup'ını kapatmaya çalışır"""
        return self.navigation.close_cookie_popup()
    
    def close_google_password_popup(self):
        """Google şifre kaydetme popup'ını kapatır"""
        return self.navigation.close_google_password_popup()
    
    def proceed_to_checkout(self):
        """Ödeme sayfasına geçer"""
        return self.cart.proceed_to_checkout()
    
    def handle_add_to_cart_popup(self):
        """Sepete ekleme popup'ını işler"""
        return self.cart.handle_add_to_cart_popup()
    
    def click_sepetim_button(self):
        """Sepetim butonuna tıklar"""
        return self.cart.click_sepetim_button()
    
    def increase_product_quantity(self):
        """Sepetteki ürün sayısını + butonu ile 1 arttırır"""
        return self.cart.increase_product_quantity()
    
    def click_complete_shopping_button(self):
        """Alışverişi tamamla butonuna tıklar"""
        return self.cart.click_complete_shopping_button()
    
    def click_add_new_address_button(self):
        """Yeni adres ekle butonuna tıklar"""
        return self.cart.click_add_new_address_button()
    
    def fill_address_form(self):
        """Adres formunu doldurur"""
        return self.cart.fill_address_form()
    
    def click_enter_card_details_button(self):
        """Kart bilgilerini gir butonuna tıklar"""
        return self.cart.click_enter_card_details_button()
    
    def fill_card_form(self):
        """Kart formunu doldurur"""
        return self.cart.fill_card_form()
    
    def confirm_order(self):
        """Siparişi onaylar"""
        return self.cart.confirm_order()