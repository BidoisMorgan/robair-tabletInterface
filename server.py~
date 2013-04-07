#!/usr/bin/env python
import redis
import datetime
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template,session, redirect
 
red = redis.StrictRedis()
app = Flask(__name__)
app.secret_key = 'blablabla'

@app.route('/')
def reserver():
    return render_template('reservation.html')
  
@app.route('/commande')
def index():
    return render_template('navigation.html')
 
@app.route('/api')
def api():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        while True:
            message = ws.receive()
            test(message)
            ws.send(message)
    return
    
 
if __name__ == '__main__':
    address = "127.0.0.1", 5000
    http_server = WSGIServer(address, app, handler_class=WebSocketHandler)
    print("Server running on http://%s:%d. Ctrl+C to quit" % address)
    http_server.serve_forever()
