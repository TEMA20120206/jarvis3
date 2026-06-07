[app]
title = Jarvis Controller
package.name = jarvis
package.domain = org.jarvis
version = 1.0.0
source.dir = .
main.py = main.py

# ЖЕСТКАЯ ФИКСАЦИЯ ВЕРСИЙ
requirements = python3==3.11.9,hostpython3==3.11.9,kivy==2.3.0,requests,plyer,cython==3.0.11

android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, CHANGE_WIFI_MULTICAST_STATE

# ЯВНОЕ УКАЗАНИЕ NDK
android.ndk = 25b
android.api = 33
android.minapi = 21
android.targetapi = 33

android.accept_sdk_license = True
android.exclude_android_tests = True

[buildozer]
log_level = 2
warn_on_root = 0
