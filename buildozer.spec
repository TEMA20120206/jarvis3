[app]
title = Jarvis Controller
package.name = jarvis
package.domain = org.jarvis
version = 1.0.0
source.dir = .
main.py = main.py

# Добавил python-for-android и cython, чтобы избежать ошибок при сборке
requirements = python3,kivy,requests,plyer,cython==3.0.11

android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

# Убрал жесткую привязку к android.ndk = 23c, пусть Buildozer сам выберет совместимую
android.api = 33
android.minapi = 21
android.targetapi = 33

android.accept_sdk_license = True
android.exclude_android_tests = True

[buildozer]
log_level = 2
warn_on_root = 0
