import socket
import struct
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import requests

class JarvisBackground(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        # Статусный лог
        self.status_label = Label(
            text="J.A.R.V.I.S. Инициализация...",
            font_size='18sp',
            color=(0, 0.8, 1, 1)  # Неоновый голубой
        )
        self.add_widget(self.status_label)

        # Кнопка Wake-on-LAN
        self.wol_button = Button(
            text="ВКЛЮЧИТЬ ПК (WOL)",
            background_color=(0, 0.5, 0.8, 1),
            font_size='20sp'
        )
        self.wol_button.bind(on_press=self.start_wol_thread)
        self.add_widget(self.wol_button)

        # Кнопка Запуска Игры (HTTP)
        self.game_button = Button(
            text="ЗАПУСТИТЬ CS",
            background_color=(0, 0.7, 0.5, 1),
            font_size='20sp'
        )
        self.game_button.bind(on_press=self.start_http_thread)
        self.add_widget(self.game_button)

    def update_status(self, text):
        self.status_label.text = text

    # --- Потоки во избежание фризов UI ---
    def start_wol_thread(self, instance):
        self.update_status("Отправка макропакета WOL...")
        threading.Thread(target=self.send_wol, daemon=True).start()

    def start_http_thread(self, instance):
        self.update_status("Запрос на запуск игры...")
        threading.Thread(target=self.send_http_request, daemon=True).start()

    # --- Логика WOL ---
    def send_wol(self):
        # ЗАМЕНИ НА СВОЙ MAC-АДРЕС ПК
        mac_address = "30-C5-99-28-8B-2D" 
        try:
            add_sep = mac_address.replace(":", "")
            data = ''.join(['FFFFFFFFFFFF', add_sep * 16])
            packet = struct.pack('B' * 102, *[int(data[i:i+2], 16) for i in range(0, len(data), 2)])
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(packet, ('255.255.255.255', 9))
            sock.close()
            Clock.schedule_once(lambda dt: self.update_status("Пакет WOL успешно отправлен!"), 0)
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_status(f"Ошибка WOL: {str(e)}"), 0)

    # --- Логика HTTP ---
    def send_http_request(self):
        # ЗАМЕНИ НА IP СВОЕГО СЕРВЕРА НА ПК
        url = "http://192.168.0.110:5000/start-game" 
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                Clock.schedule_once(lambda dt: self.update_status("Команда на ПК выполнена!"), 0)
            else:
                Clock.schedule_once(lambda dt: self.update_status(f"Код сервера: {response.status_code}"), 0)
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_status(f"Ошибка сети: {str(e)}"), 0)

class JarvisApp(App):
    def build(self):
        return JarvisBackground()

if __name__ == '__main__':
    JarvisApp().run()
