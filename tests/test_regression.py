#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regression Testler - Tam İşlevsellik
Kapsamlı işlevsellik testleri - Tam otomasyon sürecinin tüm adımları
"""

import pytest
import allure
from pages.hepsiburada_automation import HepsiburadaAutomation


@pytest.mark.regression
class TestRegression:
    """Regression test sınıfı - tam işlevsellik testleri"""
    
    @allure.feature("Tam Otomasyon")
    @allure.story("End-to-End Test")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.slow
    def test_full_automation(self, automation):
        """Tam otomasyon sürecini test eder - End-to-End"""
        with allure.step("Tam otomasyon testi başlatılıyor"):
            result = automation.run_full_automation()
            
        with allure.step("Tam otomasyon sonucu kontrol ediliyor"):
            assert result is not None, "Tam otomasyon testi sonucu None döndü"
            assert result, f"Tam otomasyon başarısız: {result}"
            
        allure.attach(
            f"Tam otomasyon başarılı: {result}",
            name="Test Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Giriş İşlemleri")
    @allure.story("Direkt Giriş Testi")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_direct_login(self, automation):
        """Sabit kullanıcı bilgileri ile direkt giriş testi"""
        with allure.step("Direkt giriş testi başlatılıyor"):
            result = automation.run_direct_login_test()
            
        with allure.step("Direkt giriş sonucu kontrol ediliyor"):
            assert result is not None, "Direkt giriş testi sonucu None döndü"
            assert result, f"Direkt giriş başarısız: {result}"
            
        allure.attach(
            f"Direkt giriş başarılı: {result}",
            name="Test Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Ürün İşlemleri")
    @allure.story("Ürün Seçimi Testi")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_selection(self, automation):
        """Ürün seçimi işlevselliğini test eder"""
        with allure.step("Ürün seçimi testi başlatılıyor"):
            result = automation.run_product_selection_test()
            
        with allure.step("Ürün seçimi sonucu kontrol ediliyor"):
            assert result is not None, "Ürün seçimi testi sonucu None döndü"
            assert result, f"Ürün seçimi başarısız: {result}"
            
        allure.attach(
            f"Ürün seçimi başarılı: {result}",
            name="Test Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Sepet İşlemleri")
    @allure.story("Sepete Ekleme Testi")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_cart(self, automation):
        """Sepete ekleme işlevselliğini test eder"""
        with allure.step("Sepete ekleme testi başlatılıyor"):
            result = automation.run_add_to_cart_test()
            
        with allure.step("Sepete ekleme sonucu kontrol ediliyor"):
            assert result is not None, "Sepete ekleme testi sonucu None döndü"
            assert result, f"Sepete ekleme başarısız: {result}"
            
        allure.attach(
            f"Sepete ekleme başarılı: {result}",
            name="Test Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Sepet İşlemleri")
    @allure.story("Sepet Operasyonları Testi")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_operations(self, automation):
        """Sepet operasyonlarını test eder"""
        with allure.step("Sepet operasyonları testi başlatılıyor"):
            result = automation.run_cart_operations_test()
            
        with allure.step("Sepet operasyonları sonucu kontrol ediliyor"):
            assert result is not None, "Sepet operasyonları testi sonucu None döndü"
            assert result, f"Sepet operasyonları başarısız: {result}"
            
        allure.attach(
            f"Sepet operasyonları başarılı: {result}",
            name="Test Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Giriş İşlemleri")
    @allure.story("Tam Giriş Testi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_full_login(self, automation):
        """Tam giriş sürecini test eder"""
        with allure.step("Tam giriş testi başlatılıyor"):
            result = automation.run_full_login_test()
            
        with allure.step("Tam giriş sonucu kontrol ediliyor"):
            assert result is not None, "Tam giriş testi sonucu None döndü"
            assert result, f"Tam giriş başarısız: {result}"
            
        allure.attach(
            f"Tam giriş başarılı: {result}",
            name="Test Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Navigasyon")
    @allure.story("Adım Adım Test")
    @allure.severity(allure.severity_level.NORMAL)
    def test_step_by_step_navigation(self, automation):
        """Adım adım navigasyon testini çalıştırır"""
        with allure.step("Adım adım navigasyon testi başlatılıyor"):
            result = automation.run_step_by_step_test()
            
        with allure.step("Adım adım navigasyon sonucu kontrol ediliyor"):
            assert result is not None, "Adım adım navigasyon testi sonucu None döndü"
            assert result, f"Adım adım navigasyon başarısız: {result}"
            
        allure.attach(
            f"Adım adım navigasyon başarılı: {result}",
            name="Test Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
