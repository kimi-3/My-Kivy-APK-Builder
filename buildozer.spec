[app]
# (必填) 应用名称
title = Esp32App
# (必填) 包名（小写，无空格）
package.name = esp32app
# (必填) 包域名（自定义）
package.domain = org.test
# (必填) 源码目录（当前目录）
source.dir = .
# (必填) 包含的文件后缀
source.include_exts = py,png,jpg,kv,atlas
# 版本号
version = 0.1

# 安卓配置
[android]
# 兼容的NDK版本（和workflow一致）
android.ndk = 25b
android.ndk_api = 21
# 安卓API版本（和workflow一致）
android.api = 33
android.minapi = 21
# 稳定版Build Tools（避免预览版许可问题）
android.build_tools = 33.0.2
# 强制生成APK（禁用AAB）
android.aab = False
# 应用权限（根据需求添加，比如网络权限）
android.permissions = INTERNET,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE
# (必填) 依赖列表（和workflow安装的版本一致）
requirements = python3,kivy==2.2.1,kivymd==1.2.0,paho-mqtt,pyjnius
# 架构（适配大多数安卓设备）
android.archs = arm64-v8a,armeabi-v7a
# 禁用签名（Debug模式无需签名）
android.release = False
# 简化gradle配置，减少兼容问题
android.gradle_download = https://services.gradle.org/distributions/gradle-7.4.1-all.zip
android.gradle_plugin = 7.2.0

# 通用配置
[buildozer]
# 日志级别（详细）
log_level = 2
# 构建目录
build_dir = ./.buildozer
# 缓存目录
cache_dir = ~/.buildozer
# 忽略的文件
ignore_patterns = *.pyc,__pycache__,*.kv.orig,*.swp
