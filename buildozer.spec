[app]
title = Jarvis Controller
package.name = jarviscontroller
package.domain = org.jarvis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

requirements = python3==3.11.9,hostpython3==3.11.9,kivy==2.3.0,kivymd,requests

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# КРИТИЧЕСКИЕ НАСТРОЙКИ ДЛЯ ФИКСА
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_path = /home/runner/work/jarvis3/jarvis3/android-ndk-r25b
p4a.source_dir = ./python-for-android

[buildozer]
log_level = 2
warn_on_root = 1
