from flask import Flask, render_template, request, redirect, url_for, abort
import socket
import threading
import json
from datetime import datetime

app = Flask(__name__)

# Путь для хранения JSON-файла
DATA_FILE = 'storage/data.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']

        # Отправка данных через сокет
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(f'{username},{message}'.encode('utf-8'), ('localhost', 5000))

        return redirect(url_for('index'))

    return render_template('message.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

def start_socket_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 5000))
    print("Socket server running on port 5000")
    
    while True:
        data, _ = sock.recvfrom(1024)
        try:
            username, message = data.decode('utf-8').split(',', 1)
            timestamp = datetime.now().isoformat()
            record = {
                timestamp: {
                    'username': username,
                    'message': message
                }
            }
            
            # Запись в JSON файл
            try:
                with open(DATA_FILE, 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = {}

            data.update(record)

            with open(DATA_FILE, 'w') as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print(f"Error processing message: {e}")

if __name__ == '__main__':
    # Запуск HTTP сервера и сокет-сервера в разных потоках
    socket_thread = threading.Thread(target=start_socket_server, daemon=True)
    socket_thread.start()
    
    app.run(port=3000)
