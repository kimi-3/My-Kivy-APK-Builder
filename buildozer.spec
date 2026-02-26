[app]
# 1. 项目基础配置（适配你的ESP32项目）
title = Esp32MobileApp          # 应用名称（手机端显示）
package.name = esp32app         # 包名（小写，无特殊字符）
package.domain = org.esp32      # 域名（release模式不能用org.test，改为自定义）
source.dir = .                  # 工作目录（保持不变）
source.include_exts = py,png,jpg,kv,atlas,pem  # 新增pem（CA证书）
version = 0.0.1                 # 版本号
fullscreen = 0                  # 非全屏（手机端友好）
orientation = portrait          # 强制竖屏（适配手机）

# 2. 核心依赖（新增MQTT，固定版本避免兼容问题）
requirements = python3,kivy==2.2.1,kivymd==1.2.0,paho-mqtt,pyjnius,libiconv,libffi

# 3. 程序入口（匹配你的main.py）
entrypoint = main.py

# 4. 安卓关键配置（修复APK生成 + 网络权限）
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

# 关键：补充网络权限（MQTT必须）
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

# 关键：强制生成APK（关闭默认的AAB）
android.aab = False

# 关键：适配手机架构（减少构建体积，支持主流安卓手机）
android.arch = arm64-v8a,armeabi-v7a

# 可选：添加CA证书到APK（MQTT TLS需要）
android.add_assets = ca.pem

# 可选：禁用黑窗口（手机端无控制台）
android.blacklist_libs = libpython3.9.so

# 5. Release模式配置（暂时注释，调试阶段不用）
# android.keystore = /home/runner/work/RepositoryName/AndAgain/DomainName.PackageName.keystore
# android.keystore_storepass = android
# android.keystore_keypass = android
# android.keystore_alias = DomainName.PackageName

[buildozer]
log_level = 2                   # 日志级别（2=详细，便于调试）
warn_on_root = 1                # 根用户警告（保持不变）
