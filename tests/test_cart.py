#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sepet Testleri
Sepet işlemleri ile ilgili testler
"""

import pytest
import allure
from pages.hepsiburada_automation import HepsiburadaAutomation


@pytest.mark.cart
class TestCart:
    """Sepet test sınıfı"""
    
    @allure.feature("Sepet İşlemleri")
    @allure.story("Sepete Ekleme Testi")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_cart(self, automation):
        """Sepete ekleme işlevselliğini test eder"""
        with allure.step("Sepete ekleme testi başlatılıyor"):
            result = automation.run_add_to_cart_test()
            
        with allure.step("Sepete ekleme sonucu doğrulanıyor"):
            assert result is not None, "Sepete ekleme testi sonucu None döndü"
            assert result, f"Sepete ekleme başarısız: {result}"
            
        allure.attach(
            f"Sepete ekleme başarılı: {result}",
            name="Sepete Ekleme Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Sepet İşlemleri")
    @allure.story("Sepet Operasyonları Testi")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_operations(self, automation):
        """Sepet operasyonlarını test eder"""
        with allure.step("Sepet operasyonları testi başlatılıyor"):
            result = automation.run_cart_operations_test()
            
        with allure.step("Sepet operasyonları sonucu doğrulanıyor"):
            assert result is not None, "Sepet operasyonları testi sonucu None döndü"
            assert result, f"Sepet operasyonları başarısız: {result}"
            
        allure.attach(
            f"Sepet operasyonları başarılı: {result}",
            name="Sepet Operasyonları Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Sepet İşlemleri")
    @allure.story("Sepet Miktar Artırma")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_quantity_increase(self, automation):
        """Sepetteki ürün miktarını artırma işlevselliğini test eder"""
        with allure.step("Sepet miktar artırma testi başlatılıyor"):
            # Önce sepete ürün ekle
            add_result = automation.run_add_to_cart_test()
            assert add_result, "Sepete ürün ekleme başarısız"
            
            # Sonra sepet operasyonlarını test et
            result = automation.run_cart_operations_test()
            
        with allure.step("Sepet miktar artırma sonucu doğrulanıyor"):
            assert result is not None, "Sepet miktar artırma testi sonucu None döndü"
            assert result, f"Sepet miktar artırma başarısız: {result}"
            
        allure.attach(
            f"Sepet miktar artırma başarılı: {result}",
            name="Sepet Miktar Artırma Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Sepet İşlemleri")
    @allure.story("Sepet Sayfası Testi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cart_page_navigation(self, automation):
        """Sepet sayfası navigasyonunu test eder"""
        with allure.step("Sepet sayfası testi başlatılıyor"):
            # Önce giriş yap
            login_result = automation.run_direct_login_test()
            assert login_result, "Giriş başarısız"
            
            # Sonra sepete ürün ekle
            add_result = automation.run_add_to_cart_test()
            assert add_result, "Sepete ürün ekleme başarısız"
            
            # Sonra sepet operasyonlarını test et
            result = automation.run_cart_operations_test()
            
        with allure.step("Sepet sayfası sonucu doğrulanıyor"):
            assert result is not None, "Sepet sayfası testi sonucu None döndü"
            assert result, f"Sepet sayfası başarısız: {result}"
            
        allure.attach(
            f"Sepet sayfası başarılı: {result}",
            name="Sepet Sayfası Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Sepet İşlemleri")
    @allure.story("Sepet Temizleme Testi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cart_clear(self, automation):
        """Sepet temizleme işlevselliğini test eder"""
        with allure.step("Sepet temizleme testi başlatılıyor"):
            # Önce giriş yap
            login_result = automation.run_direct_login_test()
            assert login_result, "Giriş başarısız"
            
            # Sonra sepete ürün ekle
            add_result = automation.run_add_to_cart_test()
            assert add_result, "Sepete ürün ekleme başarısız"
            
            # Sonra sepet operasyonlarını test et (temizleme dahil)
            result = automation.run_cart_operations_test()
            
        with allure.step("Sepet temizleme sonucu doğrulanıyor"):
            assert result is not None, "Sepet temizleme testi sonucu None döndü"
            assert result, f"Sepet temizleme başarısız: {result}"
            
        allure.attach(
            f"Sepet temizleme başarılı: {result}",
            name="Sepet Temizleme Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
