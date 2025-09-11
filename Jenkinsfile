pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.9'
        ALLURE_RESULTS = 'allure-results'
        REPORTS_DIR = 'reports'
        SCREENSHOTS_DIR = 'screenshots'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '📥 Repository checkout ediliyor...'
                checkout scm
            }
        }
        
        stage('Environment Setup') {
            steps {
                echo '🔧 Python ortamı hazırlanıyor...'
                script {
                    // Python sürümünü kontrol et
                    bat 'python --version'
                    
                    // Gerekli dizinleri oluştur
                    bat 'if not exist allure-results mkdir allure-results'
                    bat 'if not exist reports mkdir reports'
                    bat 'if not exist screenshots mkdir screenshots'
                }
            }
        }
        
        stage('Dependencies Install') {
            steps {
                echo '📦 Bağımlılıklar yükleniyor...'
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Test Execution') {
            steps {
                echo '🧪 Tüm testler sıralı olarak çalıştırılıyor...'
                bat 'pytest tests/ -v --tb=short --alluredir=allure-results --html=reports/test_report.html --self-contained-html --maxfail=1'
            }
            post {
                always {
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'test_report.html',
                        reportName: 'Test Report'
                    ])
                }
            }
        }
        
        stage('Allure Report Generation') {
            steps {
                echo '📊 Allure raporu oluşturuluyor...'
                script {
                    // Allure raporu oluştur
                    bat 'allure generate allure-results -o allure-report --clean'
                    
                    // Allure raporunu arşivle (Windows için PowerShell kullan)
                    bat 'powershell -Command "Compress-Archive -Path allure-report -DestinationPath allure-report.zip -Force"'
                }
            }
        }
        
        stage('Test Summary') {
            steps {
                echo '📋 Test özeti oluşturuluyor...'
                script {
                    // Test sonuçlarını topla
                    bat '''
                        echo === TEST ÖZETİ === > test_summary.txt
                        echo Tarih: %date% %time% >> test_summary.txt
                        echo Branch: %GIT_BRANCH% >> test_summary.txt
                        echo Commit: %GIT_COMMIT% >> test_summary.txt
                        echo. >> test_summary.txt
                        echo === PYTEST SONUÇLARI === >> test_summary.txt
                        pytest --collect-only -q >> test_summary.txt 2>&1
                    '''
                }
            }
        }
    }
    
    post {
        always {
            echo '🧹 Temizlik işlemleri yapılıyor...'
            script {
                // Screenshot'ları arşivle (Windows için PowerShell)
                bat 'powershell -Command "if (Test-Path screenshots) { Compress-Archive -Path screenshots -DestinationPath screenshots.zip -Force }"'
                
                // Log dosyalarını temizle
                bat 'del /q *.log 2>nul || echo Log dosyası bulunamadı'
                
                // Artifacts arşivle
                echo '📦 Artifacts arşivleniyor...'
                archiveArtifacts artifacts: 'allure-report.zip', fingerprint: true
                archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
                archiveArtifacts artifacts: 'screenshots.zip', fingerprint: true
                archiveArtifacts artifacts: 'test_summary.txt', fingerprint: true
            }
        }
        
        success {
            echo '✅ Tüm testler başarıyla tamamlandı!'
            script {
                // Başarılı build için bildirim
                emailext (
                    subject: "✅ Hepsiburada Test Automation - Build Başarılı",
                    body: """
                    <h2>🎉 Test Otomasyonu Başarıyla Tamamlandı!</h2>
                    <p><strong>Build:</strong> ${BUILD_NUMBER}</p>
                    <p><strong>Branch:</strong> ${GIT_BRANCH}</p>
                    <p><strong>Commit:</strong> ${GIT_COMMIT}</p>
                    <p><strong>Süre:</strong> ${currentBuild.durationString}</p>
                    
                    <h3>📊 Raporlar:</h3>
                    <ul>
                        <li><a href="${BUILD_URL}allure/">Allure Raporu</a></li>
                        <li><a href="${BUILD_URL}HTML_Report/">HTML Raporları</a></li>
                    </ul>
                    """,
                    to: "test-team@company.com"
                )
            }
        }
        
        failure {
            echo '❌ Testler başarısız oldu!'
            script {
                // Başarısız build için bildirim
                emailext (
                    subject: "❌ Hepsiburada Test Automation - Build Başarısız",
                    body: """
                    <h2>⚠️ Test Otomasyonu Başarısız!</h2>
                    <p><strong>Build:</strong> ${BUILD_NUMBER}</p>
                    <p><strong>Branch:</strong> ${GIT_BRANCH}</p>
                    <p><strong>Commit:</strong> ${GIT_COMMIT}</p>
                    <p><strong>Süre:</strong> ${currentBuild.durationString}</p>
                    
                    <h3>📊 Raporlar:</h3>
                    <ul>
                        <li><a href="${BUILD_URL}allure/">Allure Raporu</a></li>
                        <li><a href="${BUILD_URL}HTML_Report/">HTML Raporları</a></li>
                    </ul>
                    
                    <p>Lütfen logları kontrol edin ve gerekli düzeltmeleri yapın.</p>
                    """,
                    to: "test-team@company.com"
                )
            }
        }
        
        unstable {
            echo '⚠️ Testler kararsız durumda!'
        }
    }
}
