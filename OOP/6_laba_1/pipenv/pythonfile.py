import requests
from flask import Flask, jsonify, request

response = requests.get('https://httpbin.org/')
print("5252")
for line in response.iter_lines():
    print(line)


app = Flask(__name__)

# Наші "дані" (типу імітація бази даних)
items = [
    {"id": 1, "name": "Python"},
    {"id": 2, "name": "Flask"},
    {"id": 3, "name": "SQLAlchemy"}
]

@app.route('/')
def home():
    return "Сервер фуричить! Спробуй /api/items"

@app.route('/api/items', methods=['GET'])
def get_items():
    # Повертаємо список у форматі JSON
    return jsonify(items)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Шукаємо один елемент за ID
    item = next((i for i in items if i['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Не знайшов такого"}), 404

if __name__ == '__main__':
    # debug=True автоматично перезавантажує сервер, коли ти міняєш код
    app.run(debug=True, port=5002)

