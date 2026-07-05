from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import os

app = Flask(__name__)

io = SocketIO(app)

messages = []

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@io.on('sendMessage')
def send_message_handle(msg):
    messages.append(msg)
    emit('getMessage', msg, json=True, broadcast=True)

@io.on('message')
def message_handler(msgs):
    send(messages)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    io.run(app, host="0.0.0.0", port=port, debug=False)