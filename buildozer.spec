[app]
title = Esp32MobileApp          
package.name = esp32app         
package.domain = org.esp32     
source.dir = .                 
source.include_exts = py,png,jpg,kv,atlas,pem  
version = 0.0.1                 
fullscreen = 0                 
orientation = portrait          

requirements = python3,kivy==2.2.1,kivymd==1.2.0,paho-mqtt,pyjnius,libiconv,libffi

entrypoint = main.py

android.accept_sdk_license = True
android.allow_api_min = 21
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.ndk_api = 21
exclude_patterns = **/test/*, **/tests/*
android.gradle_download = https://services.gradle.org/distributions/gradle-7.6.4-all.zip
android.gradle_plugin = 7.4.2
p4a.gradle_dependencies = gradle:7.6.4
p4a.bootstrap = sdl2
p4a.gradle_options = -Dorg.gradle.java.home=/usr/lib/jvm/java-17-openjdk-amd64

android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

android.aab = False

android.arch = arm64-v8a,armeabi-v7a

# 修正：删除开头的中文括号）
android.add_assets = ca.pem

android.blacklist_libs = libpython3.9.so

# 5. Release模式配置（暂时注释，调试阶段不用）
# android.keystore = /home/runner/work/RepositoryName/AndAgain/DomainName.PackageName.keystore
# android.keystore_storepass = android
# android.keystore_keypass = android
# android.keystore_alias = DomainName.PackageName

[buildozer]
log_level = 2                   
warn_on_root = 1  
