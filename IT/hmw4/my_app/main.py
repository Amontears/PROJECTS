import os
import json
from flask import Flask, render_template, request, redirect, url_for
import socket
import threading
from datetime import datetime

app = Flask(__name__)

# Определите путь к директории хранения
STORAGE_PATH = 'storage'

# Создайте директорию, если она не существует
if not os.path.exists(STORAGE_PATH):
    os.makedirs(STORAGE_PATH)

# Определите путь к файлу данных
data_file_path = os.path.join(STORAGE_PATH, 'data.json')

# Создайте файл данных, если он не существует
if not os.path.exists(data_file_path):
    with open(data_file_path, 'w') as f:
        json.dump({}, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        
        # Отправка данных на сокет сервер
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('localhost', 5000)
        data = json.dumps({'username': username, 'message': message})
        sock.sendto(data.encode(), server_address)
        sock.close()
        
        return redirect(url_for('index'))
    return render_template('message.html')

def run_socket_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 5000))

    while True:
        data, _ = sock.recvfrom(4096)
        message = json.loads(data.decode())

        # Запись данных в файл
        with open(data_file_path, 'a') as f:
            timestamp = datetime.now().isoformat()
            json.dump({timestamp: message}, f)
            f.write('\n')

if __name__ == '__main__':
    # Запуск сокет-сервера в отдельном потоке
    threading.Thread(target=run_socket_server, daemon=True).start()
    
    # Запуск Flask-приложения
    app.run(host='0.0.0.0', port=3000)
