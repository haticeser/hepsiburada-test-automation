#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smoke Testler - Temel İşlevsellik
Hızlı çalışan, kritik işlevsellik testleri
"""

import pytest
import allure
from pages.hepsiburada_automation import HepsiburadaAutomation


@pytest.mark.smoke
class TestSmoke:
    """Smoke test sınıfı - temel işlevsellik testleri"""
    
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
        """Temel ürün seçimi işlevselliğini test eder"""
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
