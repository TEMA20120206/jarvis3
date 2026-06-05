[app]
title = Jarvis Controller
package.name = jarvis
package.domain = org.jarvis
version = 1.0.0
source.dir = .
main.py = main.py

requirements = python3,kivy,requests,plyer,cython==3.0.11

# Добавлены все необходимые разрешения
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, CHANGE_WIFI_MULTICAST_STATE, WAKE_LOCK, RECEIVE_BOOT_COMPLETED

android.api = 33
android.minapi = 21
android.targetapi = 33

android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
