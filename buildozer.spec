[app]

title = Jarvis Controller
package.name = jarvis
package.domain = org.jarvis

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 1.0.0

requirements = python3,kivy==2.3.0,requests,plyer

orientation = portrait

android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_MULTICAST_STATE

android.api = 33
android.minapi = 21
android.targetapi = 33

android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True

fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0
