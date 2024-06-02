from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample dictionary to store user data
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/status')
def get_status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"})

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    users[username] = data
    return jsonify({"message": "User added", "user": data})

if __name__ == "__main__":
    app.run(debug=True)
