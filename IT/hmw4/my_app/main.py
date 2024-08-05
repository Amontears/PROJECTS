from flask import Flask, render_template, request, redirect, url_for
import socket
import threading
import json
import os
from datetime import datetime

app = Flask(__name__)

# Константы
STORAGE_PATH = 'F:/PROJECTS/IT/hmw4/my_app/storage/data.json'
STOP_SOCKET_SERVER = threading.Event()

def save_data_to_json(data):
    if not os.path.exists(os.path.dirname(STORAGE_PATH)):
        os.makedirs(os.path.dirname(STORAGE_PATH))

    try:
        if os.path.exists(STORAGE_PATH):
            with open(STORAGE_PATH, 'r') as file:
                all_data = json.load(file)
        else:
            all_data = {}

        timestamp = datetime.now().isoformat()
        all_data[timestamp] = data

        with open(STORAGE_PATH, 'w') as file:
            json.dump(all_data, file, indent=4)

        print(f"Data saved: {timestamp} -> {data}")  # Отладочное сообщение
    except Exception as e:
        print(f"Error saving data: {e}")  # Отладочное сообщение

def start_socket_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('localhost', 5000))

    while not STOP_SOCKET_SERVER.is_set():
        try:
            message, _ = udp_socket.recvfrom(4096)
            data = json.loads(message.decode('utf-8'))
            print(f"Received data: {data}")  # Отладочное сообщение
            save_data_to_json(data)
        except Exception as e:
            print(f"Error receiving or processing data: {e}")  # Отладочное сообщение

    udp_socket.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        username = request.form.get('username')
        message = request.form.get('message')
        data = {'username': username, 'message': message}
        
        # Отправка данных на сокет-сервер
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.sendto(json.dumps(data).encode('utf-8'), ('localhost', 5000))
        udp_socket.close()
        
        return redirect(url_for('index'))

    return render_template('message.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    try:
        # Запуск HTTP сервера
        http_thread = threading.Thread(target=lambda: app.run(port=3000))
        http_thread.start()

        # Запуск сокет-сервера
        socket_thread = threading.Thread(target=start_socket_server)
        socket_thread.start()

        # Ожидание завершения работы потоков
        http_thread.join()
        STOP_SOCKET_SERVER.set()
        socket_thread.join()
    except KeyboardInterrupt:
        # Завершение работы при прерывании
        print("Shutting down...")
        STOP_SOCKET_SERVER.set()
