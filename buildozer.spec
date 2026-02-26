[app]

title = Esp32App

package.name = esp32app

package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1


[android]

android.ndk = 25b
android.ndk_api = 21

android.api = 33
android.minapi = 21

android.build_tools = 33.0.2

android.aab = False

android.permissions = INTERNET,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE

requirements = python3,kivy==2.2.1,kivymd==1.2.0,paho-mqtt,pyjnius

android.archs = arm64-v8a,armeabi-v7a

android.release = False

android.gradle_download = https://services.gradle.org/distributions/gradle-7.4.1-all.zip
android.gradle_plugin = 7.2.0


[buildozer]

log_level = 2

build_dir = ./.buildozer

cache_dir = ~/.buildozer

ignore_patterns = *.pyc,__pycache__,*.kv.orig,*.swp
