#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ürün Testleri
Ürün seçimi ve işlemleri ile ilgili testler
"""

import pytest
import allure
from pages.hepsiburada_automation import HepsiburadaAutomation


@pytest.mark.product
class TestProduct:
    """Ürün test sınıfı"""
    
    @allure.feature("Ürün İşlemleri")
    @allure.story("Ürün Seçimi Testi")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_selection(self, automation):
        """Ürün seçimi işlevselliğini test eder"""
        with allure.step("Ürün seçimi testi başlatılıyor"):
            result = automation.run_product_selection_test()
            
        with allure.step("Ürün seçimi sonucu doğrulanıyor"):
            assert result is not None, "Ürün seçimi testi sonucu None döndü"
            assert result, f"Ürün seçimi başarısız: {result}"
            
        allure.attach(
            f"Ürün seçimi başarılı: {result}",
            name="Ürün Seçimi Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Ürün İşlemleri")
    @allure.story("Filtreli Ürün Seçimi")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_filtered_product_selection(self, automation):
        """Filtreli ürün seçimi işlevselliğini test eder"""
        with allure.step("Filtreli ürün seçimi testi başlatılıyor"):
            result = automation.select_and_click_first_product()
            
        with allure.step("Filtreli ürün seçimi sonucu doğrulanıyor"):
            assert result is not None, "Filtreli ürün seçimi testi sonucu None döndü"
            assert result, f"Filtreli ürün seçimi başarısız: {result}"
            
        allure.attach(
            f"Filtreli ürün seçimi başarılı: {result}",
            name="Filtreli Ürün Seçimi Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Ürün İşlemleri")
    @allure.story("Laptop Kategorisi Seçimi")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_laptop_category_selection(self, automation):
        """Laptop kategorisi seçimi işlevselliğini test eder"""
        with allure.step("Laptop kategorisi seçimi testi başlatılıyor"):
            result = automation.select_laptop_after_registration()
            
        with allure.step("Laptop kategorisi seçimi sonucu doğrulanıyor"):
            assert result is not None, "Laptop kategorisi seçimi testi sonucu None döndü"
            assert result, f"Laptop kategorisi seçimi başarısız: {result}"
            
        allure.attach(
            f"Laptop kategorisi seçimi başarılı: {result}",
            name="Laptop Kategorisi Seçimi Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Ürün İşlemleri")
    @allure.story("Ürün Filtreleme Testi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_filtering(self, automation):
        """Ürün filtreleme işlevselliğini test eder"""
        with allure.step("Ürün filtreleme testi başlatılıyor"):
            # Önce giriş yap
            login_result = automation.run_direct_login_test()
            assert login_result, "Giriş başarısız"
            
            # Sonra ürün seçimi yap
            result = automation.run_product_selection_test()
            
        with allure.step("Ürün filtreleme sonucu doğrulanıyor"):
            assert result is not None, "Ürün filtreleme testi sonucu None döndü"
            assert result, f"Ürün filtreleme başarısız: {result}"
            
        allure.attach(
            f"Ürün filtreleme başarılı: {result}",
            name="Ürün Filtreleme Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Ürün İşlemleri")
    @allure.story("Ürün Detay Sayfası Testi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_detail_page(self, automation):
        """Ürün detay sayfası işlevselliğini test eder"""
        with allure.step("Ürün detay sayfası testi başlatılıyor"):
            # Önce giriş yap
            login_result = automation.run_direct_login_test()
            assert login_result, "Giriş başarısız"
            
            # Sonra filtrelenmiş ürün seçimi yap
            result = automation.select_and_click_first_product()
            
        with allure.step("Ürün detay sayfası sonucu doğrulanıyor"):
            assert result is not None, "Ürün detay sayfası testi sonucu None döndü"
            assert result, f"Ürün detay sayfası başarısız: {result}"
            
        allure.attach(
            f"Ürün detay sayfası başarılı: {result}",
            name="Ürün Detay Sayfası Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
