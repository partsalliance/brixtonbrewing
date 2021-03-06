from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from threading import Thread
import time
from random import randint
from TemperatureProbe import TemperatureProbe

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

thread = None


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    t = TemperatureProbe()
    while True:
        time.sleep(1.5)
        t = TemperatureProbe()
        socketio.emit('my response',
                      {'data': + float(t.read_temp())},
                      namespace='/test')


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return render_template('index.html')

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})
    print ("clien sent me %s"% message['data'])

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)

