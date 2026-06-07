[app]
title = Jarvis Controller

package.name = jarvis
package.domain = org.jarvis

source.dir = .

version = 1.0.0

requirements = python3==3.11.9,kivy==2.3.0,requests,plyer

android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_MULTICAST_STATE

android.api = 33
android.minapi = 21
android.targetapi = 33

android.ndk = 25b

android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
