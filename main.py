from flask import Flask,request,render_template
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler


user_socket_list = []
app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])

@app.route('/hello')
def hello():
  return 'Hello World'


@app.route('/ws')
def ws():
  user_socket = request.environ.get('wsgi.websocket')
  
  if user_socket:
    user_socket_list.append(user_socket)
    print(user_socket_list)
  else:
    print('请使用websocket连接')

  while True:
    msg = user_socket.receive()
    print(msg)
    for socket in user_socket_list:
      try:
        socket.send(msg)
      except geventwebsocket.exceptions.WebSocketError as e:
        pass


if __name__ =='__main__':
 
  # app.run(host="0.0.0.0",debug=app.config['DEBUG'],port=81)
  http_serv = WSGIServer(('0.0.0.0',5000),app,handler_class=WebSocketHandler)
  http_serv.serve_forever()