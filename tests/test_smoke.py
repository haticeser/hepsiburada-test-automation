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
    @allure.issue("HEPS-001", "Tam otomasyon testi")
    @allure.testcase("TC-001", "Hepsiburada tam otomasyon test senaryosu")
    @pytest.mark.smoke
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
    
    @allure.feature("Üye Kaydı")
    @allure.story("Kullanıcı Kaydı")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("HEPS-002", "Üye kaydı testi")
    @allure.testcase("TC-002", "Hepsiburada üye kaydı test senaryosu")
    @pytest.mark.regression
    def test_user_registration(self, automation):
        """Üye kaydı testini çalıştırır"""
        with allure.step("Üye kaydı testi başlatılıyor"):
            result = automation.run_registration_test()
            
        with allure.step("Üye kaydı sonucu kontrol ediliyor"):
            assert result is not None, "Üye kaydı testi sonucu None döndü"
            assert result, f"Üye kaydı başarısız: {result}"
    
    @allure.feature("Ürün Seçimi")
    @allure.story("E-ticaret İşlemleri")
    @allure.severity(allure.severity_level.MINOR)
    @allure.issue("HEPS-003", "Ürün seçimi testi")
    @allure.testcase("TC-003", "Hepsiburada ürün seçimi test senaryosu")
    @pytest.mark.product
    def test_product_selection(self, automation):
        """Ürün seçimi testini çalıştırır"""
        with allure.step("Ürün seçimi testi başlatılıyor"):
            result = automation.run_product_test()
            
        with allure.step("Ürün seçimi sonucu kontrol ediliyor"):
            assert result is not None, "Ürün seçimi testi sonucu None döndü"
            assert result, f"Ürün seçimi başarısız: {result}"
    
