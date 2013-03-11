#!/usr/bin/env python
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template
 
app = Flask(__name__)
 
@app.route('/')
def reserver():
    return render_template('Reservation.html')
  
@app.route('/commande')
def index():
    return render_template('index2.html')
 
@app.route('/api')
def api():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        while True:
            message = ws.receive()
            test(message)
            ws.send(message)
    return
  
def test(msg):
    print msg + ' toto'
 
if __name__ == '__main__':
    address = "127.0.0.1", 5000
    http_server = WSGIServer(address, app, handler_class=WebSocketHandler)
    print("Server running on http://%s:%d. Ctrl+C to quit" % address)
    http_server.serve_forever()
