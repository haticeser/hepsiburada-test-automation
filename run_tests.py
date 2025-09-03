# run_tests.py
import os
import sys
import subprocess
import time
from datetime import datetime


def run_tests(test_type="all", verbose=False, parallel=False):
    """Testleri çalıştırır"""
    
    print("🚀 Hepsiburada Test Otomasyonu Başlatılıyor...")
    print("=" * 60)
    
    # Test dizinini kontrol et
    test_dir = os.path.join(os.path.dirname(__file__), "tests")
    if not os.path.exists(test_dir):
        print(f"❌ Test dizini bulunamadı: {test_dir}")
        return False
    
    # Pytest komutunu oluştur
    pytest_cmd = ["python", "-m", "pytest"]
    
    # Verbose mod
    if verbose:
        pytest_cmd.append("-v")
    
    # Parallel mod
    if parallel:
        pytest_cmd.extend(["-n", "auto"])
    
    # Test türüne göre dosya seç
    if test_type == "all":
        pytest_cmd.append(test_dir)
    elif test_type == "integration":
        pytest_cmd.append(os.path.join(test_dir, "test_integration.py"))
    elif test_type == "registration":
        pytest_cmd.append(os.path.join(test_dir, "test_registration.py"))
    elif test_type == "login":
        pytest_cmd.append(os.path.join(test_dir, "test_login.py"))
    elif test_type == "tempail":
        pytest_cmd.append(os.path.join(test_dir, "test_tempail.py"))
    else:
        print(f"❌ Bilinmeyen test türü: {test_type}")
        return False
    
    # HTML rapor oluştur
    report_dir = os.path.join(os.path.dirname(__file__), "reports")
    os.makedirs(report_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(report_dir, f"test_report_{timestamp}.html")
    
    pytest_cmd.extend([
        "--html", report_file,
        "--self-contained-html",
        "--capture", "no"
    ])
    
    print(f"🔍 Test türü: {test_type}")
    print(f"📊 Rapor dosyası: {report_file}")
    print(f"⚡ Komut: {' '.join(pytest_cmd)}")
    print("-" * 60)
    
    try:
        # Testleri çalıştır
        start_time = time.time()
        
        result = subprocess.run(
            pytest_cmd,
            capture_output=False,
            text=True,
            cwd=os.path.dirname(__file__)
        )
        
        end_time = time.time()
        duration = end_time - start_time
        
        print("-" * 60)
        print(f"⏱️ Test süresi: {duration:.2f} saniye")
        print(f"📊 Test sonucu: {'✅ BAŞARILI' if result.returncode == 0 else '❌ BAŞARISIZ'}")
        
        if result.returncode == 0:
            print("🎉 Tüm testler başarıyla tamamlandı!")
        else:
            print("💥 Bazı testler başarısız oldu!")
        
        # Rapor dosyası bilgisi
        if os.path.exists(report_file):
            print(f"📋 Detaylı rapor: {report_file}")
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Test çalıştırma hatası: {e}")
        return False


def show_test_menu():
    """Test menüsünü gösterir"""
    print("\n🧪 Test Seçenekleri:")
    print("1. Tüm testler (all)")
    print("2. Entegrasyon testleri (integration)")
    print("3. Kayıt testleri (registration)")
    print("4. Giriş testleri (login)")
    print("5. Tempail testleri (tempail)")
    print("6. Çıkış")
    
    while True:
        try:
            choice = input("\nSeçiminizi yapın (1-6): ").strip()
            
            if choice == "1":
                return "all"
            elif choice == "2":
                return "integration"
            elif choice == "3":
                return "registration"
            elif choice == "4":
                return "login"
            elif choice == "5":
                return "tempail"
            elif choice == "6":
                return None
            else:
                print("❌ Geçersiz seçim. Lütfen 1-6 arasında bir sayı girin.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Test iptal edildi.")
            return None
        except Exception as e:
            print(f"❌ Hata: {e}")


def main():
    """Ana fonksiyon"""
    print("🎯 Hepsiburada Test Otomasyonu")
    print("=" * 60)
    
    # Komut satırı argümanlarını kontrol et
    if len(sys.argv) > 1:
        test_type = sys.argv[1]
        verbose = "-v" in sys.argv or "--verbose" in sys.argv
        parallel = "-p" in sys.argv or "--parallel" in sys.argv
        
        print(f"🔍 Komut satırı argümanları:")
        print(f"   Test türü: {test_type}")
        print(f"   Verbose: {verbose}")
        print(f"   Parallel: {parallel}")
        print("-" * 60)
        
        success = run_tests(test_type, verbose, parallel)
        sys.exit(0 if success else 1)
    
    # İnteraktif mod
    while True:
        test_type = show_test_menu()
        
        if test_type is None:
            print("👋 Görüşürüz!")
            break
        
        # Verbose ve parallel seçenekleri
        verbose = input("Verbose mod? (y/n): ").strip().lower() == 'y'
        parallel = input("Parallel mod? (y/n): ").strip().lower() == 'y'
        
        print("-" * 60)
        success = run_tests(test_type, verbose, parallel)
        
        if not success:
            print("\n⚠ Testler başarısız oldu. Tekrar denemek ister misiniz?")
            retry = input("Tekrar dene? (y/n): ").strip().lower()
            if retry != 'y':
                break
        else:
            print("\n✅ Testler başarılı! Başka test çalıştırmak ister misiniz?")
            continue_test = input("Devam et? (y/n): ").strip().lower()
            if continue_test != 'y':
                break


if __name__ == "__main__":
    main()