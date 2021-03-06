#!/usr/bin/env python
import redis
import datetime
import threading
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template,session, redirect

#import roslib
#roslib.load_manifest('robair_driver')

class TabletNode(threading.Thread):
    '''Robair Tablet node'''
    def __init__(self, topic='/cmd', node_name="tablet"):
    	print("init\n")
        self.node_name = node_name
#        self.pub = rospy.Publisher(topic, Command)
#        rospy.init_node('tablet')

#    def main_loop(self):
#        done = lambda: rospy.is_shutdown()

    def key_pressed(self, key):
        directions = {"top": (1, 0), "bottom": (-1, 0),
                      "left": (None, -90), "right": (None, 90)}
        if key in directions.keys():
             print("%s" % key)
#            self.pub.publish(Command(*directions[key]))
            


tablet= TabletNode()
red = redis.StrictRedis()
app = Flask(__name__)
app.secret_key = 'blablabla'

@app.route('/')
def reserver():
    return render_template('reservation.html')
  
@app.route('/commande')
def index():
    return render_template('navigation.html')
 
@app.route('/commande/api')
def goApi():
    api();
    
@app.route('/api')
def api():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        while True:
            message = ws.receive()
            tablet.key_pressed(message)
            ws.send(message)
    return
 
if __name__ == '__main__':
    address = "127.0.0.1", 5000
    http_server = WSGIServer(address, app, handler_class=WebSocketHandler)
    #tablet.main_loop()
    print("Server running on http://%s:%d. Ctrl+C to quit" % address)
    http_server.serve_forever()
    
