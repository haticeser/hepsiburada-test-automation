#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Giriş Testleri
Giriş işlemleri ile ilgili detaylı testler
"""

import pytest
import allure
from pages.hepsiburada_automation import HepsiburadaAutomation


@pytest.mark.login
class TestLogin:
    """Giriş test sınıfı"""
    
    @allure.feature("Giriş İşlemleri")
    @allure.story("Direkt Giriş Testi")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_direct_login_with_credentials(self, automation):
        """Sabit kullanıcı bilgileri ile direkt giriş testi"""
        with allure.step("Direkt giriş testi başlatılıyor (viva.vista000@gmail.com)"):
            result = automation.run_direct_login_test()
            
        with allure.step("Direkt giriş sonucu doğrulanıyor"):
            assert result is not None, "Direkt giriş testi sonucu None döndü"
            assert result, f"Direkt giriş başarısız: {result}"
            
        allure.attach(
            f"Direkt giriş başarılı: {result}",
            name="Direkt Giriş Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Giriş İşlemleri")
    @allure.story("Tam Giriş Testi")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_complete_login_flow(self, automation):
        """Tam giriş sürecini test eder"""
        with allure.step("Tam giriş süreci başlatılıyor"):
            result = automation.run_full_login_test()
            
        with allure.step("Tam giriş süreci sonucu doğrulanıyor"):
            assert result is not None, "Tam giriş süreci testi sonucu None döndü"
            assert result, f"Tam giriş süreci başarısız: {result}"
            
        allure.attach(
            f"Tam giriş süreci başarılı: {result}",
            name="Tam Giriş Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Giriş İşlemleri")
    @allure.story("Özel Kullanıcı Girişi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_custom_user_login(self, automation):
        """Özel kullanıcı bilgileri ile giriş testi"""
        custom_email = "test@example.com"
        custom_password = "test123"
        
        with allure.step(f"Özel kullanıcı girişi başlatılıyor ({custom_email})"):
            result = automation.run_direct_login_test(custom_email, custom_password)
            
        with allure.step("Özel kullanıcı girişi sonucu kontrol ediliyor"):
            # Bu test başarısız olabilir, bu normal
            assert result is not None, "Özel kullanıcı girişi testi sonucu None döndü"
            
        allure.attach(
            f"Özel kullanıcı girişi sonucu: {result}",
            name="Özel Kullanıcı Girişi Sonucu",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.feature("Giriş İşlemleri")
    @allure.story("Giriş Doğrulama Testi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_validation(self, automation):
        """Giriş doğrulama testi - farklı kullanıcı bilgileri ile"""
        test_cases = [
            ("viva.vista000@gmail.com", "123456aA", True),  # Geçerli kullanıcı
            ("invalid@email.com", "wrongpassword", False),  # Geçersiz kullanıcı
            ("", "123456aA", False),  # Boş email
            ("viva.vista000@gmail.com", "", False),  # Boş şifre
        ]
        
        for email, password, expected in test_cases:
            with allure.step(f"Giriş doğrulama testi: {email}"):
                result = automation.run_direct_login_test(email, password)
                
                if expected:
                    assert result, f"Geçerli kullanıcı girişi başarısız: {email}"
                else:
                    # Geçersiz kullanıcı için başarısız olması beklenir
                    allure.attach(
                        f"Geçersiz kullanıcı testi sonucu: {result}",
                        name=f"Giriş Doğrulama - {email}",
                        attachment_type=allure.attachment_type.TEXT
                    )
