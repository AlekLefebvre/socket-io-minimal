from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*", logger=True, engineio_logger=True)


def create_app():
    app = Flask(__name__)

    socketio.init_app(app, message_queue='redis://localhost:6379/0', )

    return app

@socketio.on_error()
def error_handler(e):
    print("ERROR")
    print(e)

@socketio.on('get_count')
def get_count(site_id):
    # This is not called after a while.
    print('count')
    socketio.emit('count')


app = create_app()

if __name__ == '__main__':
    socketio.run(app)